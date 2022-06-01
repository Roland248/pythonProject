# Vyhladanie zamestnanca last name + validacia
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
firstName = 'Claas'
lastName = 'Ackermann'
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

#Options
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
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Herzlich Willkommen im bAV-Portal der Verka. Alle Versicherungsverträge immer verfügbar.")]')))
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Ihr Schnelleinstieg in die Verwaltung")]')))
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Alle Bereiche auf einen Blick")]')))
#Mitarbeitende
driver.get("https://qa-verka-portal.consulting.is2.show/#/uebersicht/verwaltung/mitarbeiter/")
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Ihre Mitarbeitenden mit bAV-Vertrag")]')))
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Hier finden Sie eine Übersicht Ihrer Mitarbeitenden mit bestehendem bAV-Vertrag.")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Vorname")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Nachname")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Geburtsdatum")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Verträge")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Status")]')))
id = driver.find_element_by_xpath('//*[contains(text(), "Liste nach Namen durchsuchen")]').get_attribute("for")

#Search for "Ackermann"
driver.find_element_by_xpath("//*[@id = '"+id+"' ]").send_keys(lastName)
#wait for loading bar to be gone
WebDriverWait(driver, 15).until_not(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Liste Mitarbeitende wird geladen")]')))
time.sleep(1)


WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Claas")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Ackermann")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "16.02.1980")]')))
#WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Eingeladen")]')))

time.sleep(1)
#Data extraction
i = 1
j = ''
while i<=5:
    j = str(i)
    extractedText = driver.find_element_by_xpath("//tr/td["+j+"]").text
    print(extractedText)
    i +=1

print("Test Passed")

#Close browser
driver.close()