# Search for Vertraege > multiple hits (search string = 8000), validate Vertrag, Produkt, Nachname, Status, Zahlweise & Status
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
UN = 'sach@bmw.de'
PW = 'Abcdef_1'
Vertraege = '8000'

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
#Vertraege
driver.get("https://qa-verka-portal.consulting.is2.show/#/uebersicht/verwaltung/vetraege/")
#wait for load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Hier finden Sie Ihre zu verwaltenden bAV-Verträge.")]')))
#Search for "AAAAAAA"
id = driver.find_element_by_xpath('//*[contains(text(), "Liste nach Vertrag, Kollektivvertrag oder Vor-/Nachname durchsuchen")]').get_attribute("for")
driver.find_element_by_xpath("//*[@id = '"+id+"' ]").send_keys(Vertraege)
#wait for loading bar to be gone

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Vertrag")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Produkt")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Nachname")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Weber")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Status")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Zahlweise")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "monatlich")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Rentenbegin")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "01.01.2030")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Balance Klassik")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800001")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800002")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800004")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800005")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800013")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800014")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800015")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800016")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800018")]')))
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "800019")]')))

print("Test Passed")

#Close browser
driver.close()