from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock

from size_dict import size_dict

from utils import add_activity_util

import datetime

Builder.load_file('mainbox/mainbox.kv')

class MainBoxLayout(BoxLayout):
  ps1_base_width = ObjectProperty(0)
  ps1_base_height = ObjectProperty(0)
  toolbar_height = ObjectProperty(0)
  label_email = ObjectProperty()

  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.on_size_count = 0
    self.sc = 2 # size coeffcient

  def on_size(self,*args):
    print('MainBoxLayout on_size')

    if self.on_size_count == 1:
      self.label_email.text = "nickapeed@yahoo.com"

      self.label_act_name.text = "Add Activity Name"
      self.label_act_note.text = "Add Activity Note"

      self.label_date.text = "Date"
      self.input_date.text = "6/20/2022"
      self.label_time.text = "Time"
      self.input_time.text = datetime.datetime.now().strftime("%-l:%M %p")

      self.btn_submit_act.text = "Submit Activity"

    self.on_size_count += 1

  def size_kids(self,*args):
    self.input_act_note.sc=self.sc

  # Act Screen Name / Email
    self.label_email.size_hint=(None,None)
    self.label_email.font_size=self.ps1_base_height * size_dict['label_email']['font_size'][self.sc]
    self.label_email.size= self.label_email.texture_size

    self.anchor_email.anchor_x="right"
    self.anchor_email.size_hint=(1,None)
    self.anchor_email.padding=(0,self.ps1_base_height * size_dict['anchor_email']['padding-top'][self.sc],
      self.ps1_base_width * size_dict['anchor_email']['padding-right'][self.sc],0)
    self.anchor_email.height=self.label_email.height + self.ps1_base_height * size_dict['anchor_email']['padding-top'][self.sc]

    Clock.schedule_once(self.get_size, .01)

  def get_size(self,*args):
    self.label_email.size= self.label_email.texture_size

  #Add Act Name
    self.label_act_name.size_hint=(None,None)
    self.label_act_name.font_size = self.ps1_base_width * size_dict['label_act_name']['font_size'][self.sc]
    self.anchor_email.size_hint_y=None
    Clock.schedule_once(self.get_size_2, .01)


  def get_size_2(self,*args):
    self.label_act_name.size = self.label_act_name.texture_size

    self.anchor_email.height=self.label_email.texture_size[1]

    self.input_act_name.font_size=self.ps1_base_width * size_dict['input_act_name']['font_size'][self.sc]
    self.input_act_name.height = self.label_act_name.height

    self.anchor_act_name_label.anchor_x="left"
    self.anchor_act_name_label.size_hint=(1,None)
    self.anchor_act_name_label.height=self.label_act_name.height

    self.box_act_name.size_hint=(1,None)
    self.box_act_name.height = self.anchor_act_name_label.height + self.input_act_name.height + \
      self.ps1_base_height * size_dict['box_act_name']['padding-top'][self.sc]
    self.box_act_name.padding =(self.ps1_base_width*size_dict['box_act_name']['padding-left'][self.sc],
      self.ps1_base_height * size_dict['box_act_name']['padding-top'][self.sc],
      self.ps1_base_width*size_dict['box_act_name']['padding-right'][self.sc],0)

  #Add Act Note
    self.label_act_note.size_hint=(None,None)
    self.label_act_note.font_size = self.ps1_base_width * size_dict['label_act_note']['font_size'][self.sc]
    Clock.schedule_once(self.get_size_3,.01)

  def get_size_3(self,*args):
    self.label_act_note.size=self.label_act_note.texture_size

    self.input_act_note.font_size=self.ps1_base_width * size_dict['input_act_note']['font_size'][self.sc]
    self.input_act_note.size_hint=(1,None)
    self.input_act_note.height=self.label_act_note.height *len(self.input_act_note._lines)

    self.anchor_act_note_label.anchor_x="left"
    self.anchor_act_note_label.size_hint=(1,None)
    self.anchor_act_note_label.height = self.label_act_note.height

    self.box_act_note.size_hint=(1,None)
    self.box_act_note.padding=(self.ps1_base_width*size_dict['box_act_note']['padding-left'][self.sc],
      self.ps1_base_height * size_dict['box_act_note']['padding-top'][self.sc],
      self.ps1_base_width*size_dict['box_act_note']['padding-right'][self.sc],0)

  #Add Date Time
    self.label_time.font_size = self.ps1_base_width * size_dict['label_time']['font_size'][self.sc]
    self.label_date.font_size = self.ps1_base_width * size_dict['label_date']['font_size'][self.sc]

    self.label_time.size_hint = (None,None)
    self.label_date.size_hint = (None,None)

    Clock.schedule_once(self.get_size_4,.01)

  def get_size_4(self,*args):
    self.label_date.size = self.label_date.texture_size
    self.label_time.size = self.label_time.texture_size

    self.input_time.font_size = self.ps1_base_width * size_dict['input_time']['font_size'][self.sc]
    self.input_date.font_size = self.ps1_base_width * size_dict['input_date']['font_size'][self.sc]
    self.input_time.size_hint=(1,None)
    self.input_date.size_hint=(1,None)

    self.input_time.height=self.label_time.height
    self.input_date.height=self.label_date.texture_size[1]

    Clock.schedule_once(self.get_size_5,.01)

  def get_size_5(self,*args):

    self.anchor_date_time.size_hint=(1,None)
    self.anchor_date_time.height = self.input_date.height + self.label_date.height + \
      self.ps1_base_height * size_dict['anchor_date_time']['padding-top'][self.sc]
    self.anchor_date_time.padding =(self.ps1_base_width * size_dict['anchor_date_time']['padding-left'][self.sc],
      self.ps1_base_height * size_dict['anchor_date_time']['padding-top'][self.sc],
      self.ps1_base_width * size_dict['anchor_date_time']['padding-right'][self.sc],0)

    self.btn_submit_act.font_size = self.ps1_base_width * size_dict['btn_submit_act']['font_size'][self.sc]

    self.anchor_submit.anchor_x = "right"
    self.anchor_submit.padding = (0,0,self.ps1_base_width * size_dict['anchor_submit']['padding-right'][self.sc],0)


  def add_activity(self):
    print(self.input_date.text)
    month,day,year = self.input_date.text.split('/')
    print('month,day,year::', month,day,year)
    # year = self.input_date.text[-4:]
    # month = self.input_date.text[]
    date_thing = f'{year}-{int(month):02d}-{int(day):02d}'
    time_thing = datetime.datetime.strptime(self.input_time.text, '%I:%M %p').time()
    # print(time_thing.time())
    # print(time_thing.ctime())
    # print(time_thing.dst())
    # print(time_thing.timestamp())
    # print(time_thing.timetuple())
    # print(time_thing.toordinal())
    # print(time_thing.fromisoformat())

    print(dir(time_thing))
    print('datetime_of_activity:::', date_thing +'T'+ str(time_thing))
    payload={}
    # payload['datetime_of_activity']='2022-05-21T15:31:00'
    payload['datetime_of_activity'] = date_thing +'T'+ str(time_thing)
    payload["note"]= self.input_act_note.text
    payload["source_name"]= "iOS Device App"
    # payload1["time_stamp_utc"]= "2021-08-29T14:04:07.567861"
    payload["user_id"]= 1
    payload["var_activity"]= self.input_act_name.text
    payload["time_offset"]= 120

    add_activity_util(payload, self.login_token)

class TextInputAddName(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    main_box =instance.parent.parent#different hiearchey than TextInputDynamicActNote
    if value:
      main_box.label_act_name.color=(0,0,0,1)
    else:
      main_box.label_act_name.color=(.3,.3,.3,1)


class TextInputDynamicActNote(TextInput):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.on_size_count=0
    self.old_line_count=1
    self.bind(_lines=self.change_height_util)
    self.sc=2

  def change_height_util(self,*args):
    self.main_box=self.parent.parent
    self.height=len(self._lines) * self.main_box.label_act_note.height
    self.main_box.box_act_note.height=self.main_box.input_act_note.height + self.main_box.anchor_act_note_label.height + \
      self.main_box.ps1_base_height * size_dict['box_act_note']['padding-top'][self.sc]

  def on_focus(self, instance_twice, value):
    self.main_box=self.parent.parent
    if value:
      self.main_box.label_act_note.color=(0,0,0,1)
    else:
      self.main_box.label_act_note.color=(.3,.3,.3,1)
