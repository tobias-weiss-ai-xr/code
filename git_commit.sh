#!/bin/bash
find ./cpp -type f -exec sh -c "file {}" \; | grep "LSB executable" | awk -F: '{print $1}' |xargs rm -f
git pull
git add -A
git commit -m "autocommit"
git push
