import rclpy
from rclpy.node import Node
from sudoku_msgs.msg import SudokuProblem, SudokuSolution

class SudokuGameSubscriber(Node):
    def __init__(self):
        super().__init__('sudoku_game_subscriber')
        self.subscription = self.create_subscription(SudokuProblem, 'sudoku_problem', self.callback, 10)
        self.publisher = self.create_publisher(SudokuSolution, 'sudoku_solution', 10)

    def callback(self, msg):
        sudoku_problem = msg.problem
        self.get_logger().info('Received Sudoku Problem:')
        self.print_sudoku(sudoku_problem)
        self.solve_and_publish_solution(sudoku_problem)

    def solve_and_publish_solution(self, sudoku_problem):
        solution = [[3, 1, 4, 2], [4, 2, 1, 3], [2, 3, 0, 1], [1, 4, 3, 0]]
        
        sudoku_solution_msg = SudokuSolution(solution=solution)
        self.publisher.publish(sudoku_solution_msg)
        self.get_logger().info('Published Sudoku Solution:')
        self.print_sudoku(solution)

    def print_sudoku(self, sudoku):
        for row in sudoku:
            self.get_logger().info(row)

def main(args=None):
    rclpy.init(args=args)
    subscriber_node = SudokuGameSubscriber()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

