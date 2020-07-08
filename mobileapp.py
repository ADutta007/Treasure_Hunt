from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from plyer import storagepath

from for_kivy import MyKivyFile


class MainWindow(MDScreen):
    pass


class SecondWindow(MDScreen):
    pass


class ThirdWindow(MDScreen):
    pass


class WindowManager(ScreenManager):
    pass


class forkivymd(MDScreen):

    def vibrates(self):
        vibrator.pattern(0, 2)


class MyMainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_widget = Builder.load_string(MyKivyFile)

    def build(self):
        self.theme_cls.theme_style = "Dark"

        return self.root_widget


if __name__ == "__main__":
    MyMainApp().run()
