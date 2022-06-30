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
    # self.test_counter=0
    # self.min_font_size = 0
    self.max_font_size = 0
    self.id_sort_counter = 0
    self.date_sort_counter = 0
    self.name_sort_counter = 0
    self.act_count_counter = 0

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

  # Table Contents I ##################################################
    self.build_rows_util()

  #Nav Buttons I
    self.label_table_nav.size_hint = (None,None)
    self.label_table_nav.font_size = self.ps1_base_width * .05###

    self.btn_top.size_hint_y = None
    self.btn_bottom.size_hint_y = None

    self.btn_top.font_size = self.ps1_base_width * .06###
    self.btn_bottom.font_size = self.ps1_base_width * .06###

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
    self.box_header_width = .975###
    self.btn_header_id.width = self.ps1_base_width * (self.box_header_width * .2)
    self.btn_header_date.width = self.ps1_base_width * (self.box_header_width * .25)
    self.btn_header_name.width = self.ps1_base_width * (self.box_header_width * .4)
    self.btn_header_count.width = self.ps1_base_width * (self.box_header_width * .15)

    #text_fitter_util shrinks the font_size to fit the button
    self.btn_header_count.font_size = self.ps1_base_width * .07# this is the longest text
    self.text_fitter_util()
    self.btn_header_id.font_size = self.btn_header_font_size
    self.btn_header_date.font_size = self.btn_header_font_size
    self.btn_header_name.font_size = self.btn_header_font_size

  # Assign sorting Buttons
    self.btn_header_id.bind(on_press=self.sort_by_util)
    self.btn_header_date.bind(on_press=self.sort_by_util)
    self.btn_header_name.bind(on_press=self.sort_by_util)
    self.btn_header_count.bind(on_press=self.act_count_util)



    self.box_header.size_hint_x = None
    self.box_header.width = self.ps1_base_width * self.box_header_width

    self.anchor_header.anchor_x = 'center'

  # Max height of all the header box items
    self.box_table_base.height = self.btn_header_id.height
  # Header background_color black
    with self.anchor_header.canvas.before:
      Color(.02,.02,.02)
      Rectangle(pos=self.anchor_header.pos,size=self.anchor_header.size)
    # with self.box_header.canvas.before:
    #   Color(.1, .1, .1, 1)
    #   Rectangle(pos=(self.box_header.pos[0],self.box_header.pos[1]-4), size=(self.ps1_base_width,6))

  # Table Content II
    self.grid_table.padding = (self.ps1_base_width * .0118,0,0,0)
    self.size_content_util()


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

    # self.btn_top.height = self.btn_top.texture_size[1]
    # self.btn_bottom.height = self.btn_bottom.texture_size[1]
    self.btn_top.height = self.ps1_base_height * .07
    self.btn_bottom_height = self.ps1_base_height * .07
    self.box_table_nav.height = self.anchor_table_nav_label.height + \
      self.btn_top.height + self.btn_bottom.height

  # box_table_base height
    self.box_table_base.size_hint_y =None
    self.box_table_base.height = self.height - (self.anchor_email_ts.height + \
      self.anchor_act_count.height + self.box_table_nav.height)

    Clock.schedule_once(self.make_frame, .01)

  def make_frame(self,*args):
    # print('self.scroll_view.x;::', self.scroll_view.x)
    with self.scroll_view.canvas.before:
      Color(.3,.3,.3)
      Rectangle(pos=(self.scroll_view.x,self.scroll_view.y),
        size=(self.ps1_base_width * .014,self.scroll_view.height))###
      Rectangle(pos=(self.scroll_view.right-(self.ps1_base_width * .014),self.scroll_view.y),
        size=(self.ps1_base_width * .014,self.scroll_view.height))###
      # print("executed shape")

  def build_rows_util(self):
    self.rowbox_dict={}

    if self.act_count_counter == 0:
      row_data = self.row_data_list[-20:]
    else:
      self.grid_table.clear_widgets()
      row_data = self.row_data_filtered

    for i in row_data:
      rowbox = RowBox()
      rowbox.size_hint_y=None
      rowbox.height = self.ps1_base_height * size_dict['rowbox']['height'][self.sc]

      rowbox.btn_id_rb.text=i[0]
      rowbox.label_date_rb.text=i[1]
      rowbox.label_name_rb.text=i[2]
      rowbox.btn_delete_rb.name=i[0]
      rowbox.btn_delete_rb.text='delete'
      rowbox.btn_delete_rb.bind(on_press=self.delete_row)

      self.rowbox_dict[i[0]]=rowbox
      self.grid_table.add_widget(rowbox)

    self.label_act_count.text = f"Activities Count: {len(self.rowbox_dict)}"



  def sort_by_util(self, widget):
    print('widget:', widget.text)
    print('widget.background_color:::', widget.background_color)

    self.grid_table.clear_widgets()
    self.rowbox_dict={}

    row_data = self.row_data_filtered

    if widget.text[:2]=='ID':

      if self.id_sort_counter % 3 == 0:# ascending
        widget.background_color = (.45,.55,.8,1)
        widget.text = 'ID\nascending'
        widget.halign = 'center'
        row_data.sort(key=lambda k: k[0])
      elif self.id_sort_counter % 3 == 1:# descending
        widget.background_color = (.45,.55,.8,1)
        widget.text = 'ID\ndescending'
        widget.halign = 'center'
        row_data.sort(key=lambda k: k[0], reverse = True)
      elif self.id_sort_counter % 3 == 2:# no sort
        widget.background_color = (1,1,1,1)
        widget.text = 'ID'
        row_data.sort(key=lambda k: k[4])
      #### Clear other buttons
      self.btn_header_date.background_color = (1,1,1,1)
      self.btn_header_date.text = 'Date/Time'
      self.btn_header_name.background_color = (1,1,1,1)
      self.btn_header_name.text = 'Acitivity Name'
      self.name_sort_counter=0
      self.date_sort_counter = 0
      self.id_sort_counter += 1

    elif widget.text[:2]=='Da':

      if self.date_sort_counter % 3 == 0:# ascending
        widget.background_color = (.45,.55,.8,1)
        widget.text = 'Date\Time\nascending'
        widget.halign = 'center'
        row_data.sort(key=lambda k: k[3])
      elif self.date_sort_counter % 3 == 1:# descending
        widget.background_color = (.45,.55,.8,1)
        widget.text = 'Date\Time\ndescending'
        widget.halign = 'center'
        row_data.sort(key=lambda k: k[3], reverse = True)
      elif self.date_sort_counter % 3 == 2:# no sort
        widget.background_color = (1,1,1,1)
        widget.text = 'Date\Time'
        row_data.sort(key=lambda k: k[4])
      #### Clear other buttons
      self.btn_header_id.background_color = (1,1,1,1)
      self.btn_header_id.text = 'ID'
      self.btn_header_name.background_color = (1,1,1,1)
      self.btn_header_name.text = 'Acitivity Name'
      self.name_sort_counter=0
      self.id_sort_counter = 0

      self.date_sort_counter += 1

    elif widget.text[:2]=='Ac':

      if self.name_sort_counter % 3 == 0:# ascending
        widget.background_color = (.45,.55,.8,1)
        widget.text = 'Activity Name\nascending'
        widget.halign = 'center'
        row_data.sort(key=lambda k: k[3])
      elif self.name_sort_counter % 3 == 1:# descending
        widget.background_color = (.45,.55,.8,1)
        widget.text = 'Activity Name\ndescending'
        widget.halign = 'center'
        row_data.sort(key=lambda k: k[3], reverse = True)
      elif self.name_sort_counter % 3 == 2:# no sort
        widget.background_color = (1,1,1,1)
        widget.text = 'Activity Name'
        row_data.sort(key=lambda k: k[4])
      #### Clear other buttons
      self.btn_header_id.background_color = (1,1,1,1)
      self.btn_header_id.text = 'ID'
      self.btn_header_date.background_color = (1,1,1,1)
      self.btn_header_date.text = 'Date/Time'
      self.date_sort_counter=0
      self.id_sort_counter = 0

      self.name_sort_counter += 1

    for i in row_data:
      rowbox = RowBox()
      rowbox.size_hint_y=None
      rowbox.height = self.ps1_base_height * size_dict['rowbox']['height'][self.sc]

      rowbox.btn_id_rb.text=i[0]
      rowbox.label_date_rb.text=i[1]
      rowbox.label_name_rb.text=i[2]
      rowbox.btn_delete_rb.name=i[0]
      rowbox.btn_delete_rb.text='delete'
      rowbox.btn_delete_rb.bind(on_press=self.delete_row)

      self.rowbox_dict[i[0]]=rowbox
      self.grid_table.add_widget(rowbox)

    self.label_act_count.text = f"Activities Count: {len(self.rowbox_dict)}"
    self.size_content_util()


  def size_content_util(self):
    for counter, (i,rowbox) in enumerate(self.rowbox_dict.items()):
      # -> Needs to be in size_dict <-

      rowbox.btn_id_rb.size_hint = None, None
      rowbox.label_date_rb.size_hint = None, None
      rowbox.label_name_rb.size_hint = None, None
      rowbox.btn_delete_rb.size_hint = None, None

      rowbox.btn_id_rb.width=self.ps1_base_width * (self.box_header_width * .2)
      rowbox.label_date_rb.width = self.ps1_base_width * (self.box_header_width * .25)
      rowbox.label_name_rb.width = self.ps1_base_width * (self.box_header_width * .4)
      rowbox.btn_delete_rb.width = self.ps1_base_width * (self.box_header_width * .15)

      rowbox.btn_id_rb.height = self.ps1_base_height * size_dict['rowbox']['height'][self.sc]
      rowbox.label_date_rb.height = self.ps1_base_height * size_dict['rowbox']['height'][self.sc]
      rowbox.label_name_rb.height = self.ps1_base_height * size_dict['rowbox']['height'][self.sc]
      rowbox.btn_delete_rb.height = self.ps1_base_height * size_dict['rowbox']['height'][self.sc]

      rowbox.height = self.ps1_base_height * size_dict['rowbox']['height'][self.sc]

      self.text_fitter_content_util(rowbox.btn_id_rb)
      self.text_fitter_content_util(rowbox.label_date_rb)
      self.text_fitter_content_util(rowbox.label_name_rb)
      self.text_fitter_content_util(rowbox.btn_delete_rb)

      rowbox_padding = self.ps1_base_width * ((1 - self.box_header_width)/2)
      # with rowbox.canvas.before:
      #   Color(.1, .1, .4, 1)
      #   Rectangle(pos=(rowbox.pos[0]+rowbox_padding,rowbox.pos[1]), size=(self.ps1_base_width * self.box_header_width,3))


  def act_count_util(self, widget):
    print('self.act_count_counter:::', self.act_count_counter)
    self.act_count_counter += 1
    if self.act_count_counter % 3 == 0:
      self.row_data_filtered = self.row_data_list[-20:]
    elif self.act_count_counter % 3 ==1:
      self.row_data_filtered = self.row_data_list[-50:]
    elif self.act_count_counter % 3 ==2:
      self.row_darta_filtered = self.row_data_list

    self.label_act_count.text = f'Activities Count: {len(self.row_data_filtered)}'

    self.build_rows_util()

  def delete_row(self, widget):
    print('delte row')
    print('widget:', widget.name)


  def text_fitter_util(self):
    # this utility shrinks btn_header_count text until it fits with a 5% buffer
    # uses that font_size on the other buttons
    while self.btn_header_count.texture_size[0]>(self.btn_header_count.width-(self.btn_header_count.width*.05)):
      self.btn_header_count.font_size-=1
      self.btn_header_count.texture_update()
    self.btn_header_font_size = self.btn_header_count.font_size


  def text_fitter_content_util(self, thing):
    # # is there room for two lines in button / label ---> if yes split into rows:

    if thing.text.find(" ", round(len(thing.text)/2)) > 0 and thing.text.find("\n")==-1 :
      space_character = thing.text.find(" ", round(len(thing.text)/2))
      new_string_list = list(thing.text)
      new_string_list[space_character]="\n"
      thing.text=''.join(new_string_list)
      thing.halign ='center'
      thing.texture_update()

    if self.max_font_size ==0:
      while thing.texture_size[1] < thing.height *.8 and \
        thing.texture_size[0] < thing.width * .8:
        thing.font_size += .5
        thing.texture_update()

      while thing.texture_size[0] > thing.width * .8 or \
        thing.texture_size[1] > thing.height * .8:
        thing.font_size -= .5
        thing.texture_update()

    else:
      while thing.texture_size[1] < thing.height *.8 and \
        thing.texture_size[0] < thing.width * .8 and \
        thing.font_size < self.max_font_size:
        thing.font_size += .5
        thing.texture_update()

      while thing.texture_size[0] > thing.width * .8 or \
        thing.texture_size[1] > thing.height * .8 or \
        thing.font_size > self.max_font_size:
        thing.font_size -= .5
        thing.texture_update()

    if self.max_font_size == 0:
      self.max_font_size = thing.font_size * 1.5
