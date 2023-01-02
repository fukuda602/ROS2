[![test](https://github.com/fukuda602/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/fukuda602/mypkg/actions/workflows/test.yml)
# mypkg
* このリポジトリは千葉工業大学ロボットシステム学で使用したROS2のパッケージを管理しています。

## ノードとトピック
* talker.pyからlistener.pyに1,2,3...nの数字を送り、listener.pyで標準出力します。

## 実行例
* 端末1
```
ros2 run mypkg talker
```
* 端末2
```
ros2 run mypkg listener
```
```
[INFO] [1672160812.793019600] [listener]: Listen: 22
[INFO] [1672160813.230284800] [listener]: Listen: 23
[INFO] [1672160813.730327400] [listener]: Listen: 24
[INFO] [1672160814.230059900] [listener]: Listen: 25
[INFO] [1672160814.731179000] [listener]: Listen: 26
```
* 終了は【Ctrl + C】

## ROS2バージョン
* Foxy Fitzroy

## テスト環境
* Ubuntu20.04

## LICENSE
* BSDライセンスが適用されております。詳しくはLICENSEをご参照下さい。

ⓒ 2022 Taiki Fukuda
