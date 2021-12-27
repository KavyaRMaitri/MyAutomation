from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from CheckOutPage import CheckOutPage
from HomePage import HomePage
from TestCases.Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        homepage.ShopItems().click()
        checkoutpage = CheckOutPage(self.driver)
        cards = checkoutpage.getCardTitle()

        cards = self.driver.find_elements_by_css_selector(".card-title a")

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                self.driver.find_element_by_css_selector(".card-footer button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        # time.sleep(5)
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = (self.driver.find_element_by_css_selector(".alert-success").text)
        print(textMatch)

        assert ("Success! Thank you!" in textMatch)