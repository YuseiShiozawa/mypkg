#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

cd src/mypkg/test/
#echo "read" > "option.txt"
#ls option.txt
#timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
ros2 run mypkg sudoku_ans < 'sudoku.txt' & 
ros2 run mypkg sudoku_problem <'sudoku.txt'> /tmp/mypkg.log
#cat /tmp/mypkg.log |
#grep 'Listen: 10'
cat /tmp/mypkg.log | grep "...."
#cat /tmp/mypkg.log
#cat /tmp/mypkg.log | grep "0"
#cat /tmp/mypkg.log | grep '0'

