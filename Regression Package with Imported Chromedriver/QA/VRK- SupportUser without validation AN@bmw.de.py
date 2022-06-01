# support@verka.de for an@bmw.de
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
chromeDriverExe = "/usr/local/bin/chromedriver"
UN = 'support@verka.de'
PW = 'Abcdef_1'
AN = 'an@bmw.de'

#Options
##################
options = webdriver.ChromeOptions()
options.add_argument("headless")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#Open URL
driver.get("https://qa-verka-portal.consulting.is2.show/#/login")
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
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Benutzername / E-Mail-Adresse *")]')))
#Benutzer
driver.find_element_by_xpath('//input[@id="input-58"]').send_keys(AN)
time.sleep(1)
#Click Prüfung
driver.find_element_by_xpath('//*[contains(text(), "Prüfung")]').click()
time.sleep(1)
#Click Starten
driver.find_element_by_xpath('//*[contains(text(), "Starten")]').click()

print("Test Passed")

#Close browser
driver.close()