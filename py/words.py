from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color,Rectangle
from kivy.graphics import Color,Rectangle,Canvas
import kivy.utils
import os
import kivy

#wordsfile=os.listdir('./words')
class Words(FloatLayout):
    def __init__(self,**kwarg):
        self.canvas=Canvas()
        self.rows=1
        super(Words,self).__init__()
        kivy.resources.resource_add_path("./container_kvs")
        font1 = kivy.resources.resource_find("msgothic.ttc")
        label=Label(text="dwdwdw",font_name=font1,pos_hint={'x':.2,"y":.1},size_hint=(0,0))

        self.add_widget(label)

        #bur=Button(text='dwdw',size_hint=(.2,.5),pos_hint={"x":.1,'y':.1})
        #self.add_widget(bur)