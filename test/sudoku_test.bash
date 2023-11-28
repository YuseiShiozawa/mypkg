#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc
cd src/mypkg/test/
ros2 run mypkg sudoku_ans < 'sudoku_ans.txt' &
ros2 run mypkg sudoku_problem > /tmp/mypkg.log

cat /tmp/mypkg.log | 
grep 'Received'

