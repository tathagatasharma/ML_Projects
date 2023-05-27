#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 09:26:37 2023

@author: tathagatasharma
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://www.nfl.com/standings/league/2020/REG'

page = requests.get(url)
page


soup = BeautifulSoup(page.text,'lxml')

soup

head = soup.find_all('thead')

head2=soup.find_all('th')



head_list=[]

for i in head2:
    header=i.text
    head_list.append(header)


head_list

len(head_list)

nfl = pd.DataFrame(columns=head_list)

body = soup.find_all('tbody')


for j in soup.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [td.text for td in row_data]
    length = len(nfl)
    nfl.loc[length] = row
    
nfl.to_csv('/Users/tathagatasharma/Documents/nfl_standings_scrapped_table.csv')
    
    
    