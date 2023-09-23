### Aliyun update source

```
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```

### Backup and Recovery

```
sudo tar cvpjf /media/ubuntu/Other/Backup/System/ubuntu_backup_20200301.tar.bz2 --exclude=./proc --exclude=./lost+found --exclude=./mnt --exclude=./sys --exclude=./ssd --exclude=./media ./
sudo mkdir proc lost+found mnt sys media
```

### Uninstall unuseful softwares

```
sudo apt-get remove libreoffice-common 
sudo apt-get remove unity-webapps-common 
sudo apt-get remove totem firefox thunderbird empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines cheese transmission-common gnome-orca webbrowser-app gnome-sudoku  landscape-client-ui-install 
sudo apt-get remove onboard deja-dup
```

### Install useful softwares

```
sudo apt-get install guake kazam stardict pinta SMPlayer
```

### Install Chinese input method

```
sudo apt-get install im-config fcitx fcitx-config-gtk fcitx-table-all
```

### Clear system

```
sudo apt-get autoremove
sudo apt-get autoclean
sudo apt-get clean
```

### Install Chrome

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### Resolve conflicts

```
sudo apt-get update
sudo apt-get -f install
```

### Clear fcitx sogou

```
sudo apt-get remove fcitx-ui-qimpanel
```

### Enable hibernate mode

```
sudo apt-get install laptop-mode-tools
cat /proc/sys/vm/laptop_mode
sudo gedit /etc/laptop-mode/laptop-mode.conf
ENABLE_LAPTOP_MODE_ON_BATTERY=1
ENABLE_LAPTOP_MODE_ON_AC=1
ENABLE_LAPTOP_MODE_WHEN_LID_CLOSED=1
```

### Enable USB devices

```
sudo vi /etc/bluetooth/main.conf
67 -> [Policy]
89 -> AutoEnable=true
sudo mv /lib/udev/rules.d/50-bluetooth-hci-auto-poweron.rules /lib/udev/rules.d/50-bluetooth-hci-auto-poweron.rules.bak
```

### Configure V2Ray

```
sudo bash go.sh --local ./v2ray-linux-64.zip
sudo mv config.json /etc/v2ray/config.json
sudo gedit /etc/v2ray/config.json
jq . /etc/v2ray/config.json
/usr/bin/v2ray/v2ray -test -config /etc/v2ray/config.json
service v2ray status
service v2ray restart
```

### Set auto start

```
sudo cp /usr/share/applications/guake.desktop /etc/xdg/autostart
```

### Import stardict dictionary

```
sudo tar -xjvf stardict-xiandaihanyucidian_fix-2.4.2.tar.bz2 -C /usr/share/stardict/dic/
```

### Projector output

```
xrandr -q
xrandr --output DP1 --output LVDS1 --off
xrandr --output DP1 --primary --left-of LVDS1
```

### ReText configuration

```
sudo apt-get install retext
sudo gedit ~/.config/ReText\ project/ReText.conf
```

> _styleSheet=/home/yinzhenzhixin/.config/ReText project/github.css_  
> _useWebKit=true_