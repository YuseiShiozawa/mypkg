#SPDX-FileCopyrightText: 2023 Yusei Shiozawa
#SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
#from sudoku_msgs.msg import Problem
import random
import time
import threading
import sys

class SudokuSub():
    def __init__(self, node):
        self.publisher = node.create_subscription(Int32MultiArray, 'sudoku_problem', self.callback, 10)
        print("Waiting....")

    def callback(self, msg):
        data = msg.data
        flag = 0
        answer1 = [1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2]
        answer2 = [4, 1, 3, 2, 3, 2, 4, 1, 2, 3, 1, 4, 1, 4, 2, 3]
        answer3 = [2, 4, 1, 3, 3, 1, 4, 2, 4, 2, 3, 1, 1, 3, 2, 4]
        numbers = []
        print("Received")
        for i in range(4):
            wait = threading.Thread(target=lambda:
            setattr(threading.current_thread(), 'answers',input(f"{i+1}行目の数字を入力:")))
            wait.start()
            wait.join(timeout=5)
            if wait.is_alive():
                if data[1] == answer1[1]:
                    if i == 0:
                        setattr(wait, 'answers', "1 2 3 4")
                    if i == 1:
                        setattr(wait, 'answers', "4 3 2 1")
                    if i == 2:
                        setattr(wait, 'answers', "2 1 4 3")
                    if i == 3:
                        setattr(wait, 'answers', "3 4 1 2")
                elif data[1] == answer2[1]:
                    if i == 0:
                        setattr(wait, 'answers', "4 1 3 2")
                    if i == 1:
                        setattr(wait, 'answers', "3 2 4 1")
                    if i == 2:
                        setattr(wait, 'answers', "2 3 1 4")
                    if i == 3:
                        setattr(wait, 'answers', "1 4 2 3")
                elif data[1] == answer3[1]:
                    if i == 0:
                        setattr(wait, 'answers', "2 4 1 3")
                    if i == 1:
                        setattr(wait, 'answers', "3 1 4 2")
                    if i == 2:
                        setattr(wait, 'answers', "4 2 3 1")
                    if i == 3:
                        setattr(wait, 'answers', "1 3 2 4")
                #flag = 1
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

def main():
    #global flag
    #flag = 5
    rclpy.init()
    node = Node('sudoku_ans')
    sudoku_ans = SudokuSub(node)
    rclpy.spin_once(node)

if __name__ == '__main__':
    main()
