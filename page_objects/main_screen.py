from config import App
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainScreen:
    def titles():
        titles = []

        for el in App.driver().find_elements_by_id('titleText'):
            titles.append(el.get_attribute('text'))
        return titles


    def wait_for_screen_active():
        WebDriverWait(App.driver(), 10).until(
        EC.presence_of_element_located((By.ID, 'cardView'))
        )

    def first_card():
        return App.driver().find_element_by_id('cardView')

    def first_card_title_text():
        return App.driver().find_element_by_id('titleText').get_attribute('text')

    def first_card_content_text():
        return App.driver().find_element_by_id('descriptionText').get_attribute('text')
