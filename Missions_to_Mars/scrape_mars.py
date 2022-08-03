#!/usr/bin/env python
# coding: utf-8

# In[159]:


from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo



def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # In[137]:
    

    ### NASA Mars News
    url = 'https://redplanetscience.com'
    browser.visit(url)
    soup = bs(browser.html,'html.parser')
    title_1 = soup.find('div', class_= 'content_title')

    
    ### JPL Mars Space Images - Featured Image
    
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('a',class_='fancybox-thumbs')
    
    for result in results:
        featured_image_url = result['href']
        print(featured_image_url)
    
      
    
    ### Mars Facts
    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)
    tables
    
    
    df = tables[0]
    df.head()
    
    df = df.drop([2],axis=1)
    df.head()
    
    html_table = df.to_html()
    html_table = html_table.replace('\n','')
    html_table
    
    df.to_html('table.html')
 

    ### Mars Hemispheres
    url = 'https://marshemispheres.com'
    browser.visit(url)
    soup = bs(browser.html,'html.parser')
    
    
    listings_1 = soup.find_all('div', class_='description')
    for listing in listings_1:
        title = listing.find('a', class_="itemLink product-item").h3.text
    
    listings_2 = soup.find_all('div',class_='item')
    for listing in listings_2:
        img_url = listing.find('img', class_='thumb')['src']
    
    
    hemisphere_image_urls = []
    for i in range(4):
        dic = {title:img_url}
        hemisphere_image_urls.append(dic)

    py_dicts = {
            'Hemisphere_Img': hemisphere_image_urls,
            'JPL_Space_Img' : featured_image_url

        }


    return py_dicts