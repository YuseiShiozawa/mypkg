import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import random
import time

class SudokuGameSubscriber():
    def __init__(self, node):
        self.publisher = node.create_subscription(Int32MultiArray, 'sudoku_problem', self.callback, 10)
        print("....")

    def callback(self, msg):
        data = msg.data
        answer1 = [1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2]
        answer2 = [4, 1, 3, 2, 3, 2, 4, 1, 2, 3, 1, 4, 1, 4, 2, 3]
        answer3 = [2, 4, 1, 3, 3, 1, 4, 2, 4, 2, 3, 1, 1, 3, 2, 4]
        numbers = []
        print('Received Sudoku Problem:')
        for i in range(4):
            try:
                input_str = input(f"{i+1}行目の数字を入力して: ")
            except:
                input_str = "0 0 0 0"
            number = [int(num) for num in input_str.split()]
            print(number)
            numbers.extend(number)
            
        print()  # 改行
        for k, num in enumerate(numbers, 1):
            print(num, end=" ")
            if k % 4 == 0:
                print()
        print()
        if data[1] == answer1[1]:
            if numbers == answer1:
                print("correct")
            else:
                print("not correct")
        elif data[1] == answer2[1]:
            if numbers == answer2:
                print("correct")
            else:
                print("not correct")
        elif data[1] == answer3[1]:
            if numbers == answer3:
                print("correct")
            else:
                print("not correct")
        print("Game finish")

def main():
    rclpy.init()
    node = Node('sudoku_ans')
    sudoku_ans = SudokuGameSubscriber(node)
    rclpy.spin_once(node)

if __name__ == '__main__':
    main()

