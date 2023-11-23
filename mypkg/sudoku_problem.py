import rclpy
from rclpy.node import Node
from sudoku_msgs.msg import SudokuProblem

class SudokuPublisher(Node):
    def __init__(self):
        super().__init__('sudoku_game_publisher')
        self.publisher = self.create_publisher(SudokuProblem, 'sudoku_problem', 10)
        self.publish_sudoku_problem()

    def PublishProblem(self):
        problems = [
                [[0, 3, 0, 0], [0, 0, 2, 0], [0, 1, 0, 4], [4, 0, 0, 0]],
                [[2, 0, 0, 0], [0, 0, 3, 0], [0, 4, 0, 2], [0, 0, 0, 1]]
                ]

        select = random.choice(problems)
        sudokumsg = SudokuProblem(problem=selected_problem)
        self.publisher.publish(sudokumsg)
        self.get_logger().info('mondai!!!')

    def main(args=None):
        rclpy.init(args=args)
        publisher_node = SudokuGamePublisher()
        rclpy.spin(publisher_node)
        publisher_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
