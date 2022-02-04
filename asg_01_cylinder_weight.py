#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Cylinder

densidad = 0
valor = Cylinder()
density_found = False
volume_found = False

def callback(data):
	global densidad
	global density_found
	densidad = data.data	
	density_found = True	

def callback2(data):
	global valor
	global volume_found
	valor.volume = data.volume
	valor.surface_area = data.surface_area
	volume_found = True
	
def calculate():
	if density_found and volume_found:
		g = 9.8
		peso_especifico = densidad * g
		volumen = valor.volume
		peso = volumen * peso_especifico
		pub.publish(peso)			

rospy.init_node("cylinder_weight")
pub = rospy.Publisher("/weigth", Float64, queue_size=10)
rospy.Subscriber("/density", Float64, callback)
rospy.Subscriber("/cylinder", Cylinder, callback2)

while not rospy.is_shutdown():
	calculate()
	rospy.sleep(0.1)
	
