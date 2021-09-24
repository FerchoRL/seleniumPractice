import time

from selenium.webdriver import ActionChains


class SearchPage():
    # Locators
    SEARCH_BAR = "//input[@placeholder='Buscar...']"
    SEARCH_BTN = "//i[@class='icon-zoom']/parent::button[@class='input-group-text']"
    MSG_NOT_FOUND = "h1.a-headline__results.d-lg-block"
    PRODUCT_FOUND_INFO = "a-product__information--title"
    LIST_BTN_FILTER = "//button[@class='a-title__filter']"
    BRAND_BTN = "//button[h3[div[div[label[contains(text(),'Marcas')]]]]]"
    BRAND_CHECKBOX = "//input[@id='1z13br1']"
    PRICE_BTN = "//button[h3[div[div[label[contains(text(),'Precios')]]]]]"
    PRICE_CHECKBOX = "//input[@id='27ki']"

    def __init__(self, driver):
        self.driver = driver

    # Methods for searchPage
    def search_main_page(self, product):
        product_input = self.driver.find_element_by_xpath(self.SEARCH_BAR)
        product_input.send_keys(product)
        search_btn = self.driver.find_element_by_xpath(self.SEARCH_BTN)
        search_btn.click()

    def search_successful(self):
        # Return is_displayed locator
        product_info = self.driver.find_element_by_class_name(self.PRODUCT_FOUND_INFO).is_displayed()
        return product_info

    def invalid_search(self):
        msg_not_found = self.driver.find_element_by_css_selector(self.MSG_NOT_FOUND)
        return msg_not_found

    def filter_results(self):
        self.driver.implicitly_wait(time_to_wait=20)
        self.close_filters()
        self.filter_by(self.BRAND_BTN, self.BRAND_CHECKBOX)
        self.filter_by(self.PRICE_BTN, self.PRICE_CHECKBOX)

    def filter_by(self, btn_xpath, checkbox_xpath):

        btn_filter = self.driver.find_element_by_xpath(btn_xpath)
        btn_filter.click()
        checkbox_value = self.driver.find_element_by_xpath(checkbox_xpath)
        checkbox_value.click()
        btn_filter.click()

    def close_filters(self):
        list_filters = self.driver.find_elements_by_xpath(self.LIST_BTN_FILTER)
        for button in list_filters:
            time.sleep(1)
            button.click()

    def validate_is_active(self, list_xpath):
        # Obtain list element and validate if include active class
        list_values = self.driver.find_element_by_xpath(list_xpath)
        class_value = str(list_values.get_attribute("class"))
        is_active = True if class_value.find("active") else False
        return is_active
