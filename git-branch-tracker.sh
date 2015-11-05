#!/bin/bash

# Sets a local branch's upstream to origin/<branchname> if it doesn't have one
# already.  Meant to be run after a push, but will likely do nothing after a
# branch's first push since the upstream should then be set.  Since it doesn't
# overwrite existing upstreams, it can be used after every push on every repo.

BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Set branch tracking if we don't already have an upstream
if [ ! $(git rev-parse --abbrev-ref "$BRANCH"@{upstream} 2> /dev/null) ]; then
    git branch --set-upstream-to=origin/$BRANCH $BRANCH
fi
