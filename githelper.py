#!/usr/bin/env python

# Git command aliaser and combiner
# More effective than permuting aliases!
# For each letter in the word passed as the argument, performs an action (in
# the order specified)
#
# Also supports git arguments, but if multiple actions are sepcified, the
# arguments are only passed to the last action.

import sys, os

if __name__ == '__main__':
    
    argmap = dict(
        a="git add -A",
        c="git commit -v",
        s="git stash --include-untracked",
        r="git fetch && git rebase remotes/origin/`git rev-parse --abbrev-ref HEAD`",
        m="ORIGINAL_BRANCH=`git rev-parse --abbrev-ref HEAD`; git checkout ${GIT_MASTER_BRANCH_NAME:=master} && git pull && git checkout $ORIGINAL_BRANCH && git rebase ${GIT_MASTER_BRANCH_NAME} && git checkout ${GIT_MASTER_BRANCH_NAME} && git merge $ORIGINAL_BRANCH",
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
            extraargs = " ".join(sys.argv[2:])
        for i, arg in enumerate(list(sys.argv[1])):

            # Block force pushing to master; make them type the command out manually instead
            if arg == 'f':
                gitbranch = os.popen("git rev-parse --abbrev-ref HEAD 2> /dev/null").read().strip()
                if gitbranch == 'master':
                    print "##### Don't force push to master!"
                    exit()

            command = argmap[arg]

            # If this is the last action, add the extra args
            if i == len(sys.argv[1]) - 1:
                command += " {}".format(extraargs)

            # Run the command
            print "##### Running Git command: {}".format(command)
            if os.system(command) != 0:
                print "##### Git command failed: {}".format(command)
                exit()

            # If we did a push, run the branch tracker to make sure we pull from there too
            if command.find("git push") != -1:
                os.system(os.path.join(sys.path[0], "git-branch-tracker.sh"))
