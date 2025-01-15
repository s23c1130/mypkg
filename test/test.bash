#!/bin/bash -xv

# SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

res=0

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

sudo apt -y update
sudo apt -y install xdotool
sudo apt -y install xvfb
sudo apt -y install pip
sudo apt -y install lm-sensors
pip install pyautogui
pip install python-xlib

Xvfb -ac :99 -screen 0 1280x1024x24 &
export DISPLAY=:99

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source install/setup.bash && source install/local_setup.bash
install/mypkg/lib/mypkg/MousePointPub &
timeout 3 install/mypkg/lib/mypkg/listener &> /tmp/mypkg.log

x=`xdotool getmouselocation | awk '{print substr($1, 3)}'`
y=`xdotool getmouselocation | awk '{print substr($2, 3)}'`

x_check="x:${x}"
y_check="y:${y}"

cat /tmp/mypkg.log

grep "${x_check}" /tmp/mypkg.log

if [ $? = 0 ]; then
    echo X_POS OK
else
    echo X_POS NG
    res=1
fi

grep "${y_check}" /tmp/mypkg.log

if [ $? = 0 ]; then
    echo Y_POS OK
else
    echo Y_POS NG
    res=1
fi


vmstat

exit $res
