#!/bin/bash
#SPDX-FileCopyrightText: 2023 Yusei Shiozawa
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc
timeout 245 ros2 launch mypkg sudoku_ans_problem.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log | 
grep "Correct"

