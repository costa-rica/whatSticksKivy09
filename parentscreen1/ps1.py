from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors.touchripple import TouchRippleBehavior
from areyousure.areyousure import ModalNoResponse

from size_dict import size_dict

import requests
import json
import webbrowser

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
    self.bind(size=self.size_kids)
    self.call_count=0


  def size_kids(self,*args):
    print('ParentScreen1 size_widgets')

    if self.call_count >0:
      self.ps1_base_width=self.width
      self.ps1_base_height=self.height

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

      self.label_register.font_size = self.ps1_base_width * size_dict['btn_exit']['font_size'][2] *.75

      Clock.schedule_once(self.size_kids_2)
    self.call_count+=1

  def size_kids_2(self,*args):
    #set size of image
    self.image_wsh.size_hint = (None,None)
    self.image_wsh.size = self.image_wsh.texture_size

    Clock.schedule_once(self.size_image,.01)

    # set size of label
    self.label_app_name.size_hint_x = None
    self.label_app_name.width = self.label_app_name.texture_size[0]

    self.box_app_name.size_hint_x = None
    self.box_app_name.width = self.label_app_name.width + self.image_wsh.width

#### REMOVE before publishing ###
    # self.md_txt_field_email.text = 'nickapeed@yahoo.com'
    # self.md_txt_field_password.text = 


  def verify_user(self):
    base_url = 'https://api.what-sticks-health.com'
    self.response_login = requests.request('GET',base_url + '/login',
        auth=(self.md_txt_field_email.text,self.md_txt_field_password.text))

    if self.response_login.status_code ==200:
      login_token = json.loads(self.response_login.content.decode('utf-8'))['token']

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
    elif self.response_login.status_code == 401:
      self.failboxlogin = ModalNoResponse(line_color = (.5,.3,.3),
      message = "Wrong Email or Password.")
      self.add_widget(self.failboxlogin)
    else:
      message = f"Something went wrong.\nTry again later or contact\nnick@dashanddata.com.\nstatus code:{self.response_login.status_code}"
      self.failboxlogin = ModalNoResponse(line_color = (.5,.3,.3), message = message)
      self.add_widget(self.failboxlogin)

  def show_password(self,toggle_widget):
    if toggle_widget.state=='down':
      self.show_password_toggle.text="Hide password"
      self.md_txt_field_password.password=False
    else:
      self.show_password_toggle.text="Show password"
      self.md_txt_field_password.password = True

  def size_image(self,*args):
    self.image_wsh.texture_update()
    while self.image_wsh.size[1] > self.label_app_name.height * .5 and \
      self.image_wsh.height > 2 :
      self.image_wsh.size[1] -= .25
      self.image_wsh.texture_update()


class ShowPasswordToggle(MDFillRoundFlatButton, MDToggleButton): ...


class RegisterLabel(ButtonBehavior, Label):
  def on_press(self):
    webbrowser.open('https://what-sticks-health.com/register')


class AnchorClickable_login(TouchRippleBehavior, ButtonBehavior, AnchorLayout):
  def __init__(self, **kwargs):
    super(AnchorClickable_login, self).__init__(**kwargs)

  def on_touch_down(self, touch):
    collide_point = self.collide_point(touch.x, touch.y)
    if collide_point:
      touch.grab(self)
      self.ripple_duration_in = 0.7
      self.ripple_scale = 0.1
      self.ripple_show(touch)
      print('Login on_touch_down')
      Clock.schedule_once(self.open_site,1)
      # webbrowser.open('https://what-sticks-health.com/register')
      return True
    return False

  def on_touch_up(self, touch):
    if touch.grab_current is self:
      touch.ungrab(self)
      self.ripple_duration_out = 0.4
      self.ripple_fade()
      return True
    return False


  def open_site(self, *args):
    webbrowser.open('https://what-sticks-health.com/register')
