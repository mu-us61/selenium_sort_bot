from selenium import webdriver
from selenium.webdriver import Chrome
from . import constants as const
from .filtering import FilterPlaces
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(
        self, executable_path=const.DRIVER_PATH, breakdown=False, *args, **kwargs
    ):
        self.executable_path = executable_path
        super().__init__(self.executable_path, *args, **kwargs)
        self.breakdown = breakdown

        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, *args):
        if self.breakdown == True:
            self.quit()
        # return super().__exit__(*args)

    def homepage(self):
        self.get(const.BASE_URL)

    def select_currency(self, currency=None):
        btn_select_currency = self.find_element_by_css_selector(
            "button[data-tooltip-text='Choose your currency']"
        )
        btn_select_currency.click()

        btn_country = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param="changed_currency=1&selected_currency={currency}&top_currency=1"]'
        )
        btn_country.click()

    def select_city(self, city):
        btn_city = self.find_element_by_id("ss")
        btn_city.send_keys(f"{city}")
        btn_first_pick = self.find_element_by_css_selector('li[data-i="0"]')
        btn_first_pick.click()

    def select_date(self, start, end):
        # btn_date = self.find_element_by_css_selector(
        #     'li[data-component="search/dates/date-field-select"]'
        # )
        # btn_date.click()
        btn_start = self.find_element_by_css_selector(f'td[data-date="{start}"]')
        btn_start.click()

        btn_end = self.find_element_by_css_selector(f'td[data-date="{end}"]')
        btn_end.click()

    def select_adult_number(self, number=1):
        btn_selection = self.find_element_by_id("xp__guests__toggle")
        btn_selection.click()
        btn_increase = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        btn_decrease = self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]'
        )
        adultNumber = self.find_element_by_id("group_adults")

        while True:
            # print("while1")
            btn_decrease.click()
            adult_num = adultNumber.get_attribute("value")
            # print(adult_num)
            if int(adult_num) == 1:
                break

        while True:
            # print("while2")
            adult_num = adultNumber.get_attribute("value")
            if int(adult_num) == number:
                break
            else:
                btn_increase.click()

    def search(self):
        btn_search = self.find_element_by_css_selector('button[type="submit"]')
        btn_search.click()

    def filter_fun(self):
        driver = self
        filter_instance = FilterPlaces(driver)
        filter_instance.select_stars(4)
        filter_instance.sort_lowest_price()


