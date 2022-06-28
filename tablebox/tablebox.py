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
    print('-- TableBox size_kids --')

  #  Email / Screen Name I
    self.label_email_ts.size_hint=(None,None)
    self.label_email_ts.font_size=100
    self.label_email_ts.size = self.label_email_ts.texture_size

    self.anchor_email_ts.anchor_x="right"
    self.anchor_email_ts.anchor_y= "bottom"
    self.anchor_email_ts.size_hint_y=None
    self.anchor_email_ts.height = self.ps1_base_height * .05

  # Activities Count I
    self.label_act_count.size_hint=(None,None)
    self.label_act_count.font_size = 100
    self.label_act_count.size = self.label_act_count.texture_size

    self.anchor_act_count.anchor_x="left"
    self.anchor_act_count.anchor_y="bottom"
    self.anchor_act_count.size_hint_y=None
    self.anchor_act_count.height = self.ps1_base_height * .05

  # Table Header I (give oversized font_size - fitter will shrink later)
    self.btn_header_id.font_size = 100
    self.btn_header_date.font_size = 100
    self.btn_header_name.font_size = 100
    self.btn_header_count.font_size = 100

    self.btn_header_id.size_hint = (None,None)
    self.btn_header_date.size_hint = (None,None)
    self.btn_header_name.size_hint = (None,None)
    self.btn_header_count.size_hint = (None,None)

    self.box_header.size_hint_y = None
    self.box_header.height = self.ps1_base_height * .095###

    self.anchor_header.size_hint = (1,None)
    self.anchor_header.height = self.ps1_base_height * .1###

    self.btn_header_id.height = self.ps1_base_height * .095###
    self.btn_header_date.height = self.ps1_base_height * .095###
    self.btn_header_name.height = self.ps1_base_height * .095###
    self.btn_header_count.height = self.ps1_base_height * .095###



  # Table Contents I
    self.build_rows_util()

  #Nav Buttons I
    self.label_table_nav.size_hint = (None,None)
    self.label_table_nav.font_size = self.ps1_base_width * .03###

    self.btn_top.size_hint_y = None
    self.btn_bottom.size_hint_y = None

    self.btn_top.font_size = self.ps1_base_width * .04###
    self.btn_bottom.font_size = self.ps1_base_width * .04###

    Clock.schedule_once(self.get_size, .01)


  def get_size(self,*args):
    print('-- TableBox get_size --')

  # Email / Screen Name II
    while self.label_email_ts.texture_size[1] > (self.anchor_email_ts.height * .95) or \
      self.label_email_ts.texture_size[0] > (self.anchor_email_ts.width * .5):###
      self.label_email_ts.font_size-=1
      self.label_email_ts.texture_update()

    self.label_email_ts.size = self.label_email_ts.texture_size

  # Activities Count II
    while self.label_act_count.texture_size[1] > (self.anchor_act_count.height *.95) or \
      self.label_act_count.texture_size[0] > (self.anchor_act_count.width * .5):###
      self.label_act_count.font_size -= 1
      self.label_act_count.texture_update()

    self.label_act_count.size = self.label_act_count.texture_size


  # Table Headers II
    self.box_header_witdth = .975###
    self.btn_header_id.width = self.ps1_base_width * (self.box_header_witdth/4)
    self.btn_header_date.width = self.ps1_base_width * (self.box_header_witdth/4)
    self.btn_header_name.width = self.ps1_base_width * (self.box_header_witdth/4)
    self.btn_header_count.width = self.ps1_base_width * (self.box_header_witdth/4)

    #text_fitter_util shrinks the font_size to fit the button
    self.btn_header_count.font_size = self.ps1_base_width * .07# this is the longest text
    self.text_fitter_util()
    self.btn_header_id.font_size = self.btn_header_font_size
    self.btn_header_date.font_size = self.btn_header_font_size
    self.btn_header_name.font_size = self.btn_header_font_size

    self.box_header.size_hint_x = None
    self.box_header.width = self.ps1_base_width * self.box_header_witdth

    self.anchor_header.anchor_x = 'center'

    # Max height of all the header box items
    self.box_table_base.height = self.btn_header_id.height


  # Table Content II
    self.grid_table.padding = (self.ps1_base_width * .01,0,0,0)
    for i,rowbox in self.rowbox_dict.items():
      # -> Needs to be in size_dict <-
      rowbox.btn_id_rb.font_size = self.ps1_base_width * .02###
      rowbox.label_date_rb.font_size = self.ps1_base_width * .02###
      rowbox.label_name_rb.font_size = self.ps1_base_width * .02###
      rowbox.btn_delete_rb.font_size = self.ps1_base_width * .02###

      rowbox.btn_id_rb.size_hint_x = None
      rowbox.label_date_rb.size_hint_x = None
      rowbox.label_name_rb.size_hint_x = None
      rowbox.btn_delete_rb.size_hint_x = None

      rowbox.btn_id_rb.width=self.ps1_base_width * (self.box_header_witdth/4)
      rowbox.label_date_rb.width = self.ps1_base_width * (self.box_header_witdth/4)
      rowbox.label_name_rb.width = self.ps1_base_width * (self.box_header_witdth/4)
      rowbox.btn_delete_rb.width = self.ps1_base_width * (self.box_header_witdth/4)


  #Nav buttons II
    self.label_table_nav.size = self.label_table_nav.texture_size
    self.anchor_table_nav_label.anchor_x = "left"
    self.anchor_table_nav_label.anchor_y = "bottom"
    self.anchor_table_nav_label.size_hint_y = None
    self.anchor_table_nav_label.height = self.label_table_nav.height + self.ps1_base_height * .01
    self.anchor_table_nav_label.padding =(
      self.ps1_base_width * .01,
      self.ps1_base_height * .01,
      0,0)###

    self.btn_top.height = self.btn_top.texture_size[1]
    self.btn_bottom.height = self.btn_bottom.texture_size[1]
    self.box_table_nav.height = self.anchor_table_nav_label.height + \
      self.btn_top.height + self.btn_bottom.height

  # box_table_base height
    self.box_table_base.size_hint_y =None
    self.box_table_base.height = self.height - (self.anchor_email_ts.height + \
      self.anchor_act_count.height + self.box_table_nav.height)

    print('self.height:', self.height)
    print('self.ps1_base_height:', self.ps1_base_height)
    print('self.anchor_email_ts.height:',self.anchor_email_ts.height)
    print('self.anchor_act_count.height:', self.anchor_act_count.height)
    print('self.box_table_base.height:', self.box_table_base.height)
    print('self.box_table_nav.height:', self.box_table_nav.height)



    Clock.schedule_once(self.make_frame, .01)

  def make_frame(self,*args):
    print('self.scroll_view.x;::', self.scroll_view.x)
    with self.scroll_view.canvas.before:
      Color(.1,.1,.1)
      Rectangle(pos=(self.scroll_view.x,self.scroll_view.y),
        size=(self.ps1_base_width * .014,self.scroll_view.height))###
      Rectangle(pos=(self.scroll_view.right-(self.ps1_base_width * .014),self.scroll_view.y),
        size=(self.ps1_base_width * .014,self.scroll_view.height))###
      print("executed shape")

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


  def text_fitter_util(self):
    # this utility shrinks btn_header_count text until it fits with a 5% buffer
    # uses that font_size on the other buttons
    while self.btn_header_count.texture_size[0]>(self.btn_header_count.width-(self.btn_header_count.width*.05)):
      self.btn_header_count.font_size-=1
      self.btn_header_count.texture_update()
    self.btn_header_font_size = self.btn_header_count.font_size



class CountButton(Button):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('CountButton __init__')
