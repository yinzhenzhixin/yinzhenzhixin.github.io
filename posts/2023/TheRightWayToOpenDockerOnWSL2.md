You know I know that It's fantastic to run docker on WSL2. Moreover, it's more exiting to run it without docker desktop. How?

Let's say you have WSL2 ready with Debian or Ubuntu. There are two approaches below to install docker engine on your system.

1\. Just follow the docker official [page](https://link.zhihu.com/?target=https%3A//docs.docker.com/engine/install/debian/) to install all you need about docker and docker-compose.  
2\. Use the docker shell script with the following commands (provided by a handsome guy [here](https://link.zhihu.com/?target=https%3A//nickjanetakis.com/blog/install-docker-in-wsl-2-without-docker-desktop)

```
# Install Docker, you can ignore the warning from Docker about using WSL
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add your user to the Docker group (Will take effort after relogin)
sudo usermod -aG docker $USER

# Install Docker Compose v2
sudo apt-get update && sudo apt-get install docker-compose-plugin

# Sanity check that both tools were installed successfully
docker --version
docker compose version
```

With any of the ways above, you may found that docker info works now while docker ps -a not. The reason is that you don't set docker service up correctly. Here is the tricky:

```
# Using Ubuntu 22.04 or Debian 10 / 11? You need to do 1 extra step for iptables
# compatibility, you'll want to choose option (1) from the prompt to use iptables-legacy.
sudo update-alternatives --config iptables
```

To make sure the docker service automatically start up every time when you boot linux, add the following scripts to your ~/.profile:

```
if grep -q "microsoft" /proc/version > /dev/null 2>&1; then
    if service docker status 2>&1 | grep -q "is not running"; then
        wsl.exe --distribution "${WSL_DISTRO_NAME}" --user root \
            --exec /usr/sbin/service docker start > /dev/null 2>&1
    fi
fi
```

Last but not least, if you experience a very slow network with docker pull, don't hesitate to use docker registry mirrors by adding something like below to your /etc/docker/daemon.json:

```
{
 "registry-mirrors": [
        "https://registry.docker-cn.com",
        "docker.mirrors.ustc.edu.cn",
        "http://hub-mirror.c.163.com",
        "https://mirror.baidubce.com",
        "ccr.ccs.tencentyun.com",
        "dockerproxy.com",
        "05f073ad3c0010ea0f4bc00b7105ec20.mirror.swr.myhuaweicloud.com",
        "1nj0zren.mirror.aliyuncs.com"
        ]
}
```