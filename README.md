Githelper: a simple Python script to shorten Git operations even better than
bash aliases can.

Rather than `git add -A`, do `g a`! Did you also want to `git commit` and then
`git push`? Do `g acp`! Mix and match the letters until you get the operations
you want, and they will be run in order.

Also yells at you if you accidentally try to force push to the master branch
using the `f` option.

You can also add args to the end of the command as long as you're only doing
one operation, e.g. `g p --force`.

Also runs the included `git-branch-tracker` script when you push a new branch
to set that branch as your new upstream (to make `git pull` work).

Aliases:
```
a: git add -A
c: git commit -v
s: git stash --include-untracked
r: git fetch && git rebase remotes/origin/`git rev-parse --abbrev-ref HEAD`
p: git push
f: git push --force-with-lease
t: git push --tags
```

To use, clone this repo:
```
cd
git clone git@github.com:rettigs/githelper.git
git config --global push.default current # Recommended, but be careful about pushing without this
```
Then put this in your `~/.bashrc`: (if you're using bash)
```
alias g='~/githelper/githelper.py'
```
