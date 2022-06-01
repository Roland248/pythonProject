# Search for AN > no hit (search string = 123), validate message = Keine Daten verfügbar
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
UN = 'admin@bmw.de'
PW = 'Abcdef_1'
Name = '123'

###ERORS###
class ProduktNoMatch(Exception):
    """Products do not match"""
    def __init__(self, itr, message="Products do not match"):
        self.itr = itr
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.itr} -> {self.message}'
class ZahlwegNoMatch(Exception):
    """Zahlweg do not match"""
    def __init__(self, itr, message="Zahlweg do not match"):
        self.itr = itr
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.itr} -> {self.message}'
    pass
class FinanzierungsartNoMatch(Exception):
    """Finanzierungsart do not match"""
    def __init__(self, itr, message="Finanzierungsart do not match"):
        self.itr = itr
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.itr} -> {self.message}'
    pass

##################
options = webdriver.ChromeOptions()
options.add_argument("headless")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#Open URL
driver.get("https://qa-verka-portal.consulting.is2.show/#/login")
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Anmelden")]')))
driver.maximize_window()
#Username
driver.find_element_by_xpath('//input[@id="login-email"]').send_keys(UN)
#Pass
driver.find_element_by_xpath('//input[@id="login-password"]').send_keys(PW)
#Login button
driver.find_element_by_xpath('//*[contains(text(), "Jetzt anmelden!")]').click()
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Arbeitgeber Verka Portal")]')))
#Verwaltung
driver.find_element_by_xpath('//*[contains(text(), "Verwaltung")]').click()
#Mitarbeiter
driver.get("https://qa-verka-portal.consulting.is2.show/#/uebersicht/verwaltung/mitarbeiter/")
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Ihre Mitarbeitenden mit bAV-Vertrag")]')))

#Search for "Ir"
id = driver.find_element_by_xpath('//*[contains(text(), "Liste nach Namen durchsuchen")]').get_attribute("for")
driver.find_element_by_xpath("//*[@id = '"+id+"' ]").send_keys(Name)
#wait for loading bar to be gone
WebDriverWait(driver, 15).until_not(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Liste Mitarbeitende wird geladen")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Keine Daten verfügbar")]')))

print("Test Passed")

#Close browser
driver.close()