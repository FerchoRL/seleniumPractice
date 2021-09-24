import time
import unittest
import HtmlTestRunner
import sys
import os
from ddt import ddt, file_data, data
from selenium import webdriver
from page_object.search_page import SearchPage

sys.path.append("D://htdocs//pycharmProjects//apexPractice")

@ddt
class TestSearchProduct(unittest.TestCase):

    @classmethod
    # Define global variables
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/htdocs/pycharmProjects/apexPractice/drivers/chromedriver.exe")
        cls.driver.get("https://www.liverpool.com.mx/tienda/home")
        cls.driver.maximize_window()
        cls.search_page = SearchPage(driver=cls.driver)
        cls.driver.implicitly_wait(time_to_wait=20)

    @data("FIFA 21", "Funda Samsung Galaxy A70", "Resident Evil Village XBOX")
    def test_product_found(self, product):
        # Call search_main_page
        self.search_page.search_main_page(product=product)
        # Call search_successful()
        is_search_successful = self.search_page.search_successful()
        # Assertions
        assert is_search_successful is True

    @file_data("D:\\htdocs\\pycharmProjects\\apexPractice\\Files\\invalid_product_data.json")
    def test_product_not_found(self, value_search, expected_msg):
        self.search_page.search_main_page(product=value_search)
        msg_not_found = self.search_page.invalid_search()
        assert msg_not_found.is_displayed() is True
        self.assertEqual(msg_not_found.text, expected_msg)

    def test_filter_product_results(self):
        self.search_page.search_main_page(product="Un Producto Desconocido")
        self.search_page.filter_results()

    @classmethod
    def tearDownClass(cls):
        print("hello")
        # cls.driver.close()

    if __name__ == '__main__':
        # Generate HTML Report with command: python TestScripts\test_search_product.py
        # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\htdocs\\pycharmProjects\\apexPractice\\reports'))
        unittest.main()
