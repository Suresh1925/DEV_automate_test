import time
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilites.readproperties import Readconfig


class Test_01_Login:
    url = Readconfig.getapplicationurl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()

    def test_homepage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.Username)
        self.lp.set_password(self.Password)
        self.lp.click_login()
        time.sleep(10)
        self.lp.click_date_in_overview()
        self.lp.click_Today_date_in_overview()
        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\" + "login_page.png")
        time.sleep(2)
        self.lp.click_userprofile()
        self.lp.click_logout()

