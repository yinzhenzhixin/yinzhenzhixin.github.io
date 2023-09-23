### Alpine

```
sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
```

### Pip

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```