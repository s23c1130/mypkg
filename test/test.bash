#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

sudo apt -y install xdotool
cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

x=`xdotool getmouselocation | awk '{print substr($1, 3)}'`
y=`xdotool getmouselocation | awk '{print substr($2, 3)}'`

x_y="x:${x} y:${y}"

grep "${x_y}" /tmp/mypkg.log

if [ $? = 0 ]; then
    echo OK
    exit 0
else
    echo NG
    exit 1
fi