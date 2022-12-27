#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 Taiki Fukuda s21C1101AP@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
import random
from rclpy.node import Node
#from std_msgs.msg import Int16
from person_msgs.srv import Query

y = ["pa-", "gu-" ,"choki"]
result = random.choice(y)
input("jyanken:")

class Talker():
#    def __init__(self, node):
#        self.pub = node.create_publisher(Int16, "countup", 10)
#        self.n = 0
#        node.create_timer(0.5, self.cb)

#    def cb(self):
#        msg = Int16()
#        msg.data = self.n
#        self.pub.publish(msg)
#        self.n += 1
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

srv = node.create_service(Query, "query", cb)

def main():
    rclpy.init()
    node = Node("talker")
#    talker = Talker(node)
#    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
