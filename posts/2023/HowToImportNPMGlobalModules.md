Sometimes you may npm install certain modules globally.

In that case, these modules may not be imported into your node projects as they don't know where you placed the system places the global modules for you.

So, please add ENV for your dockers. Yes dockers, as the problem often occurs in docker containers.

```
ENV NODE_PATH=/usr/local/lib/node_modules
```

Meanwhile, if you get ssl certificate error when npm install, you can try to run the following command.

```
npm config set strict-ssl false
```

Fianally, if you experience that the download speed is real slow in china mainland, you can try to switch your registry with the following command

```
npm config set registry http://r.cnpmjs.org/
```