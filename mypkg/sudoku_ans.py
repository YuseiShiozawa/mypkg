#SPDX-FileCopyrightText: 2023 Yusei Shiozawa
#SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
#from sudoku_msgs.msg import Problem
import random
import time
import threading

class SudokuSub():
    def __init__(self, node):
        self.publisher = node.create_subscription(Int32MultiArray, 'sudoku_problem', self.callback, 10)
        print("Waiting....")

    def callback(self, msg):
        data = msg.data
        answer1 = [1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2]
        answer2 = [4, 1, 3, 2, 3, 2, 4, 1, 2, 3, 1, 4, 1, 4, 2, 3]
        answer3 = [2, 4, 1, 3, 3, 1, 4, 2, 4, 2, 3, 1, 1, 3, 2, 4]
        numbers = []
        print("Received")
        for i in range(4):
            wait = threading.Thread(target=lambda:
            setattr(threading.current_thread(), 'answers',input(f"{i+1}行目の数字を入力:")))
            wait.start()
            wait.join(timeout=60)
            if wait.is_alive():
                setattr(wait, 'answers', "0 0 0 0")
            answers = getattr(wait, 'answers')
            #answers = input(f"{i+1}行目の数字を入力:")
            #except:
                #answers = "0 0 0 0"
            number = [int(num) for num in answers.split()]
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
        #print()
        #print("待機中....")

def main():
    #global flag
    #flag = 5
    rclpy.init()
    node = Node('sudoku_ans')
    sudoku_ans = SudokuSub(node)
    rclpy.spin_once(node)

if __name__ == '__main__':
    main()
