# SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

import pyautogui
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
rclpy.init()
node = Node("MousePointPub")
x_pub = node.create_publisher(Int32, "x_pos", 10)
y_pub = node.create_publisher(Int32, "y_pos", 10)
n = 0
def cb():
    global n
    x, y = pyautogui.position()
    x_msg = Int32()
    y_msg = Int32()
    x_msg.data = x
    y_msg.data = y
    x_pub.publish(x_msg)
    y_pub.publish(y_msg)
def main():
    node.create_timer(0.1, cb)
    rclpy.spin(node)