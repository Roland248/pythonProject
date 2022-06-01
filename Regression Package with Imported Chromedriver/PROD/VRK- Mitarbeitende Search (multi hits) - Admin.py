# Search for AN > multiple hits (search string = Ir)
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
UN = 'christian.pappenroth@verka.de'
PW = 'Verka#2021portal'
firstName = 'Ir'

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
driver.get("https://portal.verka.de/#/login")
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
driver.get("https://portal.verka.de/#/uebersicht/verwaltung/mitarbeiter/")
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Ihre Mitarbeitenden mit bAV-Vertrag")]')))

#Search for "Ir"
id = driver.find_element_by_xpath('//*[contains(text(), "Liste nach Namen durchsuchen")]').get_attribute("for")
driver.find_element_by_xpath("//*[@id = '"+id+"' ]").send_keys(firstName)
#wait for loading bar to be gone
WebDriverWait(driver, 15).until_not(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Liste Mitarbeitende wird geladen")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Irena")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Franke")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "16.07.1982")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Pierre")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Girschner")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "07.07.1989")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Birgitt")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Gute")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "16.01.1947")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Mira")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Lehmann")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "14.11.1952")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Irmtraud")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Pölitz")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "17.05.1987")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Miroslawa")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Schuchhardt")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "22.04.1948")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Jiri")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Seip")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "09.09.1968")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Birgit")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "von Weber")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "20.05.1970")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Angemeldet")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Kasimir")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Wiek")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "11.07.1942")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Grit")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Wirth")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "20.09.1952")]')))

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Fredi")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Zirme")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "02.05.1949")]')))

time.sleep(1)


print("Test Passed")

#Close browser
driver.close()