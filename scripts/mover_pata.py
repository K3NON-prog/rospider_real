
import time 
import math
import signal
import rclpy 
from rclpy.node import Node 
from ros_robot_controller_msgs.msg import (ServosPosition, ServoPosition)

rclpy.init()
node = Node('mover_pata')
pub = pub =node.create_publisher(ServosPosition,'/ros_robot_controller/bus_servo/set_position',10)

time.sleep(1.0)

ID_SERVO = 4

POSICION_A = 700
POSICION_B = 950

def mover_servo(posicion):
    msg = ServosPosition()
    msg.duration = 1.0
    servo = ServoPosition()
    servo.id = ID_SERVO
    servo.position = posicion
    msg.position = [servo]
    pub.publish(msg)
    
for i in range(5):   
    print("Posicion A")
    mover_servo(POSICION_A)
    time.sleep(2.0)
    
    print("Posicion B")
    mover_servo(POSICION_B)
    time.sleep(2.0)
    print("Regreso a A")
    mover_servo(POSICION_A)
    time.sleep(2.0)

node.destroy_node()
rclpy.shutdown()
