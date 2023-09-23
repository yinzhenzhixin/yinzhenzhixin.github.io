近两周熬了两次夜,一次3点半,一次一点半,为啥呢?

要从7年前买的SONY 14A26CCW说起,这笔记本跑ubuntu14.04本是刚刚的,无奈现在ubuntu20.04都出了,早已放弃对14.04的支持.对我的影响呢,就是python3官方预装版本只有3.4,进而呢,想用pip3安装jupyterlab,系统总是报错,要求python版本必须大于3.5

升级python3的思路倒是有的,网上无非有两种玩儿法.

1.通过官方apt安装,前提是添加相关的源(可悲墙内羞涩,更新时总是超时断开):

```
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev
sudo apt-get install python3-pip python3.7-dev
sudo apt-get install python3.7
```

2\. 通过编译python源码安装(此法更亏,虽然可以安装成功,但是后期你会慢慢发现很多系统软件受影响):

```
sudo apt-get install make build-essential zlib1g-dev libffi-dev libssl-dev libsqlite3-dev libbz2-dev libgdm-dev libdb4o-cil-dev libpcap-dev libreadline-dev libncurses5-dev libtk8.5
sudo tar -xf Python-3.7.0.tar.xz
cd Python-3.7.0
./configure --with-openssl=/home/yinzhenzhixin/openssl -prefix=/home/username/python-3.7.0
sudo make
sudo make install
```

这两个熬夜,主要都献给了第二种方法,先后编译安装3.7和3.8的python近10次,由此导致的系统软件不可用,进而还原Ubuntu近10次,尴尬万分.

如果要根治这个问题,最好的方法就是将ubuntu升级到18.04之后,这样系统自带了3.6以后的python,省得麻烦；然则,上面说了,7年前的本子,显卡比较老,新版本的ubuntu驱动不支持,导致屏幕亮度无法调节,无法睡眠等问题,也很尴尬.

不管怎么说,两个熬夜也不算白费,期间学习了很多,比如针对ubuntu14.04自带的python和python3,可以分别安装如下两款python虚拟机,用于在虚拟环境开发,避免干扰系统,不用的时候虚拟环境很容易就能清除:

```
sudo apt-get install python-virtualenv
virtualenv mypyvenv

sudo apt-get install python3.4-venv
pyvenv-3.4 mypy3venv

source mypyvenv/bin/activate
deactivate
```

还有更新pip的各种方法:

```
pip install --upgrade pip
pip install -U pip
easy_install -U pip
```

以及修改python和pip软链接,以使自己编译安装的python3替换掉系统预装的python3:

```
rm -rf /usr/bin/python3
rm -rf /usr/bin/pip3
ln -s /usr/local/bin/python3.7 /usr/bin/python3
ln -s /usr/local/bin/pip3.7 /usr/bin/pip3
```

尽管似乎白白耗费了两个熬夜,不过起码我把这些才过的坑写下来,以后自己遇到类似的坑也能跨过去,或者别人也能从中借鉴,人生,其实和troubleshooting有时候是一样一样的.