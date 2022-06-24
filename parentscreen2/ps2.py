from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
import mainbox.mainbox

# from kivy.clock import Clock

Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...

class ParentScreen2(Screen):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen2')
    self.on_enter_count=0
    self.sc_tracker=2

  def on_enter(self):
    print('ParentScreen2 on_enter', self.on_enter_count)
    act_screen = self.children[0].children[1].children[0]
    self.main_box = act_screen.children[0].children[0].children[1]
    # extra_box = act_screen.children[0].children[0].children[0]
    self.main_box.ps1_base_width=self.parent.ps1_base_width
    self.main_box.ps1_base_height=self.parent.ps1_base_height
    self.main_box.size_kids()
    # Clock.schedule_once(self.main_box.size_kids(), 2)
    self.on_enter_count+=1

  def change_app_size(self, *args):
    self.main_box.sc=self.sc_tracker % 3 +1
    if self.main_box.sc == 3:
      self.btn_font_size.text="Font size: Large"
      self.btn_font_size.background_color=(.1,.1,.3)
    elif self.main_box.sc ==2:
      self.btn_font_size.text="Font size: Medium"
      self.btn_font_size.background_color=(.3,.3,.3)
    else:
      self.btn_font_size.text="Font size: Small"
      self.btn_font_size.background_color=(.6,.6,.9)
    self.sc_tracker+=1
    self.main_box.size_kids()

# class ExtraBoxLayout(BoxLayout):
#   ps1_base_height=ObjectProperty(0)
#   def __init__(self,**kwargs):
#     super().__init__(**kwargs)
#     print('ExtraBoxLayout __init__')
