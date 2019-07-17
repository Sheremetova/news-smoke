import unittest
import time

from config import App
from device import *
from page_objects.main_screen import MainScreen
from page_objects.notification_bar_screen import NotificationBarScreen

class NewsSmokeTests(unittest.TestCase):
    def test_scroll_down(self):
        # given internet connection is enabled
        execute_adb('shell svc wifi enable')
        execute_adb('shell svc data enable')

        # and I install and open the app
        App.set_up()
        MainScreen.wait_for_screen_active()

        # then I see some news cards
        titles_before_scroll = MainScreen.titles()
        assert titles_before_scroll and '' not in titles_before_scroll, \
               "Some titles are empty"
        contents_before_scroll= MainScreen.contents()
        assert contents_before_scroll and '' not in contents_before_scroll, \
               "Some contents are empty"

        # when I scroll down
        scroll_down()

        # then I should see another news cards
        titles_after_scroll = MainScreen.titles()
        contents_after_scroll = MainScreen.contents()

        assert titles_after_scroll and '' not in titles_after_scroll, \
               "Some titles after scroll are empty"
        assert contents_after_scroll and '' not in contents_after_scroll, \
               "Some contents after scroll are empty"

        assert titles_before_scroll != titles_after_scroll, \
               "Same titles appears after scroll"
        assert contents_before_scroll != contents_after_scroll, \
               "Same contents appears after scroll"

        App.tear_down()

    def test_pass_card_to_notification(self):
        # given internet connection is enabled
        execute_adb('shell svc wifi enable')
        execute_adb('shell svc data enable')

        # and I install and open the app
        App.set_up()
        MainScreen.wait_for_screen_active()

        # when I select first news card to display in the notifications bar
        first_news_card = MainScreen.visible_news_cards()[0]
        first_news_card.click()
        first_card_title_text = MainScreen.title_of(first_news_card)
        first_card_content_text = MainScreen.content_of(first_news_card)

        # and I open Home
        execute_adb('shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN')

        # and I open notifications
        App.driver().open_notifications()
        NotificationBarScreen.wait_for_screen_active()

        # then I should see correct news card in notification bar
        # TODO : implement title and content checking in a separate notification
        assert first_card_title_text in NotificationBarScreen.titles(), \
               "Notification titles doesn't contain correct text"
        assert first_card_content_text in NotificationBarScreen.contents(), \
               "Notification contents doesn't contain correct text"

        App.tear_down()

    def test_news_filtering(self):
        # given internet connection is enabled
        execute_adb('shell svc wifi enable')
        execute_adb('shell svc data enable')

        # and I install and open the app
        App.set_up()
        MainScreen.wait_for_screen_active()

        # when I enter 'SpaceX' to search box
        titles_before_update = MainScreen.titles()
        text = 'SpaceX'
        MainScreen.type_to_search_box(text)
        self.wait_until_titles_updated(titles_before_update)

        # then I should see news cards with the 'SpaceX' text in the title or content
        for card in MainScreen.visible_news_cards():
            assert text in MainScreen.title_of(card) or \
                   text in MainScreen.content_of(card)

        App.tear_down()

    def test_saving_data_without_internet(self):
        # given internet connection is enabled
        execute_adb('shell svc wifi enable')
        execute_adb('shell svc data enable')

        # given I install and open the app
        App.set_up()
        MainScreen.wait_for_screen_active()

        # then I see some news cards
        titles_before_internet_disabling = MainScreen.titles()
        assert titles_before_internet_disabling and '' not in titles_before_internet_disabling, \
               "Some titles are empty"

        contents_before_internet_disabling = MainScreen.contents()
        assert contents_before_internet_disabling and '' not in contents_before_internet_disabling, \
               "Some contents are empty"

        # when I close the app
        App.driver().close_app()

        # and I disable internet connection
        execute_adb('shell svc wifi disable')
        execute_adb('shell svc data disable')

        # and I open the app
        App.driver().launch_app()

        # then I should see the same some news cards
        assert titles_before_internet_disabling == MainScreen.titles(), \
               "Titles changed after turning off the internet connection"
        assert contents_before_internet_disabling == MainScreen.contents(), \
               "Contents changed after turning off the internet connection"

        App.tear_down()

    def wait_until_titles_updated(self, titles_before_update):
        end = time.time() + 10
        while time.time() < end:
            if titles_before_update != MainScreen.titles():
                return True
            else:
                time.sleep(0.1)
        raise Exception('Titles were not updated in 10 seconds')
