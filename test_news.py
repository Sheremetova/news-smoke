import os
import subprocess
import unittest

from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class NewsSmokeTests(unittest.TestCase):
    def set_up(self):
        desired_capabilities = {
            'appPackage': 'my.deler.newstestapplication',
            'appActivity': 'my.deler.newstestapplication.screens.MainActivity',
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'Android Emulator',
            'app': PATH('apk/news.apk'),
            'noReset': True
            }


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def tear_down(self):
        # stop session
        self.driver.quit()
