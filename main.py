#! -*- coding:utf-8 -*-
from airtest.core.android.adb import ADB
from airtest.core.api import connect_device
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class App(App):

    def build(self):
        return First_test(padding = 20, orientation = "vertical", spacing = 30)

class First_test(BoxLayout):

    def __init__(self, **kwargs):
        super(First_test, self).__init__(**kwargs)
        devices = ADB().devices()
        serial = devices[0][0]
        DEVICE_URL = "android:///{serial}".format(serial = serial)
        self.device = connect_device(DEVICE_URL)
        self.start_app()

    def start_app(self):
        package_name = 'com.ss.android.ugc.aweme'
        activity_name = 'com.ss.android.ugc.aweme.splash.SplashActivity'
        self.device.shell("am start %s/%s" %(package_name, activity_name))

if __name__ == '__main__':

    App().run()
