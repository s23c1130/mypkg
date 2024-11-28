#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 11 ros2 launch mypkg talk_listen.launch.py > $dir/ros2_ws/mypkg.log

cat $dir/ros2_ws/mypkg.log |
grep 'Listen: 10'
