#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

cd src/mypkg/test/
ros2 run mypkg sudoku_ans < 'sudoku.txt' &
ros2 run mypkg sudoku_problem > log.txt
#> /tmp/mypkg.log
#ros2 run mypkg sudoku_ans < 'sudoku.txt' > /tmp/mypkg.log
#> /tmp/mypkg.log
#cat /tmp/mypkg.log |
#grep 'Listen: 10'
#cat /tmp/mypkg.log | grep "...."
#cat /tmp/mypkg.log
#cd $dir/ros2_ws
cat log.txt | grep "no"
##cat /tmp/mypkg.log | grep "0"
#cat /tmp/mypkg.log | grep "no"

