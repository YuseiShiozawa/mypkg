import rclpy
from rclpy.node import Node
from sudoku_msgs.msg import Problem
import random
import time

class SudokuSub():
    def __init__(self, node):
        self.publisher = node.create_subscription(Problem, 'sudoku_problem', self.callback, 10)
        print("....")

    def callback(self, msg):
        data = msg.problem
        answer1 = [1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2]
        answer2 = [4, 1, 3, 2, 3, 2, 4, 1, 2, 3, 1, 4, 1, 4, 2, 3]
        answer3 = [2, 4, 1, 3, 3, 1, 4, 2, 4, 2, 3, 1, 1, 3, 2, 4]
        numbers = []
        #print("問題を受け取りました:")
        for i in range(4):
            answers = input(f"{i+1}行目の数字を入力:")
            number = [int(num) for num in answers.split()]
            #print(number)
            numbers.extend(number)

        print()
        for k, num in enumerate(numbers, 1):
            print(num, end=" ")
            if k % 4 == 0:
                print()
            print()
    
        if data[1] == answer1[1]:
            if numbers == answer1:
                print("Correct")
            else:
                print("Miss")
        elif data[1] == answer2[1]:
            if numbers == answer2:
                print("Correct")
            else:
                print("Miss")    
        elif data[1] == answer3[1]:
            if numbers == answer3:
                print("Correct")
            else:
                print("Miss")
def main():
    rclpy.init()
    node = Node('sudoku_ans')
    sudoku_ans = SudokuSub(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
