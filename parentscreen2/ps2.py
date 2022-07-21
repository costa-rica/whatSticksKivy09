from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors.touchripple import TouchRippleBehavior
from kivymd.app import MDApp

import mainbox.mainbox
import tablebox.tablebox
from utils import table_api_util
import webbrowser


Builder.load_file('parentscreen2/ps2.kv')


class NavMenu(BoxLayout): ...


class ParentScreen2(Screen):
  child_sm=ObjectProperty(ScreenManager())
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen2')
    self.sc_tracker=2

  def table_box_util(self,*args):# passes
    print('ParentScreen2 table_box_util')
    self.table_box = self.children[0].children[1].children[0].children[0]

  # Get base measurements and pass to table_box
    self.table_box.ps1_base_width = self.parent.ps1_base_width
    self.table_box.ps1_base_height = self.parent.ps1_base_height
    self.table_box.login_token = self.parent.login_token
    self.table_box.user_id = self.parent.id
    self.table_box.email = self.parent.email

  #Get data from apip and pass it to the table_box
    self.table_box.row_data_list = table_api_util(self.table_box.login_token)

  def on_enter(self):
    print('ParentScreen2 on_enter')
    act_screen = self.children[0].children[1].children[0]

    # nav_menu = act_screen.parent.parent.children[0].children[0]

    self.nav_menu.ps1_base_height = self.parent.ps1_base_height
    self.nav_menu.anchor_version.padding = (0,0,self.nav_menu.width * .1, self.parent.ps1_base_height * .1)
    self.nav_menu.label_version.font_size

    self.main_box = act_screen.children[0].children[0].children[1]
    self.main_box.label_email.text  = self.parent.email
    self.main_box.ps1_base_width=self.parent.ps1_base_width
    self.main_box.ps1_base_height=self.parent.ps1_base_height
    self.main_box.size_kids()
    self.main_box.login_token = self.parent.login_token
    self.main_box.user_id = self.parent.id

    self.font_size_toolbar_size()
    self.navmenu_font_size()


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

      self.table_box.size_email()
      Clock.schedule_once(self.table_box.size_email_2,.01)

    except AttributeError:
      print('no table_box object yet')



  def font_size_toolbar_size(self):
    while self.btn_font_size.texture_size[0] < self.btn_font_size.width * .7 and \
      self.btn_font_size.texture_size[1] < self.btn_font_size.height * .7:
      self.btn_font_size.font_size+=1
      self.btn_font_size.texture_update()

    if self.btn_font_size.text == 'Font Size':
      Clock.schedule_once(self.font_size_toolbar_size_2, .01)

  def font_size_toolbar_size_2(self, *args):
  # if 'Font Size' is wider than button -> split it into two rows and shrink till it fits
    if self.btn_font_size.text == 'Font Size' and \
      self.btn_font_size.texture_size[0] > self.btn_font_size.width * .95:
      self.btn_font_size.text = 'Font\nsize'
      while self.btn_font_size.texture_size[1] > self.btn_font_size.height:
        self.btn_font_size.font_size -= .25
        self.btn_font_size.texture_update()

  def navmenu_font_size(self):
    print('navmenu_font_size')
    self.nav_menu.label_act_screen.text = "Add Activity"
    self.nav_menu.label_table_screen.text = "View Logged Activities"
    self.nav_menu.label_wsh_web.text = "Go to Website"
    self.nav_menu.label_exit.text = "Exit"
    self.nav_menu.label_version.text = "Version 0.64"

    self.nav_menu.label_table_screen.color = (.1,.1,.1)
    self.nav_menu.label_table_screen.size_hint = (None,None)

    self.nav_menu.label_act_screen.color = (.1,.1,.1)
    self.nav_menu.label_act_screen.size_hint = (None,None)

    self.nav_menu.label_wsh_web.color = (.1,.1,.1)
    self.nav_menu.label_wsh_web.size_hint = (None,None)

    self.nav_menu.label_exit.color = (.1,.1,.1)
    self.nav_menu.label_exit.size_hint = (None,None)

    self.nav_menu.label_version.color = (.1,.1,.1)
    self.nav_menu.label_version.size_hint = (None,None)

    self.nav_menu.anchor_act_screen_label.size_hint_y = None
    self.nav_menu.anchor_act_screen_label.height = self.nav_menu.height * .1
    self.nav_menu.anchor_act_screen_label.anchor_x = "left"
    self.nav_menu.anchor_act_screen_label.padding = (self.nav_menu.width * .02,0,0,0)

    self.nav_menu.anchor_table_screen_label.size_hint_y = None
    self.nav_menu.anchor_table_screen_label.height = self.nav_menu.height * .1
    self.nav_menu.anchor_table_screen_label.anchor_x = "left"
    self.nav_menu.anchor_table_screen_label.padding = (self.nav_menu.width * .02,0,0,0)

    self.nav_menu.anchor_wsh_web_label.size_hint_y = None
    self.nav_menu.anchor_wsh_web_label.height = self.nav_menu.height * .1
    self.nav_menu.anchor_wsh_web_label.anchor_x = "left"
    self.nav_menu.anchor_wsh_web_label.padding = (self.nav_menu.width * .02,0,0,0)

    self.nav_menu.anchor_exit_label.size_hint_y = None
    self.nav_menu.anchor_exit_label.height = self.nav_menu.height * .1
    self.nav_menu.anchor_exit_label.anchor_x = "left"
    self.nav_menu.anchor_exit_label.padding = (self.nav_menu.width * .02,0,0,0)

    # self.nav_menu.anchor_exit_label.size_hint_y = None
    # self.nav_menu.anchor_exit_label.height = self.nav_menu.height * .1
    self.nav_menu.anchor_version.anchor_x = "right"
    self.nav_menu.anchor_version.anchor_y = "bottom"

    # self.nav_menu.anchor_version.padding = (0,0,self.nav_menu.width * .02,self.nav_menu.height * .02)
    self.nav_menu.anchor_version.padding = (0,0,self.nav_menu.width * .02,self.nav_menu.height * .05)

    # self.nav_menu.label_table_screen.font_size = menu_item_font_size
    # self.nav_menu.label_wsh_web.font_size = menu_item_font_size
    # self.nav_menu.label_exit.font_size = menu_item_font_size
    self.fit_navmenu_item_util(self.nav_menu.label_act_screen)
    self.fit_navmenu_item_util(self.nav_menu.label_table_screen)
    self.fit_navmenu_item_util(self.nav_menu.label_wsh_web)
    self.fit_navmenu_item_util(self.nav_menu.label_exit)
    self.fit_navmenu_item_util(self.nav_menu.label_version)
    # self.nav_menu.label_version.font_size = 20

    Clock.schedule_once(self.navmenu_sizing, .01)

  def navmenu_sizing(self, *args):
    self.nav_menu.label_table_screen.size = self.nav_menu.label_table_screen.texture_size
    self.nav_menu.label_act_screen.size = self.nav_menu.label_act_screen.texture_size
    self.nav_menu.label_wsh_web.size = self.nav_menu.label_wsh_web.texture_size
    self.nav_menu.label_exit.size = self.nav_menu.label_exit.texture_size
    self.nav_menu.label_version.size = self.nav_menu.label_version.texture_size

    menu_items_list = [self.nav_menu.label_table_screen,
      self.nav_menu.label_act_screen,
      self.nav_menu.label_wsh_web,self.nav_menu.label_exit]

    min_font_size = min([i.font_size for i in menu_items_list])

    for i in menu_items_list:
      i.font_size = min_font_size
      i.texture_update()
      i.size = i.texture_size



  def fit_navmenu_item_util(self, thing):
    while thing.texture_size[0] < (self.nav_menu.width * .85) and \
      thing.texture_size[1] < (self.nav_menu.height * .085):
      thing.font_size += 1
      thing.texture_update()

    while thing.texture_size[0] > (self.nav_menu.width * .85) or \
      thing.texture_size[1] > (self.nav_menu.height * .085):
      thing.font_size -= .25
      thing.texture_update()

    return thing.font_size

  def change_screen(self):
    self.child_sm.current = "table_screen"



class AnchorClickable_nav(ButtonBehavior,AnchorLayout):
  ripple_duration_out = NumericProperty(.7)
  ripple_duration_in = NumericProperty(1)
  def __init__(self, **kwargs):
    super(AnchorClickable_nav, self).__init__(**kwargs)

  def on_touch_down(self,touch):
    collide_point_1 = self.collide_point(touch.x, touch.y)
    if collide_point_1:
      print('Table on_touch_down')
      self.ps2 = self.parent.parent.parent.parent
      Clock.schedule_once(self.options,1)


  def on_touch_up(self, touch):
    if touch.grab_current is self:
      touch.ungrab(self)
      self.ripple_duration_out = 0.4
      self.ripple_fade()
      print('Table on_touch_UP')
      return True
    return False



  def options(self,*args):
    print('self.children[0].text[:4]:::',self.children[0].text[:4])
    if self.children[0].text[:4] == 'Add ':
      self.ps2.child_sm.current = 'act_screen'
    elif self.children[0].text[:4] == 'View':
      self.ps2.child_sm.current = 'table_screen'
      self.ps2.table_box_util()# utility for sending data to table_box
    elif self.children[0].text[:4] == 'Go t':
      webbrowser.open('https://what-sticks-health.com')
    elif self.children[0].text[:4] == 'Exit':
      print('app exit')
      MDApp.get_running_app().stop()
