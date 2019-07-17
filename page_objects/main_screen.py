from config import App
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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

    def visible_news_cards():
        cards = App.driver().find_elements_by_id('cardView')
        for card in cards:
            try:
                card.find_element_by_id('titleText')
                card.find_element_by_id('descriptionText')
            except NoSuchElementException:
                cards.remove(card)

        return cards

    def title_of(card):
        return card.find_element_by_id('titleText').text

    def content_of(card):
        return card.find_element_by_id('descriptionText').text
