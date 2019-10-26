import json
import pytest
from selenium import webdriver


class TestWebsite:
    @pytest.fixture()
    def test_setup(self):
        global games, driver
        games = json.load(open("/Users/admin/PycharmProjects/TestingRSWebsite/data/games.json"))
        driver = webdriver.Chrome(executable_path="/Users/admin/PycharmProjects/TestingRSWebsite/drivers/"
                                                  "chromedriver")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_data_base(self, test_setup):
        driver.get("http://rska.herokuapp.com/")
        driver.find_element_by_xpath("//*[contains(text(), 'Links')]").click()
        driver.find_element_by_xpath("//*[contains(text(), 'About Me')]").click()

        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_xpath("//*[contains(text(), 'Game Store')]").click()

        driver.find_element_by_id("delete_all").click()

        for game in games:
            driver.find_element_by_id("title").send_keys(game['tittle'])
            driver.find_element_by_id("rdate").send_keys(game['rdate'])
            driver.find_element_by_id("type").send_keys(game['type'])
            driver.find_element_by_id("company").send_keys(game['company'])
            driver.find_element_by_id("add_entry").click()
            driver.find_element_by_id("title").clear()
            driver.find_element_by_id("rdate").clear()
            driver.find_element_by_id("type").clear()
            driver.find_element_by_id("company").clear()
