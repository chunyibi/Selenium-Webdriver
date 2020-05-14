# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:50:36 2020

@author: chuny
"""

# import useful python packages

import re      
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

# use selenium to open the kickstarter website via Chrome
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
browser.implicitly_wait(5)
browser.get("https://www.kickstarter.com/discover/advanced?woe_id=23424977&sort=magic&seed=2619898&page=1")
time.sleep(2)
# make sure the website language is English and currency is USD
browser.find_element_by_xpath("//select/option[@value='en']").click()
browser.find_element_by_xpath("//select/option[@value='USD']").click()
# clike the "Load more" button
browser.find_element_by_id("text").click()
# set number of pages you want to scroll down
for i in range(100):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# use beautifulsoup to get all page source and get all related information
get_soup = BeautifulSoup(browser.page_source, 'html.parser')
get_info = get_soup.find_all('div', attrs={'class': 'mb5 relative'})

# close and quit the browser 
browser.close()        
browser.quit()

# get title, funded percentage, funded amount, project category and project location from the website
# set all data in the desired format
data=[]
for info in get_info:
    title= "NA"
    funded_percent= "NA"
    funded_amount= "NA"
    category = "NA"
    location= "NA"
    
    t=info.find("h3",attrs={"class":"type-18 light hover-item-text-underline mb1"})
    if t:
        title=t.text.strip()
    f=info.find("div",attrs={"class":"type-13 mr2 dark-grey-500 medium"})
    if f:
        funded_percent= re.findall(r'[0-9]+,[0-9]+|[0-9]+',f.text.strip())[0].replace(",","")
    fa=info.find("div",attrs={"class":"type-13 mr2"})
    if fa:
        funded_amount=re.findall(r'[0-9]+,[0-9]+|[0-9]',fa.text.strip())[0].replace(",","")
    c=info.find("a",attrs={'href':re.compile('/categories/')})
    if c:
        subcategory=c.text.strip()
        category=re.search('/categories/(.*?)">', str(c)).group(1).split("/")[0]
    l=info.find("a",attrs={"class":"dark-grey-500 hover-soft-black text-underline type-13 medium ml4"})
    if l:
        city=l.text.split(",")[0]
        state=l.text.split(",")[1]
    if float(funded_percent)==0:
        goal=0
    else:
        goal=float(funded_amount)/(float(funded_percent)/100)
    data.append([title,float(funded_percent),float(funded_amount),int(goal),category,subcategory,city,state])

# proper format the data use dataframe
# export the data to excel file
headers=["Project Title","Funded Percentage","Funded Amount","Project Goal","Project Category","Sub Category","Project City","Project State"] 
df=pd.DataFrame(data,columns=headers)
#df.to_excel("kickstarter.xlsx")
df.to_excel("kickstarter_ORIGINAL.xlsx")