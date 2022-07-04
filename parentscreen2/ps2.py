from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.graphics import Color, Rectangle
# from kivymd.uix.navigationdrawer import MDNavigationDrawer

import mainbox.mainbox
import tablebox.tablebox
from utils import table_api_util



# from kivy.clock import Clock

Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...



class ParentScreen2(Screen):
  child_sm=ObjectProperty(ScreenManager())
  # nav_drawer=ObjectProperty(BoxLayout())
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen2')
    self.on_enter_count=0
    self.sc_tracker=2
    # self.child_sm.bind(self.child_sm.children==self.screen_change)
    # self.nav_drawer.bind(on_motion = self.nav_drawer_pos)




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

    print('self.parent.email:::', self.parent.email, type(self.parent.email))
    print('********')
    self.main_box.label_email.text  = self.parent.email



    self.main_box.ps1_base_width=self.parent.ps1_base_width
    self.main_box.ps1_base_height=self.parent.ps1_base_height
    self.main_box.size_kids()
    self.main_box.login_token = self.parent.login_token
    self.main_box.user_id = self.parent.id



    self.font_size_toolbar_size()
    self.navmenu_font_size()
    self.navmenu_line()

    self.nav_drawer.bind(on_motion = self.nav_drawer_pos)

    self.on_enter_count+=1

  def change_app_size(self, *args):
    self.main_box.sc=self.sc_tracker % 3 +1
    if self.main_box.sc == 3:
      self.btn_font_size.text="Large"
      self.btn_font_size.background_color=(.5,.5,1, .5)
    elif self.main_box.sc ==2:
      self.btn_font_size.text="Font Size"
      self.btn_font_size.background_color=(.3,.3,.3)
    else:
      self.btn_font_size.text="Small"
      self.btn_font_size.background_color=(.5,.5,1, .5)
    self.sc_tracker+=1
    self.main_box.size_kids()

    self.font_size_toolbar_size()

    try:
      self.table_box.sc =  self.main_box.sc
      self.table_box.size_rows_util()
    except AttributeError:
      print('no table_box object yet')



  def font_size_toolbar_size(self):
    while self.btn_font_size.texture_size[0] < self.btn_font_size.width * .7 and \
      self.btn_font_size.texture_size[1] < self.btn_font_size.height * .7:
      self.btn_font_size.font_size+=1
      self.btn_font_size.texture_update()

  def navmenu_font_size(self):
    # print('*****')
    print('self.navmenu.list_item_table.size::', self.navmenu.list_item_table.size)
    # print('self.navmenu.list_item_table.font_size::', self.navmenu.list_item_table.texture_size)
    # print(dir(self.navmenu.list_item_table))

    print('self.navmenu.box_table_screen_label.size:', self.navmenu.box_table_screen_label.size)
    print('self.navmenu.label_table_screen.size:::', self.navmenu.label_table_screen.size)

  def navmenu_line(self):
    print('**** navmenu_line')
    box_label = self.navmenu.box_table_screen_label
    print(self.navmenu.x,box_label.y)
    # print(dir(self.nav_drawer))
    with box_label.canvas:
      Color(.3,.3,.3,1)
      Rectangle(pos=(self.nav_drawer.x,box_label.y),
        size=(self.navmenu.width * .02, 3))###

  def nav_drawer_pos(self):
    print(self.nav_drawer.x)

  def on_motion(self, etype, me):
    print(self.nav_drawer.x)
