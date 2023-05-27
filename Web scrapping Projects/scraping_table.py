#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:36:19 2023

@author: tathagatasharma
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

soup

table = soup.find_all('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
table

title=table.find_all('th')
title


headers = []
for i in table.find_all('th'):
    column=i.text
    headers.append(column)

headers


df= pd.DataFrame(columns=headers)

df

#gets all our data within the table and adds it to our dataframe
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row
    
#exports the data as a csv
df.to_csv('/Users/tathagatasharma/Documents/world_population_scrapped_table.csv')


