import pytest
import random
from selenium import webdriver


# selenium easy solutions : "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
class TestWebsite:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/admin/PycharmProjects/TestingRSWebsite/drivers/"
                                                  "chromedriver")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        # driver.close()
        # driver.quit()
        print("Test completed")

    def test_all(self, test_setup):
        # TEST 1 #
        for i in range(10):
            i = random.randint(-100000000000,2000000000)
            driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
            driver.find_element_by_id("user-message").send_keys("My first message!!!")
            driver.find_element_by_xpath("//*[contains(text(), 'Show Message') and @class='btn btn-default']").click()
            driver.find_element_by_id("sum1").send_keys(int(i))
            driver.find_element_by_id("sum2").send_keys(int(i*10/2555))
            driver.find_element_by_xpath("//*[contains(text(), 'Get Total') and @class='btn btn-default']").click()

        # # TEST 2 #
        for i in range(10):

            driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
            driver.find_element_by_id("isAgeSelected").click()
            driver.find_element_by_xpath("//*[@value='Check All' and @class='btn btn-primary']").click()

            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[1]/label/input").click()
            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[2]/label/input").click()
            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[3]/label/input").click()

        # # TEST 3 #
        for i in range(10):

            driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[1]/div[2]/label[1]/input").click()
            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[1]/div[2]/label[2]/input").click()
            driver.find_element_by_xpath("//*[@id='buttoncheck']").click()

            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[1]/label[1]/input").click()
            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[1]/label[2]/input").click()

            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[2]/label[1]/input").click()
            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[2]/label[2]/input").click()
            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[2]/label[3]/input").click()
            driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/button").click()

        # ### TEST 4 ###
        for i in range(5):

            driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
            driver.find_element_by_xpath("//*[@id='select-demo']").click()
            driver.find_element_by_xpath("//*[@id='select-demo']/option[2]").click()
            driver.find_element_by_xpath("//*[@id='select-demo']").click()
            driver.find_element_by_xpath("//*[@id='select-demo']/option[3]").click()
            driver.find_element_by_xpath("//*[@id='select-demo']").click()
            driver.find_element_by_xpath("//*[@id='select-demo']/option[4]").click()
            driver.find_element_by_xpath("//*[@id='select-demo']").click()
            driver.find_element_by_xpath("//*[@id='select-demo']/option[5]").click()
            driver.find_element_by_xpath("//*[@id='select-demo']").click()
            driver.find_element_by_xpath("//*[@id='select-demo']/option[6]").click()
            driver.find_element_by_xpath("//*[@id='select-demo']").click()
            driver.find_element_by_xpath("//*[@id='select-demo']/option[7]").click()
            driver.find_element_by_xpath("//*[@id='select-demo']").click()
            driver.find_element_by_xpath("//*[@id='select-demo']/option[8]").click()

            driver.find_element_by_xpath("//*[@id='multi-select']/option[1]").click()
            driver.find_element_by_xpath("//*[@id='multi-select']/option[2]").click()
            driver.find_element_by_xpath("//*[@id='multi-select']/option[3]").click()
            driver.find_element_by_xpath("//*[@id='multi-select']/option[4]").click()
            driver.find_element_by_xpath("//*[@id='multi-select']/option[5]").click()
            driver.find_element_by_xpath("//*[@id='multi-select']/option[6]").click()
            driver.find_element_by_xpath("//*[@id='multi-select']/option[7]").click()
            driver.find_element_by_xpath("//*[@id='multi-select']/option[8]").click()
            driver.find_element_by_xpath("// *[ @ id = 'printMe']").click()
            driver.find_element_by_xpath("// *[ @ id = 'printAll']").click()

        # # TEST 5 #
        for i in range(5):
            driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")
            driver.find_element_by_xpath("// *[ @ id = 'contact_form'] / fieldset / div[1] / div / div / input").send_keys(
                "Janusz")
            driver.find_element_by_xpath("// *[ @ id = 'contact_form'] / fieldset / div[2] / div / div / input").send_keys(
                "Kowalski")

            driver.find_element_by_xpath("// *[ @ id = 'contact_form'] / fieldset / div[3] / div / div / input").send_keys(
                "janusz.kowalski@gmail.com")
            driver.find_element_by_xpath("// *[ @ id = 'contact_form'] / fieldset / div[4] / div / div / input").send_keys(
                "+48509321678")
            driver.find_element_by_xpath("// *[ @ id = 'contact_form'] / fieldset / div[5] / div / div / input").send_keys(
                "Kolorowa 27")
            driver.find_element_by_xpath("// *[ @ id = 'contact_form'] / fieldset / div[6] / div / div / input").send_keys(
                "Kraków")

            driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[7]/div/div/select").click()
            driver.find_element_by_xpath(
                " // *[ @ id = 'contact_form'] / fieldset / div[7] / div / div / select / option[2]").click()

            driver.find_element_by_xpath("// *[ @ id = 'contact_form'] / fieldset / div[8] / div / div / input").send_keys(
                "30-047")
            driver.find_element_by_xpath("// *[ @ id = 'contact_form'] / fieldset / div[9] / div / div / input").send_keys(
                "http://rska.herokuapp.com")
            driver.find_element_by_xpath(
                "// *[ @ id = 'contact_form'] / fieldset / div[10] / div / div[1] / label / input").click()

            driver.find_element_by_xpath(
                "// *[ @ id = 'contact_form'] / fieldset / div[11] / div / div / textarea").send_keys(
                "My super project!!")

            driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[13]/div/button").click()

        # # TEST 6 #
        text_area = "XWZYXZMSAKJBAS<MOIASDN2123213lkasdASDL"

        for i in range(6):
            driver.get("https://www.seleniumeasy.com/test/ajax-form-submit-demo.html")
            driver.find_element_by_xpath("//*[@id='title']").send_keys(text_area)
            driver.find_element_by_xpath("//*[@id='description']").send_keys(
                text_area+text_area)
            driver.find_element_by_xpath("//*[@id='btn-submit']").click()
            text_area += text_area

        # TEST 7 #
        for i in range(10):
            j = random.randint(1, 11)
            driver.get("https://www.seleniumeasy.com/test/jquery-dropdown-search-demo.html")
            driver.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div[1]/div/div[2]/span/span[1]/span/span[2]").click()
            driver.find_element_by_xpath("// *[ @ id = 'select2-country-results'] / li[{}]".format(j)).click()

        for k in range(1, 51):
            driver.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li/input").click()
            driver.find_element_by_xpath("/html/body/span/span/span/ul/li[{}]".format(k)).click()

        for n in range(1, 6):
            if n == 2 or n == 5:
                continue
            driver.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div[3]/div/div[2]/span/span[1]/span/span[2]").click()
            driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[{}]".format(n)).click()

        for x in range(1, 3):
            for y in range(1, 3):
                if x == 3:
                    continue
                driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[4]/div/div[2]/select").click()
                driver.find_element_by_xpath(
                    "//*[@id='files']/optgroup[{}]/option[{}]]".format(
                        x, y)).click()
