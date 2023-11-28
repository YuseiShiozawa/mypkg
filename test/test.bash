#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc
echo -e "0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n" > 'sudoku1.txt'
#cd src/mypkg/test/
timeout 10 ros2 run mypkg sudoku_ans < 'sudoku1.txt' & 
ros2 run mypkg sudoku_problem > /tmp/mypkg.log
#& cd $dir/ros2_ws & 
#ros2 run mypkg sudoku_problem > /tmp/mypkg.log
#ros2 run mypkg sudoku_ans < 'sudoku.txt' > /tmp/mypkg.log
#> /tmp/mypkg.log
#cat /tmp/mypkg.log |
#grep 'Listen: 10'
#cat /tmp/mypkg.log | grep "...."
#cat /tmp/mypkg.log
#cd $dir/ros2_ws
##cat /tmp/mypkg.log | grep "0"
cat /tmp/mypkg.log | grep "0"
#cat /tmp/mypkg.log | grep "no"

