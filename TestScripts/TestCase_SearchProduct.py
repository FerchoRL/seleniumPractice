from selenium import webdriver
from ddt import ddt, data, file_data
import HtmlTestRunner
import unittest


@ddt
class SearchProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:/htdocs/pycharmProjects/apexPractice/drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.liverpool.com.mx/tienda/home")
        self.driver.implicitly_wait(time_to_wait=20)

    @data("FIFA 21", "Funda Samsung Galaxy A70", "Resident Evil Village XBOX")
    def test_product_found(self, product):
        # game_info = "FIFA 21 Legacy Edición Regular para Nintendo switch Juego Físico"
        # Obtain web driver elements
        search_bar = self.driver.find_element_by_xpath("//input[@placeholder='Buscar...']")
        search_btn = self.driver.find_element_by_xpath("//i[@class='icon-zoom']/parent::button[@class='input-group-text']")
        # Search product
        search_bar.send_keys("FIFA 21")
        search_btn.click()
        item_info = self.driver.find_element_by_class_name("a-product__information--title")
        # Validate h1 information is displayed
        self.assertTrue(item_info.is_displayed())
        # Validate h1 contains game info
        # self.assertEqual(game_info, item_info.text)

    @file_data("D:\\htdocs\\pycharmProjects\\apexPractice\\Files\\invalid_product_data.json")
    def test_product_not_found(self, value_search, expected_msg):
        product = "5489321753"
        # Obtain web driver elements
        search_bar = self.driver.find_element_by_xpath("//input[@placeholder='Buscar...']")
        search_btn = self.driver.find_element_by_xpath("//i[@class='icon-zoom']/parent::button[@class='input-group-text']")
        # Search product
        search_bar.send_keys(value_search)
        search_btn.click()
        msg_not_found = self.driver.find_element_by_css_selector("h1.a-headline__results.d-lg-block")
        # Validate h1 message not found
        self.assertTrue(msg_not_found.is_displayed())
        # Validate msg not found
        self.assertEqual(msg_not_found.text, expected_msg)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # Generate HTML Report with command: python TestScripts\TestCase_SearchProduct.py
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\htdocs\\pycharmProjects\\apexPractice\\reports'))
    unittest.main()
