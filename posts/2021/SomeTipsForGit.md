### Git Config

```
# Show all paths of local git configuration files
git config --list --show-origin --show-scope

# Disable popup credential manager
git config --global remove helper = manager
git config --global add askpass = false
git config credential.modalprompt false --global
```

### Multiple Remote

```
# Multiple remote set
# Add second remote url
git init
git add .
git ci -m 'Initial submit'
git remote add all REMOTE-URL-1
git remote set-url --add --push all REMOTE-URL-1
git remote set-url --add --push all REMOTE-URL-2
git push all {BRANCH_NAME}
git fetch --all
git pull <remote> <branch>
git branch --set-upstream-to=origin/<branch> master
```

### Git Tags

```
# Add tag on specific commit
git tag -a <tag_name> <commit_id> -m "<message>"

# Change the commit point for specific tag
git tag -f <tag_name> <new_commit_id>

# Show tags with messages
git tag -n5

# Show commit id for given tag
git rev-list -n 1 <tag_name>
```