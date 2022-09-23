from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

import time

filename = ''
screenfour = ''

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("Main.kv")
Builder.load_file("Cam.kv")
Builder.load_file("Result.kv")

# Declare both screens



class MenuScreen(Screen):
    pass

class CameraClick(Screen):

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        photo = camera.export_to_png("IMG_{}.png".format(timestr))
        global filename, screenfour
        filename = "IMG_{}.png".format(timestr)
        screenfour.update()

class ResultPage(Screen):
    def __init__(self, **kwargs):
        super(ResultPage, self).__init__(**kwargs)
        global screenfour
        screenfour = self

    def update(self, *args):
        global filename
        imageWidget = self.ids['imageWid']
        imageWidget.source = filename

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='Menu'))
        sm.add_widget(CameraClick(name='Camera'))
        sm.add_widget(ResultPage(name='Result'))

        return sm

if __name__ == '__main__':
    TestApp().run()