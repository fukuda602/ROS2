[![test](https://github.com/fukuda602/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/fukuda602/mypkg/actions/workflows/test.yml)
# mypkg
* このリポジトリは千葉工業大学ロボットシステム学で使用したROS2のパッケージを管理しています。

## トピック
* talker.pyからlistener.pyに1,2,3...nの数字を送ります。

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

## 必要ソフトフェア
* Python 3.7 ～ 3.10

## テスト環境
* Ubuntu20.04

## LICENSE
* BSDライセンスが適用されております。詳しくはLICENSEをご参照下さい。

ⓒ 2022 Taiki Fukuda
