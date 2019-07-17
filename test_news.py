import subprocess
import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import *
from page_objects.main_screen import MainScreen

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class NewsSmokeTests(unittest.TestCase):
    def test_scroll_down(self):
        # given I install and open the app
        set_up()
        MainScreen.wait_for_screen_active()

        # then I see some news cards
        titles_before_scroll = MainScreen.titles()
        assert len(titles_before_scroll) > 0

        # when I scroll down
        self.scroll_down()


        # then I should see another news cards
        titles_after_scroll = MainScreen.titles()
        assert len(titles_after_scroll) > 0
        assert titles_before_scroll != titles_after_scroll

        tear_down()

    def test_pass_card_to_notification(self):
        # given I install and open the app
        set_up()
        MainScreen.wait_for_screen_active()

        # when I select first news card to display in the notifications bar
        MainScreen.first_card().click()
        first_card_title_text = MainScreen.first_card_title_text()
        first_card_content_text = MainScreen.first_card_content_text()

        # and I open Home
        self.execute_adb('shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN')

        # and I open notifications
        driver().open_notifications()
        self.wait_for_element_by_id('android:id/title')

        # then I should see correct news card in notification bar
        assert first_card_title_text in self.notification_titles()
        assert first_card_content_text in self.notification_contents()

        tear_down()

    def wait_for_element_by_id(self, id):
        WebDriverWait(driver(), 10).until(
        EC.presence_of_element_located((By.ID, id))
        )

    def scroll_down(self):
        width = driver().get_window_size()['width']
        height = driver().get_window_size()['height']

        driver().swipe(width*0.5, height*0.7, width*0.5, height*0.3, 400)

    def notification_titles(self):
        ntf = []
        for el in driver().find_elements_by_id('android:id/title'):
            ntf.append(el.get_attribute('text'))
        return ntf

    def notification_contents(self):
        ntf = []
        for el in driver().find_elements_by_id('android:id/text'):
            ntf.append(el.get_attribute('text'))
        return ntf

    def execute_adb(self, command):
        subprocess.call(f'adb -s {driver().desired_capabilities["deviceUDID"]} {command}',shell=True)
