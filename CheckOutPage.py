from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)