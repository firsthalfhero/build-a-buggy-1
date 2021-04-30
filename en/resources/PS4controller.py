from pyPS4Controller.controller import Controller
from pyPS4Controller.event_mapping.DefaultMapping import DefaultMapping
from gpiozero import Robot

robot = Robot(left = (7, 8), right = (9, 10))

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       print("Hello world")

    def on_x_release(self):
       print("Goodbye world")
       
    def on_left_arrow_press(self):
        robot.left()
        print("Left")
        
    def on_right_arrow_press(self):
        robot.right()
        print("Right")
        
        
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=600)