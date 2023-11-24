import rclpy
from rclpy.node import Node
from sudoku_msgs.msg import Problem
import random

class SudokuPub():
    def __init__(self, node):
        self.publisher = node.create_publisher(Problem, 'sudoku_problem', 10)
        node.create_timer(3, self.publish_sudoku_problem)

    def publish_sudoku_problem(self):
        problems = [
            [0, 2, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2],
            #[0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0],
            #[0, 4, 0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 1, 0, 0, 0]
        ]
        
        selected_problem = random.choice(problems)
        sudoku_problem_msg = Problem(problem=selected_problem)
        self.publisher.publish(sudoku_problem_msg)
        for i, num in enumerate(selected_problem, 1):
            print(num, end=' ')
            if i % 4 == 0:
                print()
        msg = Problem()
        msg.problem = selected_problem
        self.publisher.publish(msg)

def main():
        rclpy.init()
        node = Node('sudoku_problem')
        sudoku_problem = SudokuPub(node)
        rclpy.spin_once(node)


if __name__ == '__main__':
    main()
