from config import driver

class MainScreen:
    def titles():
        titles = []

        for el in driver().find_elements_by_id('titleText'):
            titles.append(el.get_attribute('text'))
        return titles
