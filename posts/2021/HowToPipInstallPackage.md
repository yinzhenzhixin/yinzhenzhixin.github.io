Python Pip normally provides two ways to install any packages from pypi, online mode and offline mode. For our mypackage package, we can leverage both of them as below.

**Online Mode**

Mypackage is a private package, which means we only maintain it internally. If you'd like to install it with the approach as you install any other public packages, \*e.g. pip install selenium\*

It will not works for mypackage. Because our mypackage does not in the default pip server ([pypi.org](https://link.zhihu.com/?target=http%3A//pypi.org/)). We say "our mypackage" here since there are other packages named "mypackage" from [pypi.org](https://link.zhihu.com/?target=http%3A//pypi.org/), but that is not what you want.

Fortunately, you can add an index url with the following command, which means you will let pip to index packages from the given server as priority (if any, pip will index the packages from the default server)

```
pip config set global.index-url http://internal-server:27149/simple/
```

wl000731481 is an internal server near us. Please ping this domain name beforehand, so that you are sure you can use the domain as the host name directly as above. Otherwise, you should use the ip address behind this domain name Instead.

One more thing, since pip requires trusted hosts as the package servers. However, normally we can't add certificates for internal servers, which means they will not be considered as trusted hosts.

Fortunately, there is a workaround. We can use the following command to explicitly let pip include a given host as a trusted one.

```
pip config set global.trusted-host <IP or DOMAIN>:<PORT>
```

That's it! We will continuously deploy the latest mypackage packages to the server above, which means you can just type the following command as usual to install the latest mypackage.

Or, you can upgrade it as below.

Moreover, you can also specify a version which you want below.

```
pip install mypackage==1.0.0
```

**Offline Mode**

Well, in case sometimes the approach above not work for you, as a workaround, you can download the mypackage whl from somewhere, and install it offline. Normally, we have sync the latest version of mypackage to the resource/pip folder in the project. Therefore, you can install it as below.

```
pip install ./resource/pip/mypackage-****.whl
```