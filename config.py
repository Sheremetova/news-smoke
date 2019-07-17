import os
import pytest

from collections import defaultdict
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def set_up():
    desired_capabilities = {
        'appPackage': 'my.deler.newstestapplication',
        'appActivity': 'my.deler.newstestapplication.screens.MainActivity',
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'Android Emulator',
        'app': PATH('apk/news.apk'),
        'noReset': True
        }

    pytest.globalDict = defaultdict() 
    pytest.globalDict['driver'] = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

def driver():
    return pytest.globalDict['driver']

def tear_down():
    # stop session
    driver().quit()
