from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import random

class Tf2Bot:
    def __init__(self, unsername, password):
        self.username = unsername
        self.password = password
        self.driver = webdriver.Chrome("C://Users/jean-//AppData//Local//Programs//Python//Python38-32//pcproject//chromedriver.exe") 

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://scrap.tf/")
        time.sleep(2)
        login_button = driver.find_element_by_class_name("sits-login")
        login_button.click()
        time.sleep(2)
        username_entree = driver.find_element_by_name("username")
        username_entree.clear()
        username_entree.click()
        username_entree.send_keys(self.username)
        time.sleep(2)
        password_entree = driver.find_element_by_name("password")
        password_entree.clear()
        password_entree.click()
        password_entree.send_keys(self.password)
        time.sleep(2)
        login_button_steam = driver.find_element_by_id("imageLogin")
        login_button_steam.click()
        time.sleep(15)
        driver.get("https://scrap.tf/raffles")
        action = ActionChains(driver)


        for i in range(10):
            run = True
            while run:
                action.perform()  # pour toute la page window.scrollTo(0, document.body.scroll);  #driver.get(items)
                time.sleep(2)
                items = driver.find_element_by_class_name("items-container")
                action.click(items)
                print("oui")
                time.sleep(5)
                upgrade_action = ActionChains(driver)
                finbtn = driver.find_element_by_class_name("fa fa-sign_in")
                upgrade_action.move_to_element(finbtn)
                upgrade_action.click()
                upgrade_action.perform()
                driver.execute_script("window.history.go(-1)")

            if not driver.execute_script("window.history.go(-1)"):
                run = False
                print("non")
                tatave.closeBrowser()

tatave = Tf2Bot("masashitakeda", "Gustave34093")
tatave.login()
