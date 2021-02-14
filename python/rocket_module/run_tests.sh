#!/usr/bin/zsh
source /home/homaar/python_envs/rocket_env/bin/activate
while inotifywait -q -r -e modify ./rocket/ ./tests/ --exclude .swp
do 
    clear && which python && date && py.test -m default -m default
done
