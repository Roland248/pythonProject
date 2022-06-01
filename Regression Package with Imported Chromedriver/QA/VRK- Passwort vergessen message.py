# Validate "Passwort vergessen" info message
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
UN = 'aaa@verka.de'

#Options
##################
options = webdriver.ChromeOptions()
options.add_argument("headless")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#Open URL
driver.get("https://qa-verka-portal.consulting.is2.show/#/passwort-vergessen")
driver.maximize_window()
time.sleep(1)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Passwort vergessen?")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Haben Sie Ihr Passwort vergessen?")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Nach Eingabe Ihrer E-Mail-Adresse erhalten Sie eine E-Mail mit Hinweisen zum Zurücksetzen Ihres Passworts.")]')))
#Username
driver.find_element_by_xpath('//input[@id="password-forget-email"]').send_keys(UN)
#Send passwor re-set email
driver.find_element_by_xpath('//*[contains(text(), "Jetzt E-Mail senden!")]').click()
time.sleep(1)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Vielen Dank für Ihre Anfrage.")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Wir haben Ihnen eben eine E-Mail zum Zurücksetzen Ihres Passworts geschickt. Bitte folgen Sie den dortigen Hinweisen, um ein neues Passwort zu hinterlegen.")]')))

driver.find_element_by_xpath('//*[contains(text(), "Zur Anmeldung!")]').click()
time.sleep(1)

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "E-Mail-Adresse *")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Verka Portal Anmeldung")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Anmelden")]')))

print("Test Passed")

#Close browser
driver.close()