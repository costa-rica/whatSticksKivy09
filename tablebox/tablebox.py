from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from size_dict import size_dict
from kivy.clock import Clock
from kivy.uix.button import Button

from kivy.graphics import Color, Rectangle
import time

Builder.load_file('tablebox/tablebox.kv')


class RowBox(BoxLayout):...


class TableBox(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  # toolbar_height=ObjectProperty(0)

  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('TableBox __init__')
    self.on_size_count=0
    self.sc = 2 # size coeffcient
    self.test_counter=0

  def on_size(self,*args):
    print('****   TableBox on_size: ', self.on_size_count)
    if self.on_size_count == 2:
      self.label_email_ts.text = "nickapeed@yahoo.com"

      self.label_act_count.text = "Activities Count: **"

      self.btn_header_id.text = "ID"
      self.btn_header_date.text = "Date/Time"
      self.btn_header_name.text = "Activity Name"
      self.btn_header_count.text = "Rows in Table"

      self.label_table_nav.text = "Jump to ..."
      self.btn_top.text = "Top"
      self.btn_bottom.text= "Bottom"
      self.size_kids()

    self.on_size_count += 1

  def size_kids(self,*args):
    # self.input_act_note.sc=self.sc
    print('-- TableBox size_kids --')

  #  Email Screen Name I
    self.label_email_ts.size_hint=(None,None)
    self.label_email_ts.font_size=self.ps1_base_width * size_dict['label_email']['font_size'][self.sc]

    self.anchor_email_ts.anchor_x="right"
    self.anchor_email_ts.size_hint_y=None

  # Activities Count I
    self.label_act_count.size_hint=(None,None)
    self.label_act_count.font_size=self.ps1_base_width * size_dict['label_email']['font_size'][1]

    self.anchor_act_count.anchor_x="left"
    self.anchor_act_count.anchor_y="bottom"
    self.anchor_act_count.size_hint_y=None

  # Table Header I
    self.btn_header_id.font_size = self.ps1_base_width * size_dict['label_email']['font_size'][2]
    self.btn_header_date.font_size = self.ps1_base_width * size_dict['label_email']['font_size'][2]
    self.btn_header_name.font_size = self.ps1_base_width * size_dict['label_email']['font_size'][2]
    self.btn_header_count.font_size = self.ps1_base_width * size_dict['label_email']['font_size'][2]

    self.btn_header_id.size_hint = (None,None)
    self.btn_header_date.size_hint = (None,None)
    self.btn_header_name.size_hint = (None,None)
    self.btn_header_count.size_hint = (None,None)

  # Table Contents I
    self.build_rows_util()

  #Nav Buttons I
    self.label_table_nav.size_hint = (None,None)
    self.label_table_nav.font_size = self.ps1_base_width * .03

    self.btn_top.size_hint_y = None
    self.btn_bottom.size_hint_y = None

    self.btn_top.font_size = self.ps1_base_width * .04
    self.btn_bottom.font_size = self.ps1_base_width * .04

    Clock.schedule_once(self.get_size, .01)


  def get_size(self,*args):
    print('-- TableBox get_size --')

  # Email Screen Name II
    self.label_email_ts.size= self.label_email_ts.texture_size
    self.anchor_email_ts.padding=(0,self.ps1_base_height * size_dict['anchor_email']['padding-top'][self.sc],
      self.ps1_base_width * size_dict['anchor_email']['padding-right'][self.sc],0)
    self.anchor_email_ts.height=self.label_email_ts.height + self.ps1_base_height * size_dict['anchor_email']['padding-top'][self.sc]

  # Activities Count II
    self.label_act_count.size=self.label_act_count.texture_size
    self.anchor_act_count.padding=(
      self.ps1_base_width * .01,
      self.ps1_base_height * .01,
      0,0)
    self.anchor_act_count.height=self.label_act_count.height + self.ps1_base_height * .01

  # Table Headers II
    self.btn_header_id.size = self.btn_header_id.texture_size
    self.btn_header_date.size = self.btn_header_date.texture_size
    self.btn_header_name.size = self.btn_header_name.texture_size
    self.btn_header_count.size = self.btn_header_count.texture_size

    self.btn_header_id.width = self.ps1_base_width * .25
    self.btn_header_date.width = self.ps1_base_width * .25
    self.btn_header_name.width = self.ps1_base_width * .25
    self.btn_header_count.width = self.ps1_base_width * .25

    # -> Needs to be in size_dict <-
    self.btn_header_id.font_size = self.ps1_base_width * .03
    self.btn_header_date.font_size = self.ps1_base_width * .03
    self.btn_header_name.font_size = self.ps1_base_width * .03
    self.btn_header_count.font_size = self.ps1_base_width * .03

    self.box_table_base.height = self.btn_header_id.height


  # Table Content II
    for i,rowbox in self.rowbox_dict.items():
      # -> Needs to be in size_dict <-
      rowbox.btn_id_rb.font_size = self.ps1_base_width * .02
      rowbox.label_date_rb.font_size = self.ps1_base_width * .02
      rowbox.label_name_rb.font_size = self.ps1_base_width * .02
      rowbox.btn_delete_rb.font_size = self.ps1_base_width * .02


  #Nav buttons II
    # self.label_table_nav.height = self.label_table_nav.texture_size[1]
    self.label_table_nav.size = self.label_table_nav.texture_size
    self.anchor_table_nav_label.anchor_x = "left"
    self.anchor_table_nav_label.anchor_y = "bottom"
    self.anchor_table_nav_label.size_hint_y = None
    self.anchor_table_nav_label.height = self.label_table_nav.height + self.ps1_base_height * .01
    self.anchor_table_nav_label.padding =(
      self.ps1_base_width * .01,
      self.ps1_base_height * .01,
      0,0)

    self.btn_top.height = self.btn_top.texture_size[1]
    self.btn_bottom.height = self.btn_bottom.texture_size[1]

  # box_tabel_base height
    self.box_table_base.size_hint_y =None
    # self.box_table_base.height = self.scroll_view.height + self.box_header.height
    self.box_table_base.height = self.ps1_base_height - (self.anchor_email_ts.height + \
      self.anchor_act_count.height + self.box_table_nav.height)


  def build_rows_util(self):
    self.rowbox_dict={}
    for i in self.row_data_list[0:30]:
      rowbox = RowBox()
      rowbox.btn_id_rb.text=i[0]
      rowbox.label_date_rb.text=i[1]
      rowbox.label_name_rb.text=i[2]
      rowbox.btn_delete_rb.name=i[3]
      rowbox.btn_delete_rb.text='delete'
      self.rowbox_dict[i[0]]=rowbox
      self.grid_table.add_widget(rowbox)

    self.label_act_count.text = f"Activities Count: {len(self.rowbox_dict)}"


class CountButton(Button):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('CountButton __init__')
