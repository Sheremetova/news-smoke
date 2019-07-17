import unittest

from config import *
from device import *
from page_objects.main_screen import MainScreen
from page_objects.notification_bar_screen import NotificationBarScreen

class NewsSmokeTests(unittest.TestCase):
    def test_scroll_down(self):
        # given I install and open the app
        set_up()
        MainScreen.wait_for_screen_active()

        # then I see some news cards
        titles_before_scroll = MainScreen.titles()
        assert titles_before_scroll and '' not in titles_before_scroll,
               "Some titles before scroll are empty"

        # when I scroll down
        scroll_down()

        # then I should see another news cards
        titles_after_scroll = MainScreen.titles()

        assert titles_after_scroll and '' not in titles_after_scroll,
               "Some titles after scroll are empty"
        assert titles_before_scroll != titles_after_scroll,
               "Same titles appears after scroll"

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
        execute_adb('shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN')

        # and I open notifications
        driver().open_notifications()
        NotificationBarScreen.wait_for_screen_active()

        # then I should see correct news card in notification bar
        assert first_card_title_text in NotificationBarScreen.titles()
        assert first_card_content_text in NotificationBarScreen.contents()

        tear_down()
