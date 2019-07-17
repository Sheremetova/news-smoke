import os
import pytest

from collections import defaultdict
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class App:
    @classmethod
    def set_up(cls):
        desired_capabilities = {
                'appPackage': 'my.deler.newstestapplication',
                'appActivity': 'my.deler.newstestapplication.screens.MainActivity',
                'platformName': 'Android',
                'platformVersion': '7.0', # change in accordance with a connected device
                'deviceName': 'Android Emulator',
                'app': PATH('apk/news.apk'),
                'noReset': True
                }

        cls._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    @classmethod
    def driver(cls):
        return cls._driver

    @classmethod
    def driver_exist(cls):
        try:
            cls._driver
        except AttributeError:
            return False
        return True

    @classmethod
    def tear_down(cls):
        # stop session
        cls._driver.quit()
