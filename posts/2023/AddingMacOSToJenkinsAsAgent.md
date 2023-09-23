Some company policies don't allow enable remote login in MacOS system preference, in order to add your macbook as a jenkins agent, you can follow the steps below.

1.enable ssh with the following command

```
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
sudo systemsetup -setremotelogin on (not required)
```

2.set the Remote root directory (agent configuration) as your user root directory, e.g. /Users/bma rather than others，unless there will be errors like "An unexpected error occurred while trying to open file remoting.jar"

3\. sometimes, if you want someone to access a certain http-server with your local IP, you should make sure the sharing permission get opened

```
sudo launchctl load /System/Library/LaunchDaemons/com.apple.NetworkSharing.plist
```