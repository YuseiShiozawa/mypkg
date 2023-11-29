# mypkg
[![test](https://github.com/YuseiShiozawa/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/YuseiShiozawa/mypkg/actions/workflows/test.yml) [![test](https://github.com/YuseiShiozawa/mypkg/actions/workflows/sudoku_test.yml/badge.svg)](https://github.com/YuseiShiozawa/mypkg/actions/workflows/sudoku_test.yml)

ロボットシステム学のros練習

#リポジトリ内のノード,ファイル一覧

### talker.py
* パブリッシャを持つノード. 数字をカウントしてトピック`/countup`を通じて送信する.

### listener.py
* サブスクライバを持つノード. `/countup`からメッセージを受け取り表示する

### talk_listen.launch.py
* talker.pyとlistener.pyを一度に立ち上げるファイル.

### sudoku_problem.py
* パブリッシャを持つノード. 数独の問題をトピック``を通じて送信する.

### sudoku_ans.py
* サブスクライバを持つノード. ``から数独の問題を受け取り,解答者(あなた)がターミナルの標準入力から解答を入力し,その正誤判定を行う.

## インストール手順

```bash
$ git clone https://github.com/YuseiShiozawa/mypkg.git
```

## 実行手順
### talkerとlistener
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
実行後,上記のように出力される

### sudoku_problemとsudoku_ans
```bash
端末1$ ros2 run mypkg sudoku_ans
.... 
```
....がターミナルに表示されたら端末2でsudoku_problemを実行する.

```bash
端末2$ ros2 run mypkg sudoku_problem
0 4 0 0
0 0 0 2
0 0 3 0
1 0 0 0
```

端末1に戻るとReceivedが表示されていることが確認でき,解答の入力を求められる

```bash
Received:
1行目の数字を入力して: 2 4 1 3
2行目の数字を入力して: 3 1 4 2
3行目の数字を入力して: 4 2 3 1
4行目の数字を入力して: 1 3 2 4

2 4 1 3
3 1 4 2
4 2 3 1
1 3 2 4

correct
```

## テスト環境
* Ubuntu 20.04

## 権利関係

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
   * [ryuichiueda/my_slides/robosys_2022/lesson8](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson9](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson10](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson11](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/)
* © 2023 Yusei Shiozawa
