import subprocess
import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class NewsSmokeTests(unittest.TestCase):
    def test_scroll_down(self):
        # given I install and open the app
        set_up()
        self.wait_for_element_by_id('cardView')

        # then I see some news cards
        titles_before_scroll = self.titles()
        assert len(titles_before_scroll) > 0

        # when I scroll down
        self.scroll_down()


        # then I should see another news cards
        titles_after_scroll = self.titles()
        assert len(titles_after_scroll) > 0
        assert titles_before_scroll != titles_after_scroll

        tear_down()


    def wait_for_element_by_id(self, id):
        WebDriverWait(driver(), 10).until(
        EC.presence_of_element_located((By.ID, id))
        )

    def titles(self):
        titles = []

        for el in driver().find_elements_by_id('titleText'):
            titles.append(el.get_attribute('text'))
        return titles

    def scroll_down(self):
        width = driver().get_window_size()['width']
        height = driver().get_window_size()['height']

        driver().swipe(width*0.5, height*0.7, width*0.5, height*0.3, 400)
