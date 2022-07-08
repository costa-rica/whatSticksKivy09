from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from size_dict import size_dict
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.graphics import Color, Rectangle
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import time

from kivy.clock import Clock

from utils import table_api_util, delete_row_util

Builder.load_file('areyousure/areyousure.kv')


def text_fitter_label_util( thing):
  while thing.texture_size[0] < thing.width * .6 and \
    thing.texture_size[1] < thing.height * .6:
    thing.font_size+=1
    thing.texture_update()

  return thing.font_size


def text_fitter_button_util(thing):
  while thing.texture_size[0] < thing.width * .4 and \
    thing.texture_size[1] < thing.height * .4:
    thing.font_size+=1
    thing.texture_update()

  return thing.font_size


class AreYouSureBox(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  on_size_count=ObjectProperty(0)
  delete_btn=ObjectProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('****** AreYouSureBox __init__')
    self.on_size_count=0


  def on_size(self, *args):
    print('******  AreYouSureBox on_size')
    if self.on_size_count == 1:
      # print(self.parent)
      Clock.schedule_once(self.get_size, .01)
    self.on_size_count += 1

  def get_size(self, *args):
    print('AreYouSureBox get_size')
    # print('self.parent:::', self.parent.children[1].ps1_base_width)
    self.table_box = self.parent.children[1]

    self.ps1_base_width = self.table_box.ps1_base_width
    self.ps1_base_height = self.table_box.ps1_base_height

    self.pos_hint ={"center_x":.5,"center_y":.5}
    self.label_title.text = f"Are you sure you want to delete {self.delete_btn.name}?"
    self.text_fitter_util(self.label_title)
    self.text_fitter_button_util(self.btn_yes)
    self.text_fitter_button_util(self.btn_no)

  def no_btn_util(self):
    print('no_btn_util')
    self.parent.remove_widget(self)

  def yes_btn_util(self):
    #make payload dictionary with user_id and activity id integers
    print('yes_btn_util::::')
    payload = {}
    payload['user_id'] = self.table_box.user_id
    if self.delete_btn.name[:13] == 'User Activity':
      payload['activity_id'] = int(self.delete_btn.name[13:])
      act_type = self.delete_btn.name[:13]
    elif self.delete_btn.name[:5] == 'Polar':
      payload['activity_id'] = int(self.delete_btn.name[5:])
      act_type = self.delete_btn.name[:5]
    elif self.delete_btn.name[:10] == 'Oura Sleep':
      payload['oura_sleep_description_id'] = int(self.delete_btn.name[10:])
      act_type = self.delete_btn.name[:10]


    delete_row_util(act_type, payload, self.table_box.login_token)

    counter = 0
    # remove the boxrow with the
    for key, rowbox in self.table_box.rowbox_dict.items():
      counter += 1
      if rowbox.btn_delete_rb.name == self.delete_btn.name:
        self.table_box.grid_table.remove_widget(rowbox)
        key_to_delete = key
        break

    print('counter:::', counter)
    self.table_box.row_data_list = table_api_util(self.table_box.login_token)
    del self.table_box.rowbox_dict[key_to_delete]
    self.table_box.label_act_count.text = f'Activites count: {len(self.table_box.rowbox_dict)}'



    self.parent.remove_widget(self)


  def text_fitter_util(self, thing):
    if thing.texture_size[0] > thing.width * .7 and \
      thing.texture_size[1] < thing.height * .25 and \
      thing.text.find(" ", len('Are you sure you want to delete')) > 0:
      space_character = thing.text.find(" ", len('Are you sure you want to delete'))
      new_string_list = list(thing.text)
      new_string_list[space_character]="\n"
      thing.text=''.join(new_string_list)
      thing.halign ='center'
      thing.texture_update()

    while thing.texture_size[0] < thing.width * .8 and \
      thing.texture_size[1] < thing.height * .8:
      thing.font_size+=1
      thing.texture_update()

    return thing.font_size


  def text_fitter_button_util(self,thing):
    while thing.texture_size[0] < thing.width * .5 and \
      thing.texture_size[1] < thing.height * .5:
      thing.font_size+=1
      thing.texture_update()

    return thing.font_size



class ConfirmBox(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  on_size_count=ObjectProperty(0)
  # delete_btn=ObjectProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('****** ConfirmBox __init__')
    self.on_size_count=0

  def on_size(self, *args):
    print('******  ConfirmBox on_size')
    if self.on_size_count == 1:
      Clock.schedule_once(self.get_size, .01)
    self.on_size_count += 1

  def get_size(self, *args):
    print('ConfirmBox get_size')
    self.main_box = self.parent.children[1].children[0].children[1]
    self.ps1_base_width = self.main_box.ps1_base_width
    self.ps1_base_height = self.main_box.ps1_base_height
    self.pos_hint ={"center_x":.5,"center_y":.5}
    self.label_title.text = "Activity succussfully added!"
    text_fitter_label_util(self.label_title)
    text_fitter_button_util(self.btn_ok)

  def ok_btn_util(self):
    print('ok_btn_util')
    self.main_box.reset_screen()
    self.parent.remove_widget(self)

  #
  #
  # def text_fitter_label_util(self, thing):
  #   while thing.texture_size[0] < thing.width * .6 and \
  #     thing.texture_size[1] < thing.height * .6:
  #     thing.font_size+=1
  #     thing.texture_update()
  #
  #   return thing.font_size
  #
  #
  # def text_fitter_button_util(self, thing):
  #   while thing.texture_size[0] < thing.width * .4 and \
  #     thing.texture_size[1] < thing.height * .4:
  #     thing.font_size+=1
  #     thing.texture_update()
  #
  #   return thing.font_size




class FailBox(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  on_size_count=ObjectProperty(0)
  response_status=StringProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('****** FailBox __init__')
    self.on_size_count=0

  def on_size(self, *args):
    print('******  FailBox on_size')
    if self.on_size_count == 1:
      Clock.schedule_once(self.get_size, .01)
    self.on_size_count += 1

  def get_size(self, *args):
    print('FailBox get_size')
    self.main_box = self.parent.children[1].children[0].children[1]
    self.ps1_base_width = self.main_box.ps1_base_width
    self.ps1_base_height = self.main_box.ps1_base_height
    self.pos_hint ={"center_x":.5,"center_y":.5}
    if self.response_status == '401':
      self.label_title.text = "Looks like you got logged out.\nTry closing and reopening the app."
    else:
      self.label_title.text = "Something went wrong. Try again later\nor contact nick@dashanddata.com."
    text_fitter_label_util(self.label_title)
    text_fitter_button_util(self.btn_ok)

  def ok_btn_util(self):
    print('ok_btn_util')
    self.main_box.reset_screen()
    self.parent.remove_widget(self)


class FailBoxLogin(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  on_size_count=ObjectProperty(0)
  response_status=StringProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('****** FailBox __init__')
    self.on_size_count=0

  def on_size(self, *args):
    print('******  FailBox on_size')
    if self.on_size_count == 1:
      Clock.schedule_once(self.get_size, .01)
    self.on_size_count += 1

  def get_size(self, *args):
    print('FailBox get_size')
    # self.main_box = self.parent.children[1].children[0].children[1]
    print('self.parent:', self.parent)
    self.ps1_base_width = self.parent.width
    self.ps1_base_height = self.parent.height
    self.pos_hint ={"center_x":.5,"center_y":.5}
    if self.response_status == '401':
      self.label_title.text = "Wrong Email or Password."
    else:
      self.label_title.text = "Something went wrong. Try again later\nor contact nick@dashanddata.com."
    text_fitter_label_util(self.label_title)
    text_fitter_button_util(self.btn_ok)

  def ok_btn_util(self):
    print('ok_btn_util')
    # self.main_box.reset_screen()
    self.parent.remove_widget(self)
