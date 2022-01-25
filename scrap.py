from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import numpy as np
address_data = pd.read_csv('Python Quiz Input - Sheet1.csv', sep=',',header=None)

data = address_data.values

url = 'https://tools.usps.com/zip-code-lookup.htm?byaddress'

Chromedriver_location = ''

browser = webdriver.Chrome(Chromedriver_location)
browser.get(url)
Valid_list = ['Valid_Adress']

for i in range(len(data)-1):
    Street_Address_data = data[i+1][1]
    City_data = data[i+1][2]
    State_data = data[i+1][3]
    ZIP_data = data[i+1][4]
    
    ##Write Adress##

    Street_Address = browser.find_element_by_xpath('//*[@id="tAddress"]')
    Street_Address.clear()
    Street_Address.send_keys(Street_Address_data)
    
    ##Write City##

    City = browser.find_element_by_xpath('//*[@id="tCity"]')
    City.clear()
    City.send_keys(City_data)
    
    ##Write ZIP##

    ZIP = browser.find_element_by_xpath('//*[@id="tZip-byaddress"]')
    ZIP.clear()
    ZIP.send_keys(ZIP_data)
    
    ##Select State##

    select = Select(browser.find_element_by_xpath('//*[@id="tState"]'))

    State = State_data

    for i in range(x-1): 
        if len(select.options[i].text) > 2:
            if State == select.options[i].text[:2]:
                select.select_by_index(i)
    
    ##Check##
    browser.find_element_by_xpath('//*[@id="zip-by-address"]').click()
    Valid_Adress = 'Yes'
    
    ##wait until page is loaded##
    
    time.sleep(1)
    
    try:
        browser.find_element_by_xpath('//*[@id="zip-lookup-app"]/div/div[5]/div/div/div[7]/div/div[2]/a').click()
        Valid_list.append(Valid_Adress)
    except:
        Valid_Adress = 'No' 
        Valid_list.append(Valid_Adress)
    
browser.close()

import numpy as np
data = address_data.values

data = np.concatenate((data,np.array([(Valid_list)]).T), axis=1)

pd.DataFrame(data).to_csv("Python Quiz Input - Sheet1 new.csv")


