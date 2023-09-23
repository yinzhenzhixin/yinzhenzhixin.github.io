After set up WSL2 on my new laptop, I found that apt update doesn't work with WSL2 but works with WSL1. With some investigation, finally I found that it has something to do with the resolv.conf file, which includes the DNS for linux-like systems.

You have to add your DNS items correctly to the file, like 8.8.8.8 and 8.8.4.4 for google DNS

```
sudo nano /etc/resolv.conf
```

Actually this is just a temporary solution as this file was automatically changed after reboot or network changes. To make it work all the time, you have to install resolconf to set up it.

```
apt install -y resolvconf 
```

One more thing, if you'd like to install docker engine instead of docker desktop in your linux system, sometimes you may encounter the issue "failed to start daemon: Error initializing network controller" when start docker service, then you can try to perform the following commands to make it worked

```
touch /etc/fstab
sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
```