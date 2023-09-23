When you use terminal with macos or alpine linux, you may found that all the content are displayed in poor format, default font without colors.

You can add the following scripts into your ~/.bash\_profile or ~/.profile to make it colorful, just like what you can see with ubuntu or debian.

```
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'
alias ll='ls -l'
```

BTW, there are a couple of fonts are recommended for developers below

-   [JetBrains Mono](https://link.zhihu.com/?target=https%3A//github.com/JetBrains/JetBrainsMono)
-   [Inconsolata](https://link.zhihu.com/?target=https%3A//github.com/googlefonts/Inconsolata)
-   [Iosevka](https://link.zhihu.com/?target=https%3A//github.com/be5invis/Iosevka)