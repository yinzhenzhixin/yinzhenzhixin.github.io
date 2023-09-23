Sometimes you may encounter the error "Server execution failed" when run any wsl commands, somehow because of unexpected windows updates. There are some steps for reinstall and recovery it.

[http://1.In](https://link.zhihu.com/?target=http%3A//1.In) powershell (as admin, not necessary if you vhdx file places in other partitions rather than C)

```
# list all installed distros
wsl -l -v
# destroy distros
wsl --unregister Ubuntu
wsl --unregister Debian # and so on
```

2\. In Settings > Apps > Apps & Features

-   search for `Ubuntu` (then `Debian`, etc), and if something is found, click on uninstall
-   search for `Linux`, and if something is found, click on uninstall on all results

3\. In Start Menu > Turn Windows Features on or off

-   Untick `Virtual Machine Platform` checkbox
-   Untick `Windows Subsystem for Linux` checkbox

4\. Reboot and enable the checkboxes above, and reboot again

5\. Open Powershell with administrator , run the following commands

```
run wsl --update
run wsl --install -d Debian
```