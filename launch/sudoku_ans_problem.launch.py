#SPDX-FileCopyrightText: 2023 Yusei Shiozawa
#SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    sudoku_ans = launch_ros.actions.Node(
            package='mypkg',
            executable='sudoku_ans',
            output='screen'
            )
    sudoku_problem = launch_ros.actions.Node(
            package='mypkg',
            executable='sudoku_problem',
            output='screen'
            )

    return launch.LaunchDescription([sudoku_ans, sudoku_problem])
