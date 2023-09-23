### Ruby Version

Since there are plenty of modules will be installed with bundler in our automation framework, and some of them require a lower version of ruby rather the the latest one. Therefore, please make sure you install ruby 2.7 below. Alternately, you can install RVM, which is a ruby version manager tool, so that you can switch the ruby version easily. There are some documents as references below.

[How to use RVM](https://link.zhihu.com/?target=https%3A//github.com/rvm/rvm)  
[How to install RVM on Windows](https://link.zhihu.com/?target=https%3A//www.drupal.org/node/2138087)

### Ruby Vault

Vault is a Ruby API client for interacting with a Vault server. Sometimes there is no vault install requirement in the Gemfile. If so, please install it manually.

> gem install vault

And then, add the line into your Gemfile.

> gem “vault”, “0.15.0”

Moreover, please make sure to use the correct vault address in the Gemfile below.

> Vault.address = “[http://10.229.15.62:8200](https://link.zhihu.com/?target=http%3A//10.229.15.62%3A8200/)“

### EventMachine Module missing on Old Ruby Version

If your ruby is lower than 2.6, you may come across the error “Unable to load the EventMachine C extension; To use the pure-ruby reactor, require ‘em/pure\_ruby’” when running automation tests. You can manually install the module for your ruby below.

gem uninstall eventmachine gem install eventmachine --platform ruby

### Debug Ruby Automation Tests with VS Code

Thare are at least two ways to debug automation tests. The first one is the crazy mode, you can just run the main.rb with a certain command line tool, such as powershell below, and print the specified variables concerned within your codes

cd test/admin\_portal ruby main.rb -s search\_location/ -b chrome -e QA

Okay, that’s tough! Good news is that you can use VS Code with a debug configuration file named “launch.json”.

In order to let VS Code work together with ruby, please make sure that you have installed the following modules with gem, the version of those modules should be pair with your ruby

gem "ruby-debug-ide", "0.7.0" # Debug on VS Code gem "debase", "0.2.4" # Debug on VS Code

You can create the file manually, or just click on the button on the debug tab of VS Code. For our automation tests, make sure you have the following content in the file.

```
 { // Use IntelliSense to learn about possible attributes. // Hover to view descriptions of existing attributes. // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387 "version": "0.2.0", "configurations": [ { "name": "Debug Local File", "type": "Ruby", "request": "launch", "cwd": "${workspaceRoot}/test", "program": "${workspaceRoot}/test/main.rb", "useBundler": true, "pathToRDebugIDE": "C:\\Ruby25-x64\bin\\rdebug-ide", "pathToBundler": "C:\\Ruby25-x64\\bin\\bundle.bat", "args": [ "-s", "regression/demo_test", "-b", "chrome", "-e", "QA", // "-d" ] }, { "name": "Listen for rdebug-ide", "type": "Ruby", "request": "attach", "cwd": "${workspaceRoot}", "remoteHost": "127.0.0.1", "remotePort": "1234", "remoteWorkspaceRoot": "${workspaceRoot}" }, { "name": "Rails server", "type": "Ruby", "request": "launch", "cwd": "${workspaceRoot}", "program": "${workspaceRoot}/bin/rails", "args": [ "server" ] }, { "name": "RSpec - all", "type": "Ruby", "request": "launch", "cwd": "${workspaceRoot}", "program": "${workspaceRoot}/bin/rspec", "args": [ "-I", "${workspaceRoot}" ] }, { "name": "RSpec - active spec file only", "type": "Ruby", "request": "launch", "cwd": "${workspaceRoot}", "program": "${workspaceRoot}/bin/rspec", "args": [ "-I", "${workspaceRoot}", "${file}" ] }, { "name": "Cucumber", "type": "Ruby", "request": "launch", "cwd": "${workspaceRoot}", "program": "${workspaceRoot}/bin/cucumber" } ] }
```