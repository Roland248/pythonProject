# Checking KollVtr tabs a validate Produkt, Finanzierungsart, Zahlweg and other attributes - TestFirm01
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

Produkt1 = 'Balance Flex'
Finanzierungsart1 = 'Arbeitgeberfinanzierung'
Zahlweg1 = 'Überweisung'
#IBAN1 = 'DE3000210800014009002'
#BIC1 = 'COBADEFFXXX'
#Bankname1 = 'Commerzbank AG'
#Kontoinhaber1 = 'Verka PK Kirchliche Pensionskasse AG'

Produkt2 = 'Balance Klassik'
Finanzierungsart2 = 'Mischfinanzierung'
Zahlweg2 = 'Lastschrift'

Produkt3 = 'Balance Flex'
Finanzierungsart3 = 'Entgeltumwandlung'
Zahlweg3 = 'Überweisung'

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
#Verwaltung
driver.find_element_by_xpath('//*[contains(text(), "Verwaltung")]').click()
#Firmendaten
driver.get("https://portal.verka.de/#/uebersicht/verwaltung/firmendaten")
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Einzahlungsbankverbindung")]')))
#Scroll to view
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[contains(text(), "Einzahlungsbankverbindung")]')).perform()
time.sleep(1)
#14009001
#driver.find_element_by_xpath('//*[contains(text(), "70909002")]').click()
produkt = driver.find_element_by_xpath('(//*[contains(text(), "Produkt")]/following::p[1])[1]').text
finanzierungsart = driver.find_element_by_xpath('(//*[contains(text(), "Finanzierungsart")]/following::p[1])[1]').text
zahlweg = driver.find_element_by_xpath('(//*[contains(text(), "Zahlweg")]/following::p[1])[1]').text
itr = "14009001"
try:
    assert produkt == Produkt1
except:
    raise ProduktNoMatch(itr)
try:
    assert zahlweg == Zahlweg1
except:
    raise ZahlwegNoMatch(itr)
try:
    assert finanzierungsart == Finanzierungsart1
except:
    raise FinanzierungsartNoMatch(itr)

# Validate Einzahlungsbankverbindung, IBAN, BIC, Bankname, Kontoinhaber
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Einzahlungsbankverbindung")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "DE3000210800014009002")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "COBADEFFXXX")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Commerzbank AG")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Verka PK Kirchliche Pensionskasse AG")]')))


#70909001
driver.find_element_by_xpath('//*[contains(text(), "70909001")]').click()
time.sleep(1)
produkt = driver.find_element_by_xpath('(//*[contains(text(), "Produkt")]/following::p[1])[2]').text
finanzierungsart = driver.find_element_by_xpath('(//*[contains(text(), "Finanzierungsart")]/following::p[1])[2]').text
zahlweg = driver.find_element_by_xpath('(//*[contains(text(), "Zahlweg")]/following::p[1])[2]').text
itr = "70909001"
try:
    assert produkt == Produkt2
except:
    raise ProduktNoMatch(itr)
try:
    assert zahlweg == Zahlweg2
except:
    raise ZahlwegNoMatch(itr)
try:
    assert finanzierungsart == Finanzierungsart2
except:
    raise FinanzierungsartNoMatch(itr)

# Validate Einzahlungsbankverbindung, IBAN, BIC, Bankname, Kontoinhaber
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Einzahlungsbankverbindung")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "DE30001210800070909001")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "BFSWDE33BER")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Bank für Sozialwirtschaft AG")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Verka PK Kirchliche Pensionskasse AG")]')))

#14009002
driver.find_element_by_xpath('//*[contains(text(), "14009002")]').click()
time.sleep(1)
produkt = driver.find_element_by_xpath('(//*[contains(text(), "Produkt")]/following::p[1])[3]').text
finanzierungsart = driver.find_element_by_xpath('(//*[contains(text(), "Finanzierungsart")]/following::p[1])[3]').text
zahlweg = driver.find_element_by_xpath('(//*[contains(text(), "Zahlweg")]/following::p[1])[3]').text
itr = "14009002"
try:
    assert produkt == Produkt3
except:
    raise ProduktNoMatch(itr)
try:
    assert zahlweg == Zahlweg3
except:
    raise ZahlwegNoMatch(itr)
try:
    assert finanzierungsart == Finanzierungsart3
except:
    raise FinanzierungsartNoMatch(itr)

# Validate Einzahlungsbankverbindung, IBAN, BIC, Bankname, Kontoinhaber
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Einzahlungsbankverbindung")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "DE3000210800014009001")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "COBADEFFXXX")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Commerzbank AG")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Verka PK Kirchliche Pensionskasse AG")]')))

print("Test Passed")

#Close browser
driver.close()