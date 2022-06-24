from kivymd.app import MDApp
from kivy.core.window import Window
from myscreencontroller import MyScreenController
import platform

if platform not in ['ios','android']:
  Window.size = (960, 1704)# iPhone 13 Mini
  print('Screen size set by application')

class MainApp(MDApp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.mycontroller=MyScreenController()

  def build(self):
    return self.mycontroller.get_screen()

if __name__=='__main__':
  MainApp().run()
