

import rclpy
import time
import math
from sensor_msgs.msg import Imu

A_reposo = 9.17022724147515
umbral_impact = 0.023
umbral_rearme = 0.05

impacto_activo = False

def callback(msg):
    global impacto_activo
    a = msg.linear_acceleration
    #print(f"ace: x={a.x:.2f}, y={a.y:.2f}, z={a.z:.2f}")
    # Calcular magnitud
    magnitud = math.sqrt(a.x**2 + a.y**2 + a.z**2)
    #print("magnitud de aceleracion lineal: ", magnitud)
    delta_a = abs(magnitud - A_reposo)
    #print("Cambio de aceleracion: ", delta_a)
    if (delta_a >= umbral_impact and not impacto_activo):
        print(f"IMPACTO DETECTADO delta_a{delta_a:.4f} m/s^2")
        impacto_activo = True 
    
    elif (impacto_activo and delta_a <= umbral_rearme):
        impacto_activo = False
    
    

def main():
    rclpy.init()

    node = rclpy.create_node('impacto_imu')
    node.create_subscription(Imu,'/imu',callback,10)
    print("Leyendo IMU...")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
