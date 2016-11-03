#!/usr/bin/env python

# Git command aliaser and combiner
# More effective than permuting aliases!
# For each letter in the word passed as the argument, performs an action (in
# the order specified)

import sys, os

if __name__ == '__main__':
    
    argmap = dict(
        a="git add -A",
        c="git commit -v",
        s="git stash --include-untracked",
        r="git fetch && git rebase remotes/origin/`git rev-parse --abbrev-ref HEAD`",
        p="git push",
        f="git push --force-with-lease",
        t="git push --tags"
    )

    if len(sys.argv) < 2:
        for arg, command in argmap.iteritems():
            print "{}\t{}".format(arg, command)
    else:
        extraargs = ""
        if len(sys.argv) > 2:
            if len(sys.argv[1]) != 1:
                print "##### Cannot apply extra args since we got more than one action; exiting"
                exit()
            else:
                extraargs = " ".join(sys.argv[2:])
        for arg in list(sys.argv[1]):
            if arg == 'f':
                gitbranch = os.popen("git rev-parse --abbrev-ref HEAD 2> /dev/null").read().strip()
                if gitbranch == 'master':
                    print "##### Bad monkey! Don't force push to master!"
                    exit()
            command = "{} {}".format(argmap[arg], extraargs)
            print "##### Running Git command: {}".format(command)
            if os.system(command) != 0:
                print "##### Git command failed: {}".format(command)
                exit()
            # If we did a push, run the branch tracker to make sure we pull from there too
            elif command.find("git push") != -1:
                os.system(os.path.join(sys.path[0], "git-branch-tracker.sh"))
