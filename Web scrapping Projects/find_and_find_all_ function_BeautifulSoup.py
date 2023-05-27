#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 19:59:03 2022

@author: tathagatasharma
"""

from bs4 import BeautifulSoup

import requests
import lxml

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

print(page)

soup = BeautifulSoup(page.text,'lxml')

#----------find()--------------------------

print(soup.header)

print(soup.find('header'))

print(soup.find('div',{'class':'container-fluid footer'}))

print(soup.find('h4',{'class':'pull-right price'}))

print(soup.find('h4',{'class':'pull-right price'}).string)


#-----------find_all()  part 1 ----------------------

print(soup.find_all('h4',{'class':'pull-right price'}))

print(soup.find_all('a',{'class':'title'}))

print(soup.find_all('a', class_='title'))

print(soup.find_all('p', class_="pull-right"))

print(soup.find_all('a',{'class':'title'})[2])

print(soup.find_all('a',{'class':'title'})[6:])


#-----------find_all()  part 2 ----------------------

print(soup.find_all(['h4','p'])) #Get more than one tag at a time

soup.find_all(id = True)

soup.find_all(String = "Iphone")

import re

soup.find_all(string = re.compile('Nok'))

soup.find_all(string = ['Iphone', 'Nokia 123'])

soup.find_all(class_ = re.compile('pull'))

soup.find_all('p', class_ = re.compile('pull'))

soup.find_all('p', class_ = re.compile('pull'), limit = 3)

#-----------find_all()  part 3 ----------------------

product_name = soup.find_all('a',class_ = 'title')

product_name = soup.find_all('a',{'class':'title'})

print(product_name)

product_name_list=[]

for i in product_name:
    name = i.text
    product_name_list.append(name)

print(product_name_list)


#------------------------------------
price = soup.find_all('h4', class_ = 'pull-right price')

print(price)

price_list = []

for i in price:
    n_price = i.text
    price_list.append(n_price)
    
print(price_list)


#------------------------------------
review = soup.find_all('p', class_ = re.compile('pull'))

print(review)

review_list = []

for i in review:
    n_review = i.text
    review_list.append(n_review)
    
print(review_list)

#------------------------------------
description = soup.find_all('p', class_ = 'description')

print(description)

description_list = []

for i in description:
    n_description = i.text
    description_list.append(n_description)
    
print(description_list)



import pandas as pd

table = pd.DataFrame({'Product Name': product_name_list , 'price': price_list, 
                      'review': review_list , 'description': description_list 
                     }) 

table



#---------Extracting data from Nested HTML Tags -------------------


boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')[6]
boxes

boxes.find('a').text

boxes.find('p', class_= 'description').text

box2 = soup.find_all('ul',class_ = 'nav', id = 'side-menu') [0]

box2.find_all('li')[1].text





