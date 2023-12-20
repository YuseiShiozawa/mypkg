# mypkg
[![test](https://github.com/YuseiShiozawa/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/YuseiShiozawa/mypkg/actions/workflows/test.yml) [![test](https://github.com/YuseiShiozawa/mypkg/actions/workflows/sudoku_test.yml/badge.svg)](https://github.com/YuseiShiozawa/mypkg/actions/workflows/sudoku_test.yml)

ROS 2 のパッケージ

## リポジトリ内のノード,ファイル一覧

### talker.py
* パブリッシャを持つノード. 数字をカウントしてトピック`/countup`を通じて送信する.
   * トピックに流れるメッセージの型は16ビットの符号付き整数.
  
### listener.py
* サブスクライバを持つノード. トピック`/countup`からメッセージを受け取り表示する

### talk_listen.launch.py
* talker.pyとlistener.pyを一度に立ち上げる.

### sudoku_problem.py
* パブリッシャを持つノード. 数独の問題をトピック`/sudoku_problem`を通じて送信する.
   * トピックに流れるメッセージの型は32ビットの符号付き整数の配列.

### sudoku_ans.py
* サブスクライバを持つノード. トピック`/sudoku_problem`から数独の問題を受け取り,解答者(あなた)がターミナルの標準入力から解答を入力することで,その正誤判定を行う.

## 実行手順
### talkerとlistener
* `ros2 run`で実行する方法
```bash
端末1$ ros2 run mypkg talker
端末2$ ros2 run mypkg listener
[INFO] [1701248203.389102109] [listener]: Listen: 0
[INFO] [1701248203.871938229] [listener]: Listen: 1
[INFO] [1701248204.372729350] [listener]: Listen: 2
[INFO] [1701248204.872113956] [listener]: Listen: 3
[INFO] [1701248205.373301079] [listener]: Listen: 4
[INFO] [1701248205.872914002] [listener]: Listen: 5
                         .
                         .
                         .
```
実行後,上記のように出力される. 終了するときは`Ctrl+C`

* `ros2 launch`で実行する方法
```bash
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/shiozawa/.ros/log/2023-11-30-03-00-30-886468-shiopc-14400
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [14402]
[INFO] [listener-2]: process started with pid [14404]
[listener-2] [INFO] [1701280831.771362748] [listener]: Listen: 0
[listener-2] [INFO] [1701280832.253171938] [listener]: Listen: 1
[listener-2] [INFO] [1701280832.753223990] [listener]: Listen: 2
[listener-2] [INFO] [1701280833.252446603] [listener]: Listen: 3
[listener-2] [INFO] [1701280833.752907282] [listener]: Listen: 4
[listener-2] [INFO] [1701280834.253602883] [listener]: Listen: 5
                         .
                         .
                         .
```
実行後,上記のように出力される. 終了するときは`Ctrl+C`

### sudoku_problemとsudoku_ans
ミニ数独(オリジナル):  
4×4のマスに1~4の数字が縦,横,斜めに同じ数字が存在しないように数値を入力する. 0は本来の数独での空白という扱いで,解答者(あなた)が入力する数値である. 問題は全3種.

```bash
端末1$ ros2 run mypkg sudoku_ans
待機中.... 
```
待機中....がターミナルに表示されたら端末2でsudoku_problemを実行する.

```bash
端末2$ ros2 run mypkg sudoku_problem
0 4 0 0
0 0 0 2
0 0 3 0
1 0 0 0
```

端末1に戻るとReceivedが表示され,解答の入力を求められる. 解答時間は1分. 各行の数値を下記のように入力後,解答の正誤が表示される. また,解答時間を過ぎてしまうと答えが表示される.

```bash
Received
1行目の数字を入力して:2 4 1 3
2行目の数字を入力して:3 1 4 2
3行目の数字を入力して:4 2 3 1
4行目の数字を入力して:1 3 2 4

2 4 1 3
3 1 4 2
4 2 3 1
1 3 2 4

Correct
```

## 必要なソフトウェア
* Python

## テスト環境
* Ubuntu 20.04
* ROS2 foxy

## 権利関係

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
   * [ryuichiueda/my_slides/robosys_2022/lesson8](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson9](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson10](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson11](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/)
* © 2023 Yusei Shiozawa
