import pyautogui
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int32, "countup", 10)
n = 0
def cb():
    global n
    x, y = pyautogui.position()
    msg = Int32()
    msg.data = (x << 16) | y
    pub.publish(msg)
def main():
    node.create_timer(0.1, cb)
    rclpy.spin(node)