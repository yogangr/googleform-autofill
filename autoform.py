import pandas as pd
from selenium import webdriver
import time
import csv

def fill_form():
    with open("C:/Users/lenovo/Desktop/Autofill-googleform/data.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for data in csv_reader:
            driver = webdriver.Chrome()
            driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfv-8J6Y5xbvX6IvEhy9Hx2FK2RbRYeF9w8dUpKFKV9Rwfm8w/viewform')
            time.sleep(1)
# nama
            name = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            name.send_keys(data[0])
            time.sleep(0.05)
# jenis kelamin
            if data[1] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[1] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
# usia
            if data[2] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[2] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[2] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[2] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[2] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# Pendidikan
            if data[3] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[3] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[3] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[3] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[3] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# Pekerjaan
            if data[4] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[4] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[4] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[4] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[4] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
            elif data[4] == "6":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[6]')
                opsi2.click()
            elif data[4] == "7":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[7]')
                opsi2.click()
#  Berapa kali make up
            if data[5] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[5] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]')
                opsi2.click()
            elif data[5] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]')
                opsi2.click()
# Nomor HP
            nohp = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
            nohp.send_keys(data[6])
            time.sleep(0.05)
# next
            nextbutton = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            nextbutton.click()
            time.sleep(0.5)
# kuis 1 
            if data[7] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[7] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[7] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[7] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[7] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
#  kuis 2
            if data[8] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[8] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[8] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[8] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[8] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 3 
            if data[9] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[9] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[9] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[9] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[9] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# next
            nextbutton = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
            nextbutton.click()
            time.sleep(0.5)            
# kuis 4
            if data[10] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[10] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[10] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[10] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[10] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 5
            if data[11] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[11] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[11] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[11] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[11] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 6
            if data[12] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[12] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[12] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[12] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[12] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 7
            if data[13] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[13] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[13] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[13] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[13] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 8
            if data[14] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[14] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[14] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[14] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[14] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# next
            nextbutton = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
            nextbutton.click()
            time.sleep(0.5)
# kuis 9
            if data[15] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[15] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[15] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[15] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[15] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 10
            if data[16] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[16] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[16] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[16] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[16] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click() 
# next
            nextbutton = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
            nextbutton.click()
            time.sleep(0.5)
# kuis 11
            if data[17] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[17] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[17] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[17] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[17] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 12
            if data[18] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[18] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[18] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[18] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[18] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 13
            if data[19] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[19] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[19] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[19] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[19] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 14
            if data[20] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[20] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[20] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[20] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[20] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 15
            if data[21] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[21] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[21] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[21] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[21] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 16
            if data[22] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[22] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[22] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[22] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[22] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 17
            if data[23] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[23] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[23] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[23] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[23] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()
# kuis 18
            if data[24] == "1":
                opsi1 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]')
                opsi1.click()
            elif data[24] == "2":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]')
                opsi2.click()
            elif data[24] == "3":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[3]')
                opsi2.click()
            elif data[24] == "4":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[4]')
                opsi2.click()
            elif data[24] == "5":
                opsi2 = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[5]')
                opsi2.click()                                                                                                                

            submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
            submit.click()
            time.sleep(0.5)

fill_form()
time.sleep(1)