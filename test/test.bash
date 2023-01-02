#!/bin/bash
# SPDX-FileCopyrightText: 2022 Taiki Fukuda s21C1101AP@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg play1_play2.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log 
grep 'NOW_LOWDING:5'
