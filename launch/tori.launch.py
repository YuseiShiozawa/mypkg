from launch import LaunchDescription
from launch_ros.actions import Node

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
