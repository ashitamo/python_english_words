from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color,Rectangle,Canvas,Line
import kivy.utils
import os
import kivy

#wordsfile=os.listdir('./words')
class Words(FloatLayout):
    def __init__(self,**kwarg):
        #self.canvas=Canvas()
        self.rows=1
        super(Words,self).__init__()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#67697C")))
            self.rect=Rectangle(size=self.size,pos=self.pos)
        self.bind(pos=self.update_rect,size=self.update_rect)
        # #self.canvas.add(Color(1.,1.,1.))
        print(kwarg)
        print(self.size)
        kivy.resources.resource_add_path("./font/")
        font1 = kivy.resources.resource_find("bold.ttc")
        word=kwarg['wordlist']
        for i in range(len(word)):
            word[i]=word[i].replace('/n','').replace('_',' ')
            

        llabel=Label(text=word[0],bold=True,font_name=font1,size_hint=(.35,1),pos_hint={'top':.8,'left':1},
        text_size=(150,100),halign='left',valign='top')
        self.add_widget(llabel)
        del word[0]
        for i in range(len(word)):
            a=0.9-i*0.2
            rlabel=Label(text=word[i],font_name=font1,size_hint=(1,1),pos_hint={'top':a,'left':1},
            text_size=(250,100),halign='left',valign='top')
            self.add_widget(rlabel)
        #     #print(text)
        #     if i==0:#wordlab
        #         wordlab=Label(text=text,font_name=font1,pos_hint={'top':1,"left":.1},size_hint=(.3,1))
        #         self.add_widget(wordlab)
        #     else:
        #         meanlab=Label(text=text,font_name=font1,pos_hint={'top':1-(i-1)*0.2,"left":.4},size_hint=(1,.2))
        #         self.add_widget(meanlab)
        #         print(1-(i-0)*0.2)
        # print('f')

        #llabel=Image(source='img/backgroung.png',size_hint=(1,.8),pos_hint={'top':1,'left':1})
        # rlabel=Label(text='air_conditioner',size_hint=(1,1),pos_hint={'top':.9,'left':.5},text_size=self.size,halign='left',valign='top')
        # r2label=Label(text='r2',size_hint=(1,1),pos_hint={'top':.6,'left':.5},text_size=self.size,halign='left',valign='top')
        

        # self.add_widget(llabel)
        # self.add_widget(rlabel)
        # self.add_widget(r2label)
            #print(lf.size,self.pos)
        
        bu=Button(text="詳細",pos_hint={'top':.9,'right':.9},size_hint=(.1,.4),font_name=font1)
        bu2=Button(text="播放",pos_hint={'top':.5,'right':.9},size_hint=(.1,.4),font_name=font1)
        self.add_widget(bu)
        self.add_widget(bu2)
        
    def update_rect(self,*args):
        self.rect.pos=self.pos
        self.rect.size=self.size