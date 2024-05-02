#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 88
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

# Inicializar el nodo ROS
rospy.init_node('robot_control', anonymous=True)

# Crear publicador para enviar comandos de movimiento al robot
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def sensor_callback(data):
    # Función de callback para el sensor de proximidad
    distancia = data.range  # Obtener la distancia medida por el sensor
    rospy.loginfo(f'Distancia al obstáculo: {distancia} metros')

    # Si la distancia es menor a 0.5 metros, detener el robot
    if distancia < 0.5:
        detener_robot()

def detener_robot():
    # Función para detener el movimiento del robot
    twist = Twist()  # Crear un mensaje Twist vacío
    pub.publish(twist)  # Publicar el mensaje para detener el robot
    rospy.loginfo('Robot detenido debido a la proximidad del obstáculo')

# Suscribirse al topic del sensor de proximidad
rospy.Subscriber('/sensor/proximidad', Range, sensor_callback)

# Iniciar el bucle principal del nodo ROS
rospy.spin()
