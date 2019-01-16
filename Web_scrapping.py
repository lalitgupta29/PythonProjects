# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup
import re

# specify the url
quote_page = 'https://portland.craigslist.org/search/hum?'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

#get search results 
search_results = soup.find('ul', attrs={'class':'rows'})

# get all the links on the search page
html=''
for i in range(len(search_results.contents)):
    html = html+str(search_results.contents[i])
html_ex = re.compile(r'href="(.+)"')
links = html_ex.findall(html)

# clean up links and filter links for portland locations
pdx_links = []
for i in range(len(links)):
  if 'portland' in links[i]:
    pdx_links.append(links[i])
    


