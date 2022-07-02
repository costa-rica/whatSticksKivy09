from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
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

from utils import delete_row_util

Builder.load_file('areyousure/areyousure.kv')


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
    # self.table_box.remove_areyousure_util()

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


    print(payload)
    print(act_type)
    # print(self.delete_btn.name)
    self.parent.remove_widget(self)
    delete_row_util(act_type, payload, self.table_box.login_token)


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
