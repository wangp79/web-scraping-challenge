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
    news_title = soup.find('div', class_= 'content_title')
    news_text = soup.find('div', class_='article_teaser_body')
    print(news_title)
    print(news_text)

    
    ### JPL Mars Space Images - Featured Image
    
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('a',class_='fancybox-thumbs')

    
    spaceMars_image = []

    for result in results:
        featured_image_url = result['href']
        spaceMars_image.append(f"{url}/{featured_image_url}")
    
    
    
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
    
    titles = []
    # contents = []
    listings_1 = soup.find_all('div', class_='description')
    for listing in listings_1:
        title = listing.find('a', class_="itemLink product-item").h3.text
        content = listing.find('p',class_='description')
        titles.append(title)
    print(titles)
    

    listings_2 = soup.find_all('div',class_='item')

    hemisphere_image=[]
    for listing in listings_2:
        img_url = listing.find('a', class_='itemLink product-item')['href']
        # print(img_url)
        hem_img = f"{url}/{img_url}"
        # print(hem_img)
        browser.visit(hem_img)
        soup_1 = bs(browser.html,'html.parser')
        listing_3 = soup_1.find('img', class_='wide-image')['src']
        final_url = f"{url}/{listing_3}"
        # print(final_url)
        hemisphere_image.append(final_url)
        print(hemisphere_image)

    j = 0
    py_list = []
    for i in titles:
        py_dicts = {
            'Hemisphere_Img': hemisphere_image[j],
            'image_title': i
        }
        j=j+1
        py_list.append(py_dicts)

    return py_list
