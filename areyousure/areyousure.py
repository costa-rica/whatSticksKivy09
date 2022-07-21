from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from utils import delete_row_util
from kivy.uix.modalview import ModalView
# from kivy.uix.anchorlayout import AnchorLayout

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



class ModalNoResponse(ModalView):
  line_color = ColorProperty((.3,.5,.3))
  message = StringProperty('default message')
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.background_color = (.1,.1,.1,.9)#Modal covering background widget from previous screen

  def on_size(self, *args):
    self.label_title.text = "On_size"

    self.label_title.text = self.message

    Clock.schedule_once(self.text_fitter_util_increase, .01)

  def text_fitter_util_increase(self, thing):
    while self.label_title.texture_size[0] < self.box_popup.width * .9:
      self.label_title.font_size += .25
      self.label_title.halign ='center'
      self.label_title.texture_update()
    Clock.schedule_once(self.text_fitter_util_decrease, .01)


  def text_fitter_util_decrease(self, *args):
    while self.label_title.texture_size[0] > self.box_popup.width * .9:
      self.label_title.font_size -= .25
      self.label_title.halign ='center'
      self.label_title.texture_update()

  def on_touch_down(self, touch):
    print('touched Modal')

    if self.label_title.text[:8] == "Activity":
      activity_box = self.parent
      main_box = self.parent.children[1].children[0].children[1]
      main_box.reset_screen()

    self.parent.remove_widget(self)
    return super().on_touch_down(touch)



class ModalButtonResponse(ModalView):
  line_color = ColorProperty((.3,.5,.3))
  trigger_widget_name = StringProperty('delete')
  login_token = StringProperty()


  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.background_color = (.1,.1,.1,.9)#Modal covering background widget from previous screen

  def on_size(self, *args):
    self.label_title.text = f"Delete: {self.trigger_widget_name}\nAre you sure?"
    Clock.schedule_once(self.text_fitter_util_increase, .01)

  def text_fitter_util_increase(self, thing):
  # Title #
    while self.label_title.texture_size[0] < self.box_popup.width * .9 and \
      self.label_title.texture_size[1] < self.box_popup.height * .27:
      self.label_title.font_size += .25
      self.label_title.halign ='center'
      self.label_title.texture_update()

  # Yes button #
    while self.btn_yes.texture_size[0] < self.btn_yes.width * .7 and \
      self.btn_yes.texture_size[1] < self.btn_yes.height * .7:
      self.btn_yes.font_size += .25
      self.btn_yes.halign ='center'
      self.btn_yes.texture_update()

    Clock.schedule_once(self.text_fitter_util_decrease, .01)

  def text_fitter_util_decrease(self, *args):
    while self.label_title.texture_size[0] > self.box_popup.width * .9 or \
      self.label_title.texture_size[1] > self.box_popup.height * .27:
      self.label_title.font_size -= .25
      self.label_title.halign ='center'
      self.label_title.texture_update()

  # Yes button #
    while self.btn_yes.texture_size[0] > self.btn_yes.width * .7 or \
      self.btn_yes.texture_size[1] > self.btn_yes.height * .7:
      self.btn_yes.font_size -= .25
      self.btn_yes.halign ='center'
      self.btn_yes.texture_update()

  # No button #
    self.btn_no.font_size = self.btn_yes.font_size


  def no_btn_util(self):
    print('no_btn_util')
    self.parent.remove_widget(self)


  def yes_btn_util(self):
    print('self.parent:', self.parent)#TableScreen
    table_box = self.parent.children[1]
    delete_row_util(self.trigger_widget_name, self.login_token)
    table_box.delete_row_table_reload(self.trigger_widget_name)
    self.parent.remove_widget(self)


  def on_touch_down(self, touch):
    if not self.box_popup.collide_point(*touch.pos):
      print('touched Modal')

      self.parent.remove_widget(self)
    # if self.label_title.text[:8] == "Activity":
    #   activity_box = self.parent
    #   main_box = self.parent.children[1].children[0].children[1]
    #   main_box.reset_screen()

    # self.parent.remove_widget(self)
    return super().on_touch_down(touch)
