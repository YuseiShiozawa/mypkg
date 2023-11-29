#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc
#cd src/mypkg/test/
#ros2 run mypkg sudoku_ans &
#ros2 run mypkg sudoku_problem > /tmp/mypkg.log
timeout 10 ros2 launch mypkg sudoku_ans_problem.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | 
grep "Received"

