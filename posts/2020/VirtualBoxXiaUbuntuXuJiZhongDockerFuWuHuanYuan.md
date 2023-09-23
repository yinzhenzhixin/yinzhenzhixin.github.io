之前公司测试服务器利用WSL2+Ubuntu+Docker，架起了Jenkins，Gitea和PypiServer多个服务供大家使用非常方便。但是由于公司网络收ZScaler影响，同时不太喜欢WSL2的docker以来windows端desktop等多种因素，决议将docker desktop甚至wsl2 ubuntu弃用。

-   由于测试服务器基于WIN10，且有16G内存，比较够用，希望引入VirtualBox安装完整的Ubuntu Server，版本选择20.04LTS，安装完成后，在还原以上三个服务data的过程中，总结一下经验：VirtualBox中的Ubuntu VM作为Guest，如果需要和Host机（WIN10）以及局域网其他机器组网，需要将Ubutnu VM的网络设置成NAT，同时添加port forwarding，这个可以手动在VirtualBox中添加或者使用其提供的命令行，需要什么端口添加什么，Host IP选择0.0.0.0，Guest IP选择Ubuntu VM通过ip a查到的内部IP，一般是类似10.0.1.25之类的，port根据需要添加，比如SSH的22，HTTP的80等等。
-   如果需要VirtualBox的Ubuntu VM在Host也就是WIN10启动后自动启动，可以在WIN10计划任务中添加引用bat，大概如下：

```
@ECHO OFF
cd C:\Program Files\Oracle\VirtualBox\
start VBoxManage startvm CentOS7 --type headless
Exit
```

-   由于一开始给Ubuntu VM的disk分配只有10G，后续需要扩容的话，首先在VirtualBox相关菜单设置（前提是你的host有足够的磁盘剩余空间，废话），设置完毕后，需要进入Ubuntu VM，在linux下通过fdisk和mount等命令添加和初始化新加入的磁盘空间，并且在ftab添加自动挂载。
-   如果需要将Host机子其他磁盘或文件夹share给Ubuntu VM，首先在VirtualBox相关菜单添加，设置文件夹名和挂载点（建议保持一致），然后需要在VM启动后插入VBoxsGuestAdditions.iso，进入Ubuntu并安装依赖及上述扩展包。

```
sudo apt install virtualbox-guest-utils virtualbox-guest-dkms
sudo ./VBoxLinuxAdditions.run
```

-   VirtualBox貌似强制要求shared folder挂在到了一个叫做vboxsf的用户组下面，并且无法修改为你需要的用户组。这就意味着，如果你原先docker service相关volume的data在shared folder里，同时这些data需要特定的用户组，比如root、git等，那你必须将其从shared folder移动到ubuntu本机某个目录下，以方便修改group。
-   在还原gitea和pypiserver这两个服务中遇到的问题，主要是上述group不对的问题，因为如果group不对，这些service（container）起不来，通过docker logs查看会发现多数是Deny Permission之类的，此时需要分别手动起一个初始化的service，看看相关的data的group和user具体是哪个，然后回到ubuntu，创建相同的group和user，并使用chgrp -R和chown -R从相关service的data下顶级目录改变其下所有目录的group和user（切记加-R，否则你得一个一个folder改，天知道有多少folder和files需要改）