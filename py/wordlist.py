from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color,Rectangle
import kivy.utils
import os
from kivy.app import App
#from main import Main 
wordsfile=os.listdir('./words')
class wordlistbutton(FloatLayout):
    def __init__(self,**kwarg):
        self.rows=1
        super(wordlistbutton,self).__init__()
        i=kwarg['counter']
        bul=Button(text=wordsfile[i][:-4],size_hint=(.2,.5),pos_hint={"x":.2,'y':.1},on_release= lambda a: kwarg['sel'].wordslist_button(wordsfile[i]))
        bur=Button(text=wordsfile[i+1][:-4],size_hint=(.2,.5),pos_hint={"x":.6,'y':.1},on_release= lambda a: kwarg['sel'].wordslist_button(wordsfile[i+1]))
        self.add_widget(bul)
        self.add_widget(bur)
