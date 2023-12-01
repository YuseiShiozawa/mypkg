#!/bin/bash
#SPDX-FileCopyrightText: 2023 Yusei Shiozawa
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc
#cd src/mypkg/test/
#timeout 25 ros2 run mypkg sudoku_ans &
#ros2 run mypkg sudoku_problem > /tmp/mypkg.log
timeout 245 ros2 launch mypkg sudoku_ans_problem.launch.py > /tmp/mypkg.log
#245
cat /tmp/mypkg.log | 
grep "Correct"

