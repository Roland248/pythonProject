# Special characters in password
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import time
import datetime
#import pandas as pd
#import xerox
import sys
import string
import random
from selenium.webdriver.common.action_chains import ActionChains
###VARIABLES###
#chromedriver = "/usr/local/bin/chromedriver"
#chromeDriverExe = webdriver.Chrome(chromedriver)
chromeDriverExe = "/usr/local/bin/chromedriver"
UN = 'admin@bmw.de'
PW = 'Abcdef_1'
char = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ".", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", '''\'''', "]", "^", "_", "`", "{", "|", "}", "~", "§"]
#"”"  "’" this speciacl characters are not expected
expectedError = 'Bitte erstellen Sie ein gültiges Passwort.'
###ERORS###
class NoPassError(Exception):
    """Password error missing"""
    def __init__(self, message="Password error missing"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return {self.message}
class SpecialCharInvalid(Exception):
    """Character is not valid"""
    def __init__(self, SpecialChar, message="Character is not valid"):
        self.SpecialChar = SpecialChar
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f' " {self.SpecialChar} " -> {self.message}'

#Options
##################
options = webdriver.ChromeOptions()
options.add_argument("headless")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#Open URL
driver.get("https://qa-verka-portal.consulting.is2.show/#/login")
#Maximize screen
driver.maximize_window()
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Anmelden")]')))
#Username
driver.find_element_by_xpath('//input[@id="login-email"]').send_keys(UN)
#Pass
driver.find_element_by_xpath('//input[@id="login-password"]').send_keys(PW)
#Login button
driver.find_element_by_xpath('//*[contains(text(), "Jetzt anmelden!")]').click()
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Arbeitgeber Verka Portal")]')))
#Persönliche Daten
driver.get("https://qa-verka-portal.consulting.is2.show/#/uebersicht/persoenliche-daten")
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "admin@bmw.de")]')))
#Scroll to view
#ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[contains(text(), "Passwort")]')).perform()
#time.sleep(1)
driver.get("https://qa-verka-portal.consulting.is2.show/#/uebersicht/persoenliche-daten/passwort-aendern")
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Neues Passwort übernehmen")]')))
#driver.find_element_by_xpath('//a[contains(text(), "Passwort ändern")]').click()
driver.find_element_by_xpath('//input[@id="change-password-new-password"]').send_keys("Roland20211")
time.sleep(1)
msg = driver.find_element_by_xpath('//*[contains(text(), "Bitte erstellen Sie ein gültiges Passwort.")]').text
try:
    assert msg == expectedError
except:
    raise NoPassError()

for specialChar  in char:
    print(specialChar)
    driver.find_element_by_xpath('//input[@id="change-password-new-password"]').send_keys(specialChar)
    try:
        WebDriverWait(driver, 15).until_not(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Bitte erstellen Sie ein gültiges Passwort.")]')))
    except:
        print("Test Failed")
        raise  SpecialCharInvalid(specialChar)

    driver.find_element_by_xpath('//input[@id="change-password-new-password"]').send_keys(Keys.BACKSPACE)
    time.sleep(2)
    #driver.find_element_by_xpath('//input[@id="change-password-new-password"]').send_keys(Keys.CONTROL + "a")
    #driver.find_element_by_xpath('//input[@id="change-password-new-password"]').send_keys(Keys.DELETE)
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Bitte erstellen Sie ein gültiges Passwort.")]')))
    except:
        print("Test Failed")
        raise SpecialCharInvalid(specialChar)

print("Test Passed")

#Close browser
driver.close()