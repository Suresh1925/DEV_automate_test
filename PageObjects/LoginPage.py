from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "//*[@placeholder='Email']"
    textbox_password_id = "//*[@id='password']"
    button_login_id = "//*[@type='submit']"
    button_click = "//*[@class='rounded-circle']"
    button_logout_id = "//*[@class='feather feather-log-out icon-dual icon-xs mr-2']"
    button_click_date_in_overview = "//*[@class='p-dropdown-trigger-icon ng-tns-c68-3 pi pi-chevron-down']"
    button_click_today_date_in_overview = "//*[@aria-label='Today']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_id).click()

    def click_date_in_overview(self):
        self.driver.find_element(By.XPATH, self.button_click_date_in_overview).click()

    def click_Today_date_in_overview(self):
        self.driver.find_element(By.XPATH, self.button_click_today_date_in_overview).click()

    def click_userprofile(self):
        self.driver.find_element(By.XPATH, self.button_click).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.button_logout_id).click()