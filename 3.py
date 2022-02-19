from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen;
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.clock import Clock

Window.size=(350,600)

LabelBase.register(name="hhh",fn_regular='hhh.otf')

class Fir(Screen):
    pass

class Ghiro(Screen):
    pass

class mai(MDApp):
    global screen_manager
    screen_manager= ScreenManager()
    
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "LightBlue"
        
        screen_manager.add_widget(Builder.load_file("3.kv"))
        screen_manager.add_widget(Builder.load_file("3_main.kv"))
        screen_manager.add_widget(Builder.load_file("3_signup.kv"))
        screen_manager.add_widget(Builder.load_file("3_first.kv"))
        screen_manager.add_widget(Builder.load_file("3_inf.kv"))
        screen_manager.add_widget(Builder.load_file("3_com.kv"))
        
        
        return screen_manager
    
    def on_start(self):
        Clock.schedule_once(self.change_scren, 3)
        
    def change_scren(self, dt):
        screen_manager.current='first'

    
mai().run()