from config import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainScreen:
    def titles():
        titles = []

        for el in driver().find_elements_by_id('titleText'):
            titles.append(el.get_attribute('text'))
        return titles


    def wait_for_screen_active():
        WebDriverWait(driver(), 10).until(
        EC.presence_of_element_located((By.ID, 'cardView'))
        )
