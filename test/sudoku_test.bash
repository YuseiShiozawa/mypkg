#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

ros2 run mypkg sudoku_ans
ros2 run mypkg sudoku_problem > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '....'
