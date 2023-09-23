### Bash Command in PowerShell

Since PS (PowerShell) supports bash. Actually you can use a lot of Unix commands like below.

> bash -c ‘nano notes.txt’

### Use Function in Powershell

May you want use ‘nano command’ as linux style. In fact, we can leverage the powershell function to do so. Just add the following codes in powershell line by line

function nano($File){ $File = $File -replace "\\\\", "/" -replace " ", "\\ " bash -c "nano $File" }

Note that the code ‘-replace’ here is just to format the path symbols, you can ignore it if not required. After that, you can use nano as a command in the current session of your PS.

> nano notes.txt

### Let the Function Works Regularly

As I said earlier, for now the function only works in the current session of your PS. It means that the funcion will not be available once you close the PS window and open a new one. Because it’s not been set up in the PS user profile. To do so, you have to create the user profile as below.

> New-Item -Path $profile -ItemType File -Force

There will be an empty user profile file create into the following path: _C:\\Users\\YOURUSERNAME\\Documents\\WindowsPowerShell\\Microsoft.PowerShell\_profile.ps1_

Now you can add the function body above into the profile file.  
That’s it! Now close the current PS and open a new one, you will find that now the nano command works for you regularly