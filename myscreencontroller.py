from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
import parentscreen1.ps1
import parentscreen2.ps2

KV='''
<BaseScreenManger>:
  ps1:ps1
  ps2:ps2
  canvas.before:
    Color:
      rgb: [127/255,160/255,189/255]
    Rectangle:
      pos: self.pos
      size: self.size
  ParentScreen1:
    id:ps1
    name:"parent_screen_1"
  ParentScreen2:
    id:ps2
    name:"parent_screen_2"

'''

Builder.load_string(KV)


class BaseScreenManger(ScreenManager):
  controller = ObjectProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('BaseScreenManger __init__')
    self.bind(children=self.on_children)

  def on_children(self,*args):
    children_names_dict={i.name:i for i in self.children}
    if 'parent_screen_1' in children_names_dict.keys():
      self.ps1_base_height=children_names_dict['parent_screen_1'].height
      self.ps1_base_width=children_names_dict['parent_screen_1'].width
      print(self.ps1_base_height)



class MyScreenController():
  def __init__(self):
    self.view=BaseScreenManger(controller=self)
    print('MyScreenController __init__')

  def get_screen(self):
    return self.view
