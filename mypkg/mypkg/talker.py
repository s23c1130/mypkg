# SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0


def cb():
    global n
    msg = Person()
    msg.name = '眞壁斗棋'
    msg.age = n
    pub.publish(msg)
    n += 1


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)