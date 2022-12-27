#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 Taiki Fukuda s21C1101AP@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Int16
from person_msgs.srv import Query

y = ["pa-", "gu-" ,"choki"]
result = random.choice(y)
input("jyanken:")

def cb(resquest, response):
    result = random.choice(y)
    if resquest.you == "gu-":
        response.cpu = result
    elif resquest.you == "choki":
        response.cpu = result
    elif resquest.you == "pa-":
        response.cpu = result
    else:
        response.cpu = "error"

    return response


#def main():
rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)

if __name__ == '__main__':
    main()
