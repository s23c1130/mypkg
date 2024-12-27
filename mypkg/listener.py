import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
rclpy.init()
node = Node("listener")

def cb(x_pub):
    global node
    node.get_logger().info("x:%d" % x_pub.data)
        

def cb2(y_pub):
    global node
    node.get_logger().info("y:%d" % y_pub.data)



def main():
    x_pub = node.create_subscription(Int32, "x_pos", cb, 10)
    y_pub = node.create_subscription(Int32, "y_pos", cb2, 10)
    rclpy.spin(node)