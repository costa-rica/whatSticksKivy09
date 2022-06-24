from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton
from kivy.uix.popup import Popup

# from mainbox.mainbox import CustomPopup

from size_dict import size_dict

import requests
import json

# from utils import text_size_coef_utility

Builder.load_file('parentscreen1/ps1.kv')


class ParentScreen1(Screen):
  md_txt_field_email=ObjectProperty()
  md_txt_field_password=ObjectProperty()
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  text_size_coef=ObjectProperty(.06)
  text_size_coef_sm=ObjectProperty(.04)

  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen1 __init__')
    self.bind(size=self.size_widgets)
    self.call_count=0


  def size_widgets(self,*args):
    print('ParentScreen1 size_widgets')
    if self.call_count >0:
      self.ps1_base_width=self.width
      self.ps1_base_height=self.height

      self.md_txt_field_email.text='nickapeed@yahoo.com'
      self.md_txt_field_password.text='test'

  #Size widgets based on size_dict parameters
      self.anchor_app_name.height = self.ps1_base_height * size_dict['anchor_app_name']['height'][2]
      self.label_app_name.font_size = self.ps1_base_width * size_dict['label_app_name']['font_size'][2]
      self.anchor_email_ps1.height = self.ps1_base_height * size_dict['anchor_email_ps1']['height'][2]

      self.anchor_email_ps1.padding = (self.ps1_base_width * size_dict['anchor_email_ps1']['padding-left'][2],0,
        self.ps1_base_width * size_dict['anchor_email_ps1']['padding-right'][2],0)


      self.md_txt_field_email.font_size = self.ps1_base_width * size_dict['md_txt_field_email']['font_size'][2]
      self.anchor_password.height = self.ps1_base_height * size_dict['anchor_password']['height'][2]
      self.anchor_password.padding = (self.ps1_base_width * size_dict['anchor_password']['padding-left'][2],0,
        self.ps1_base_width * size_dict['anchor_password']['padding-right'][2],0)
      self.md_txt_field_password.font_size = self.ps1_base_width * size_dict['md_txt_field_password']['font_size'][2]
      self.anchor_showpass.padding = (0,0,self.ps1_base_width * size_dict['anchor_showpass']['padding-right'][2],0)
      self.show_password_toggle.font_size = self.ps1_base_width * size_dict['show_password_toggle']['font_size'][2]
      self.anchor_login.padding = (0,0,self.ps1_base_width * size_dict['anchor_login']['padding-right'][2],0)
      self.btn_login.font_size = self.ps1_base_width * size_dict['btn_login']['font_size'][2]
      self.anchor_exit.padding = (0,0,self.ps1_base_width * size_dict['anchor_exit']['padding-right'][2],0)
      self.btn_exit.font_size = self.ps1_base_width * size_dict['btn_exit']['font_size'][2]

    self.call_count+=1


  def verify_user(self):
    base_url = 'https://api.what-sticks-health.com'
    response_login = requests.request('GET',base_url + '/login',
        auth=(self.md_txt_field_email.text,self.md_txt_field_password.text))
    print('response_login.status_code:::', response_login.status_code)
    if response_login.status_code ==200:
      login_token = json.loads(response_login.content.decode('utf-8'))['token']

      url_user_data = base_url + "/user_account_data"
      headers = {'x-access-token': login_token,'Content-Type': 'application/json'}
      response_user_data = requests.request("GET", url_user_data, headers=headers)
      user_data_dict = json.loads(response_user_data.text)

      self.parent.ps1_base_width=self.ps1_base_width
      self.parent.ps1_base_height=self.ps1_base_height

      self.parent.email = self.md_txt_field_email.text
      self.parent.login_token = login_token
      self.parent.id = user_data_dict['id']
      self.parent.username=user_data_dict['username']
      self.parent.user_timezone = user_data_dict['user_timezone']


      self.parent.current="parent_screen_2"
    else:
      custom_popup = CustomPopup(
        title="Login Unsuccessful",
        title_color=(250/255,160/255,127/255),
        separator_color=(250/255,160/255,127/255),
        title_size=self.width*.03
        )
      custom_popup.open()

  def show_password(self,toggle_widget):
    if toggle_widget.state=='down':
      self.show_password_toggle.text="Hide password"
      self.md_txt_field_password.password=False
    else:
      self.show_password_toggle.text="Show password"
      self.md_txt_field_password.password = True


class ShowPasswordToggle(MDFillRoundFlatButton, MDToggleButton):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.background_down = self.theme_cls.primary_light
