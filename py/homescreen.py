from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color,Rectangle
import kivy.utils

class homelebel(Label):
    pass
class backlayout(FloatLayout):
    pass
class homebutton(object):
    def __init__(self,**kwarg):
        super(homebutton,self).__init__()
        kivy.resources.resource_add_path("./font/")
        font1 = kivy.resources.resource_find("bold.ttc")
        value=['單字庫','','','','','']
        for i in range(6):
            bu=kwarg['homescreen']['bu'+str(i+1)]
            bu.text=value[i]
            bu.font_name=font1

