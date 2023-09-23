Refer to [https://itlanyan.com/xray-tutorial/](https://link.zhihu.com/?target=https%3A//itlanyan.com/xray-tutorial/) if you need more.

### Setup VPN

1.  Request an AWS or Azure VPN
2.  Enable the required ports, like 80, 443, etc. in the security groups
3.  Register a free domain (e.g. [https://www.freenom.com](https://link.zhihu.com/?target=https%3A//www.freenom.com))

### Install certificates

1.  SSH to the VPN
2.  Install acme

```
curl https://get.acme.sh | sh -s email=somebody@gmail.com
```

3\. Let acme upgraded automatically

```
~/.acme.sh/acme.sh  --upgrade  --auto-upgrade
```

4\. Install socat so that you can use acme standalone mode apt install socat  
5\. Issue a certificate ~/.acme.sh/acme.sh --issue -d \[domain.name\] --standalone  
6\. Install the certificate to a custom path

```
~/.acme.sh/acme.sh --install-cert -d [domain.name] \
--cert-file  /path/to/your/cert.pem  \
--key-file  /path/to/your/key.pem  \
--fullchain-file /path/to/your/fullchain.pem  \
--reloadcmd     "service nginx force-reload" (not required)
```

### Setup Xray

1.  Install Xray

```
bash <(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh) install
```

2\. After that, the executable file will be in /usr/local/bin while the config file will be in /usr/local/etc/xray

3\. Use the following config template

```
{
    "log": {
        "loglevel": "info"
    },
    "inbounds": [
        {
            "port": 443,
            "protocol": "vless",
            "settings": {
                "clients": [
                    {
                        "id": "", // use 'xray uuid' to generate UUIDs
                        "flow": "xtls-rprx-direct",
                        "level": 0
                    }
                ],
                "decryption": "none",
                "fallbacks": [
                    {
                        "dest": 80 // something like "www.baidu.com:80"
                    }
                ]
            },
            "streamSettings": {
                "network": "tcp",
                "security": "xtls",
                "xtlsSettings": {
                    "alpn": [
                        "http/1.1"
                    ],
                    "certificates": [
                        {
                            "certificateFile": "/path/to/fullchain.crt", // use the custom cert file path
                            "keyFile": "/path/to/private.key" // use the custom key file path
                        }
                    ]
                }
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "freedom"
        }
    ]
}
```

### Setup Client

1.  Install xray client from [https://github.com/XTLS/Xray-core/releases/tag/v1.5.5](https://link.zhihu.com/?target=https%3A//github.com/XTLS/Xray-core/releases/tag/v1.5.5)
2.  Create config.json under a custom path

```
{
    "log": {
        "loglevel": "warning"
    },
    "inbounds": [
        {
            "port": 1080,
            "listen": "127.0.0.1",
            "protocol": "socks",
            "settings": {
                "udp": true
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "vless",
            "settings": {
                "vnext": [
                    {
                        "address": "[YOUR HOSTNAME]",
                        "port": 443,
                        "users": [
                            {
                                "id": "[YOUR UUID]",
                                "flow": "xtls-rprx-direct",
                                "encryption": "none",
                                "level": 0
                            }
                        ]
                    }
                ]
            },
            "streamSettings": {
                "network": "tcp",
                "security": "xtls", 
                "xtlsSettings": {
                    "serverName": "[YOUR HOSTNAME]"
                }
            }
        }
    ]
}
```

3\. Run Xray client in the command line xray run -c \[config\_file\_path\]