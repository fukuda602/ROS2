[![test](https://github.com/fukuda602/mypkg/actions/workflows/test.yml/badge.svg?branch=dev)](https://github.com/fukuda602/mypkg/actions/workflows/test.yml)
# mypkg
* このリポジトリは千葉工業大学ロボットシステム学で使用したROS2のパッケージを管理しています。
* cpuとじゃんけんを行うレポジトリ
* test.bashは問題ないが、Github Actionsでエラーが起こる状態です。
* 手元の端末では動作確認済み。　

## ノードとトピック
* talker.pyからlistener.pyにgu-, cyoki, pa- を送り、listener.pyが3つのうちどれかをランダムで返します。

## 実行例
* 端末1
```
ros2 run mypkg talker
```
```
gu-
```
* 端末2
```
ros2 run mypkg listener
```
```
[INFO] [1672159993.350717100] [listener]: NOW_LOWDING:1
[INFO] [1672159993.853434600] [listener]: NOW_LOWDING:2
[INFO] [1672159994.356229000] [listener]: NOW_LOWDING:3
[INFO] [1672159994.859236800] [listener]: NOW_LOWDING:4
[INFO] [1672159995.361677000] [listener]: NOW_LOWDING:5
[INFO] [1672159999.635887500] [listener]: cpu: cyoki
```
* 終了は【Ctrl + C】

## ROS2バージョン
* Foxy Fitzroy

## テスト環境
* Ubuntu20.04

## LICENSE
* BSDライセンスが適用されております。詳しくはLICENSEをご参照下さい。

ⓒ 2022 Taiki Fukuda
