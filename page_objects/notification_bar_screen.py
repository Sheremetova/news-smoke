from config import App
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class NotificationBarScreen:
    def wait_for_screen_active():
        WebDriverWait(App.driver(), 10).until(
        EC.presence_of_element_located((By.ID, 'android:id/title'))
        )

    def titles():
        titles = []

        for el in App.driver().find_elements_by_id('android:id/title'):
            titles.append(el.text)
        return titles

    def contents():
        contents = []

        for el in App.driver().find_elements_by_id('android:id/text'):
            contents.append(el.text)
        return contents
