[![test](https://github.com/fukuda602/mypkg/actions/workflows/test.yml/badge.svg?branch=dev)](https://github.com/fukuda602/mypkg/actions/workflows/test.yml)
# mypkg
* このリポジトリは千葉工業大学ロボットシステム学で使用したROS2のパッケージを管理しています。
* cpuとじゃんけんを行うレポジトリ
* test.bashは問題ないが、Github Actionsでエラーが起こる状態です。
* 手元の端末では動作確認済み。　

## ノードとトピック
* player1.pyからplayer2.pyにgu-, cyoki, pa- を送り、player2.pyが3つのうちどれかをランダムで返します。

## 実行例
* 端末1
```
ros2 run mypkg player1
```
```
gu-
```
* 端末2
```
ros2 run mypkg player2
```
```
[INFO] [1672405609.860622400] [player2]: NOW_LOWDING:1
[INFO] [1672405610.362949300] [player2]: NOW_LOWDING:2
[INFO] [1672405610.864893800] [player2]: NOW_LOWDING:3
[INFO] [1672405611.367787400] [player2]: NOW_LOWDING:4
[INFO] [1672405611.871026300] [player2]: NOW_LOWDING:5
[INFO] [1672405612.373963700] [player2]: NOW_LOWDING:6
[INFO] [1672405612.875814200] [player2]: NOW_LOWDING:7
[INFO] [1672405613.378810900] [player2]: NOW_LOWDING:8
[INFO] [1672405613.884225100] [player2]: cpu: pa-
```
* 終了は【Ctrl + C】

## ROS2バージョン
* Foxy Fitzroy

## テスト環境
* Ubuntu20.04

## LICENSE
* BSDライセンスが適用されております。詳しくはLICENSEをご参照下さい。

ⓒ 2022 Taiki Fukuda
