#!/usr/bin/zsh
while inotifywait -q -r -e modify ./rocket/ ./tests/ --exclude .swp
do 
    clear && python $1 down 100
done
