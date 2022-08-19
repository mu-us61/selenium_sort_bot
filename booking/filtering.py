from selenium.webdriver.remote.webdriver import WebDriver


class FilterPlaces:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_stars(self, stars=2):
        element = self.driver.find_element_by_css_selector(
            f'div[data-filters-item="class:class={stars}"]'
        )
        element.click()

    def sort_lowest_price(self):
        btn = self.driver.find_element_by_css_selector(
            'button[data-testid="sorters-dropdown-trigger"]'
        )
        btn.click()
        btn2 = self.driver.find_element_by_css_selector('button[data-id="price"]')
        btn2.click()
