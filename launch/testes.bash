#!/bin/bash
gnome-terminal -- bash -c "ros2 run mypkg sudoku_ans; echo a; read -n1"
gnome-terminal -- bash -c "ros2 run mypkg sudoku_problem; echo a; read -n1"
