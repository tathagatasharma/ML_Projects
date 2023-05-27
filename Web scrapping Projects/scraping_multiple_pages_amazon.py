#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:10:05 2023

@author: tathagatasharma
"""
#part1

import requests
import pandas as pd
from bs4 import BeautifulSoup


url='https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')


#part2

df = pd.DataFrame({'Link':[''],'Name':[''],'Price':[''],'Color':['']})

#for postings in range(15):

counter=0   
while counter<10:
    postings = soup.find_all('div', class_ = 'media soft push-none rule')
    
    for post in postings:
        
        link = post.find('a', class_='media__img media__img--thumb').get('href')
        link_full = 'https://www.carpages.ca'+link
        name = post.find('h4', class_= 'hN').text.strip()
        price = post.find('div', class_='l-column l-column--medium-4 push-none').text.strip()
        color = post.find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        df = df.append({'Link':link_full,'Name':name,'Price':price,'Color':color}, ignore_index=True)
    
    #next_page = soup.find('a', class_='nextprev').get('href')
    #next_page_full='https://www.carpages.ca'+next_page
    
    try:

        next_page = soup.find_all('a', class_ = 'nextprev')[1].get('href')
        next_page_full='https://www.carpages.ca'+next_page
    except:

        next_page = soup.find('a', class_ = 'nextprev').get('href')
        next_page_full='https://www.carpages.ca'+next_page
   
    page = requests.get(next_page_full)
    soup=BeautifulSoup(page.text,'lxml')
    counter+=1
    
df.to_csv('/Users/tathagatasharma/Documents/carpages_multiple_pages_updated.csv')