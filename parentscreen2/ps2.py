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

import mainbox.mainbox
import tablebox.tablebox
from utils import table_api_util

import webbrowser


# from kivy.clock import Clock

Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...



class ParentScreen2(Screen):
  child_sm=ObjectProperty(ScreenManager())
  # nav_drawer=ObjectProperty(BoxLayout())
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen2')
    # self.on_enter_count=0
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
    print('ParentScreen2 on_enter')
    act_screen = self.children[0].children[1].children[0]
    self.main_box = act_screen.children[0].children[0].children[1]

    self.main_box.label_email.text  = self.parent.email

    self.main_box.ps1_base_width=self.parent.ps1_base_width
    self.main_box.ps1_base_height=self.parent.ps1_base_height
    self.main_box.size_kids()
    self.main_box.login_token = self.parent.login_token
    self.main_box.user_id = self.parent.id



    self.font_size_toolbar_size()
    self.navmenu_font_size()

    # self.on_enter_count+=1

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
    print('navmenu_font_size')


    self.navmenu.label_act_screen.text = "Add Activity"
    self.navmenu.label_table_screen.text = "View Logged Activities"
    self.navmenu.label_wsh_web.text = "What-Sticks Website"
    self.navmenu.label_exit.text = "Exit"

    self.navmenu.label_table_screen.color = (.1,.1,.1)
    self.navmenu.label_table_screen.size_hint = (None,None)

    self.navmenu.label_act_screen.color = (.1,.1,.1)
    self.navmenu.label_act_screen.size_hint = (None,None)

    self.navmenu.label_wsh_web.color = (.1,.1,.1)
    self.navmenu.label_wsh_web.size_hint = (None,None)

    self.navmenu.label_exit.color = (.1,.1,.1)
    self.navmenu.label_exit.size_hint = (None,None)

    self.navmenu.anchor_act_screen_label.size_hint_y = None
    self.navmenu.anchor_act_screen_label.height = self.navmenu.height * .1
    self.navmenu.anchor_act_screen_label.anchor_x = "left"
    self.navmenu.anchor_act_screen_label.padding = (self.navmenu.width * .02,0,0,0)

    self.navmenu.anchor_table_screen_label.size_hint_y = None
    self.navmenu.anchor_table_screen_label.height = self.navmenu.height * .1
    self.navmenu.anchor_table_screen_label.anchor_x = "left"
    self.navmenu.anchor_table_screen_label.padding = (self.navmenu.width * .02,0,0,0)

    self.navmenu.anchor_wsh_web_label.size_hint_y = None
    self.navmenu.anchor_wsh_web_label.height = self.navmenu.height * .1
    self.navmenu.anchor_wsh_web_label.anchor_x = "left"
    self.navmenu.anchor_wsh_web_label.padding = (self.navmenu.width * .02,0,0,0)

    self.navmenu.anchor_exit_label.size_hint_y = None
    self.navmenu.anchor_exit_label.height = self.navmenu.height * .1
    self.navmenu.anchor_exit_label.anchor_x = "left"
    self.navmenu.anchor_exit_label.padding = (self.navmenu.width * .02,0,0,0)

    menu_item_font_size = self.fit_navmenu_item_util(self.navmenu.label_act_screen)
    self.navmenu.label_table_screen.font_size = menu_item_font_size
    self.navmenu.label_wsh_web.font_size = menu_item_font_size
    self.navmenu.label_exit.font_size = menu_item_font_size

    self.fit_navmenu_item_util_2(self.navmenu.label_table_screen)
    self.fit_navmenu_item_util_2(self.navmenu.label_wsh_web)
    self.fit_navmenu_item_util_2(self.navmenu.label_exit)

    Clock.schedule_once(self.navmenu_sizing, .01)

  def navmenu_sizing(self, *args):
    self.navmenu.label_table_screen.size = self.navmenu.label_table_screen.texture_size
    self.navmenu.label_act_screen.size = self.navmenu.label_act_screen.texture_size
    self.navmenu.label_wsh_web.size = self.navmenu.label_wsh_web.texture_size
    self.navmenu.label_exit.size = self.navmenu.label_exit.texture_size

    menu_items_list = [self.navmenu.label_table_screen,
      self.navmenu.label_act_screen,
      self.navmenu.label_wsh_web,self.navmenu.label_exit]

    min_font_size = min([i.font_size for i in menu_items_list])

    for i in menu_items_list:
      i.font_size = min_font_size
      i.texture_update()
      i.size = i.texture_size





  def fit_navmenu_item_util(self, thing):
    while thing.texture_size[0] < (self.navmenu.width * .85) and \
      thing.texture_size[1] < (self.navmenu.height * .085):
      thing.font_size += 1
      thing.texture_update()

    while thing.texture_size[0] > (self.navmenu.width * .85) or \
      thing.texture_size[1] > (self.navmenu.height * .085):
      thing.font_size -= 1
      thing.texture_update()

    return thing.font_size


  def fit_navmenu_item_util_2(self, thing):
    thing.texture_update()

    line_height = self.navmenu.height * .1

    if thing.texture_size[0] > (self.navmenu.width * .9):
      print('view logged is too long')
      space_per_letter =  len(list(thing.text)) / thing.texture_size[0]
      line_length = round(space_per_letter * self.navmenu.width *.9)
      print('line_length aka number of characters in line:::', line_length)
      pos_last_space_line = thing.text[line_length:].find(' ')
      print('thing.text[line_length:]:::', thing.text[line_length:])
      print('pos_last_space_line:::', pos_last_space_line)
      if pos_last_space_line != -1:
        new_string_list = list(thing.text)
        new_string_list[line_length + pos_last_space_line]="\n"
        thing.text=''.join(new_string_list)
        thing.halign ='left'
        thing.texture_update()

        line_height = self.navmenu.height * .2
        thing.parent.height = line_height

    # print('thing.font_size:::', thing.font_size)


    while thing.texture_size[0] > (self.navmenu.width * .85) or \
      thing.texture_size[1] > (line_height * .85):
      thing.font_size -= 1
      thing.texture_update()


    return thing.font_size

  def where_is_it(self):
    print("pos:::",self.navmenu.label_table_screen.pos)
    print("navmenu.size:", self.navmenu.size)
    print("navmenu.pos::", self.navmenu.pos)
    print('label_table_screen::', self.navmenu.label_table_screen.texture_size)

  def change_screen(self):
    # if
    self.child_sm.current = "table_screen"



class AnchorClickable(TouchRippleBehavior, ButtonBehavior, AnchorLayout):
  ripple_duration_out = NumericProperty(.7)
  ripple_duration_in = NumericProperty(1)
  def __init__(self, **kwargs):
    super(AnchorClickable, self).__init__(**kwargs)

  def on_touch_down(self, touch):
    collide_point = self.collide_point(touch.x, touch.y)
    if collide_point:
      touch.grab(self)
      self.ripple_show(touch)
      print('AnchorClickable clicked')
      ps2 = self.parent.parent.parent.parent
      # ps2.where_is_it()
      print('This label sys::', self.children[0].text)
      if self.children[0].text[:4] == 'Add ':
        ps2.child_sm.current = 'act_screen'
      elif self.children[0].text[:4] == 'View':
        ps2.child_sm.current = 'table_screen'
        ps2.table_box_util()# utility for sending data to table_box
      elif self.children[0].text[:4] == 'What':
        webbrowser.open('https://what-sticks-health.com')


      return True
    return False


  def on_touch_up(self, touch):
    if touch.grab_current is self:
      touch.ungrab(self)
      self.ripple_fade()
      return True
    return False
