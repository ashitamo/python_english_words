from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen ,SwapTransition
from kivy.base import EventLoop
from kivy.core.window import Window
from kivy.graphics import Color,Rectangle,Canvas
import kivy
from kivy import utils
import os
from py.words import Words

import requests,json
from py.homescreen import homebutton 
from py.wordlist import wordlistbutton
class HomeScreen(Screen):
    pass
class Setting(Screen):
    pass
class WordListScreen(Screen):
    pass
class Screen_Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Screen_Manager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)
    def on_key(self, window, key, *args):
        if key == 27: 
            if self.current_screen.name == "home_screen":
                return False  # exit the app from this page
            elif self.current_screen.name == "wordlist_screen":
                self.current = "home_screen"
                return True  # do not exit the app
class WordsScreen(Screen):
    pass

GUI=Builder.load_file('kv/main.kv')
kivy.resources.resource_add_path("./container_kvs")
font1 = kivy.resources.resource_find("msgothic.ttc")

class Main(App):
    def build(self):
        return GUI
    def switch(self,screenname):
        screen_manager = self.root.ids['screen_manager']
        #screen_manager.transition=SwapTransition()
        #screen_manager.     = SwapTransition
        screen_manager.current = screenname
    def back(self):
        screen_manager = self.root.ids['screen_manager']
        if screen_manager.current_screen.name == "home_screen":
            cheak_back_floatlayout=self.root.ids['home_screen'].ids['cheak_back_floatlayout']
            # la =Label(text="dwwdwdwd")
            # cheak_back_floatlayout.add_widget(la)
            #can=Canvas()
            #cheak_back_floatlayout.canvas.add(Color(1.,1.,0))
            
            # x=self.root.center_y-cheak_back_floatlayout.size[0] /2
            # y=self.root.center_x-cheak_back_floatlayout.size[1] /2

            # print(x,y)
            # cheak_back_floatlayout.canvas.add(Rectangle(source='img/cheak_back.png',pos=(x,y),size=cheak_back_floatlayout.size))
            # print(cheak_back_floatlayout.canvas.pos)
            
            # can = self.root.ids['cheak_back_floatlayout'].ids['cheak_back_can']
            # can.add(Color(1.,1.,0))
            #floatlayout= FloatLayout(pos_hint={'top': 0.97,'right':0.12},size_hint=(.25,.2))
            #can.add(Rectangle(pos=cheak_back_floatlayout.pos,size=cheak_back_floatlayout.size))
            #cheak_back_floatlayout.canvas=can
            #print("fin",cheak_back_floatlayout.pos,cheak_back_floatlayout.size)
            self.stop()  # exit the app from this page
        elif screen_manager.current_screen.name == "settings_screen":
            screen_manager.current = "home_screen"
        elif screen_manager.current_screen.name == "wordlist_screen":
            screen_manager.current = "home_screen"
            return True  # do not exit the app
    def on_start(self):
        homebutton(homescreen=self.root.ids['home_screen'].ids)#back button
        scroll_layout=self.root.ids['wordlist_screen'].ids['scroll_layout']
        #for i in os.listdir('./words'):
        for i in range(0,len(os.listdir('./words')),2):
            a=wordlistbutton(counter=i,sel=self)
            scroll_layout.add_widget(a)
        print('running')
    def wordslist_button(self,wordsfile):
        print(wordsfile)
        screen_manager = self.root.ids['screen_manager']
        counterlist=[]
        scroll_layout=self.root.ids['words_screen'].ids['Words_scroll_layout']
        # with open('./words/1.txt','r',encoding='utf8') as rq:
        #     lines=rq.readlines()
        # for i in range(0,len(lines),1):
        #     wordlist=lines[i].split()
        #     for j in range(0,len(wordlist),1):
        #         if wordlist[j][0]=='#':
        #             counterlist.append(j)
        #     Words(wordsfile=wordsfile,counterlist=counterlist,wordlist=wordlist,
        #     counter=i)
        for _ in range(50):
            scroll_layout.add_widget(Words())
        screen_manager.current="words_screen"
        #print(scroll_layout.Label)

        
        
    
         

if __name__ == "__main__":
    Main().run()