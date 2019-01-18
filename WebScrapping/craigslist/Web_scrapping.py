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
page_link = 'https://portland.craigslist.org/search/hum?'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(page_link)

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

info ={}
for link in pdx_links:
  page = urllib.request.urlopen(link)
  
  # parse the html using beautiful soup and store in variable `soup`
  soup = BeautifulSoup(page, 'html.parser')
  
  html=''
  for i in range(len(soup.contents)):
      html = html+str(soup.contents[i])
  
  # get compensastion
  get_comp = re.compile(r'compensation: <b>(.+)</b>')
  comp = get_comp.findall(html)
  
  # get emp type
  get_emp_typ = re.compile(r'employment type: <b>(.+)</b>')
  emp_typ = get_emp_typ.findall(html)


