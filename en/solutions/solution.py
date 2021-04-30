from gpiozero import Robot
""" from en.resources.PS4controller import MyController """
from time import sleep, time

robot = Robot(left = (7, 8), right = (9, 10))
while True:
	robot.forward()
	sleep(3)
	robot.stop()
	robot.right()
	sleep(1)
	robot.stop()
""" 

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=600) """