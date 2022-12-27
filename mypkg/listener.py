#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 Taiki Fukuda s21C1101AP@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

#import rclpy
#from rclpy.node import Node
#from std_msgs.msg import Int16

#def cb(msg):
#    global node
#    node.get_logger().info("Listen: %d" % msg.data)

#rclpy.init()
#node = Node("listener")
#pub = node.create_subscription(Int16, "countup", cb, 10)
#rclpy.spin(node)

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
    n = 0
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, 'query') 
    while not client.wait_for_service(timeout_sec=1.0):
        n += 1
        node.get_logger().info("NOW_LOWDING:%d" % (n))
         
    req = Query.Request()
    req.you = "gu-"
    future = client.call_async(req) 

    while rclpy.ok():
        rclpy.spin_once(node) 
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('error')
            else:
                node.get_logger().info("cup: {}".format(response.cpu))
            
            break
    
    node.destroy_node() 
    rclpy.shutdown() 

if __name__ == '__main__': 
    main()
