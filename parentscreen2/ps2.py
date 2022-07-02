from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog

import mainbox.mainbox
import tablebox.tablebox
from utils import table_api_util



# from kivy.clock import Clock

Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...



class ParentScreen2(Screen):
  child_sm=ObjectProperty(ScreenManager())
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen2')
    self.on_enter_count=0
    self.sc_tracker=2
    # self.child_sm.bind(self.child_sm.children==self.screen_change)


  def table_box_util(self,*args):# passes
    print('ParentScreen2 table_box_util')
    self.table_box = self.children[0].children[1].children[0].children[0]

  # Get base measurements and pass to table_box
    self.table_box.ps1_base_width = self.parent.ps1_base_width
    self.table_box.ps1_base_height = self.parent.ps1_base_height
    self.table_box.login_token = self.parent.login_token
    self.table_box.user_id = self.parent.id
    # self.table_box.user_timezone = self.parent.user_timezone

  #Get data from apip and pass it to the table_box
    # self.table_screen_id.table_grid.row_data_list = table_api_util(self.parent.login_token)
    self.table_box.row_data_list = table_api_util(self.table_box.login_token)
    print('self.table_box.row_data_list ::::')
    print(self.table_box.row_data_list [0:4])

  def on_enter(self):
    print('ParentScreen2 on_enter', self.on_enter_count)
    act_screen = self.children[0].children[1].children[0]
    self.main_box = act_screen.children[0].children[0].children[1]
    self.main_box.ps1_base_width=self.parent.ps1_base_width
    self.main_box.ps1_base_height=self.parent.ps1_base_height
    self.main_box.size_kids()
    self.main_box.login_token = self.parent.login_token

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

    try:
      self.table_box.sc =  self.main_box.sc
      self.table_box.size_rows_util()
    except AttributeError:
      print('no table_box object yet')
