#!/usr/bin/env python
# coding: utf-8

# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# ## Create connection to NASA browser and soup

# Set up splinter
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

# Set browser variable for init_browser() function
browser = init_browser()
# Set mars varibable as list to store scrape results
mars = {}

# Create function to scrape latest news title and subtext
def latest_news():
        
    # Create variable for 'https://mars.nasa.gov/news/' to scrape
    nasa_url = 'https://mars.nasa.gov/news/'
    # Create connection to browser to scrape current data. Using browser.visit() with nasa_url as argument.
    browser.visit(nasa_url)

    # Create variable to pull html from browser. Using browser.html() with nasa_url as argument
    html = browser.html
    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')   

    # NASA Mars News
    # Scrape latest article title and subtext
    # Create results vaiable to narrow search for news title and subtext 
    results = soup.find_all('ul', class_="item_list")
    # for loop results to scrape news_title and news_p
    for result in results:
        # try and expect to handle any errors
        try:
            # Create variable for news_title from result. Store to mars list. 
            mars["news_title"] = result.find('div', class_="content_title").text
            # Create variable for news_p from result. Store to mars list.              
            mars["news_p"] = result.find('div', class_="rollover_description_inner").text
            
        except AttributeError as e:
            print(e)
    # Print that scrape is complete to server           
    print("Latest News Scrape Completed")
    # return to mars
    return mars

## Create connection to JPL browser and soup
# Create function to scrape featured image url
def featured_image():
    # Create variable for 'https://www.jpl.nasa.gov/spaceimages/' to scrape
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/'
    # Create connection to browser to scrape current data. Using browser.visit() with jpl_url as argument.
    browser.visit(jpl_url)
    # Use .links.find_by_partial_text.() with 'FULL IMAGE' argument and .click() to click on that buttom and take us to the right page
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # Create variable to pull html from browser. Using browser.html() with url as argument
    html = browser.html
    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')  

    # ## JPL Mars Space Images - Featured Image
    # Create results vaiable to narrow search for latest featured image url
    image_results = soup.find_all('a', class_="button")
    # for loop image_results to scrape image_url and featured_image_url
    for image in image_results:
        # Create variable to extract image_url 
        image_url = image('data-fancybox-href')
        # Create variale for jpl base url
        jpl_image_url = 'https://www.jpl.nasa.gov'
        # Create variable for featured_image_url. Store to mars list.
        mars["featured_image_url"] = f'{jpl_image_url}{image_url}'
    # Print that scrape is complete to server   
    print("Image Scrape Complete") 
    # return to mars
    return mars

    # Mars Facts
def mars_facts():
    # Create variable for mars url 
    mars_url = "https://space-facts.com/mars/"
    # Using pd.read_html() with mars_url as argument to read in table
    mars_tables = pd.read_html(mars_url)

    # Create Dataframe to store mars_tables
    # Create DF for first table
    df = mars_tables[0]
    # Identify DF colmumns
    df.columns = ['0', '1']
    # Create variable after convrting df to_html()
    mars_facts = df.to_html()
    # Create variable for mars_facts. Store to mars list.
    mars["mars_facts"] = mars_facts
    # Print that scrape is complete to server   
    print("Mars Facts Complete")
    # return mars
    return mars
    
    # Mars Hemispheres
def mars_hem():
    # Create connection and soup for Cerberus Hemisphere
    # Create base url for each image
    usgs_base_url = 'https://astrogeology.usgs.gov'

    # Create variable for 'https://mars.nasa.gov/news/' to scrape
    mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Create connection to browser to scrape current data. Using browser.visit() mars_with url as argument.
    browser.visit(mars_url)
    # Use .links.find_by_partial_text.() with 'Cerberus Hemisphere Enhanced' argument and .click() to click on that buttom and take us to the right page
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()

    # Create variable to pull html from browser. Using browser.html() with url as argument
    html = browser.html
    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')   

    # Create results vaiable to narrow search for Cerberus Hemisphere Enhanced title and link
    cerberus_results = soup.find_all('div', class_="container")
    # for loop cerberus_results to scrape Cerberus Hemisphere Enhanced title and link
    for cerberus in cerberus_results:
        
        # Create path to extract cerberus_link
        locate_div = cerberus.find('div', class_="wide-image-wrapper")
        locate_img = locate_div.img
        # Create variable for cerberus_link results
        cerberus_link = locate_img['src']
        
        # Create path to extraxt cerberus_title
        locate_title = cerberus.find('div', class_="content")
        # Create variable for cerberus_title results
        cerberus_title = locate_title.h2.text
    # Print that scrape is complete to server    
    print("Cerberus Scrape Complete")
    # ## Create connection and soup for Schiaparelli Hemisphere

    # Create variable for 'https://mars.nasa.gov/news/' to scrape
    mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Create connection to browser to scrape current data. Using browser.visit() with url as argument.
    browser.visit(mars_url)
    # Use .links.find_by_partial_text.() with 'Schiaparelli Hemisphere Enhanced' argument and .click() to click on that buttom and take us to the right page
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()

    # Create variable to pull html from browser. Using browser.html() with url as argument
    html = browser.html
    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')   

    # Create results vaiable to narrow search for Schiaparelli Hemisphere Enhanced title and link
    schiaparelli_results = soup.find_all('div', class_="container")
    # for loop schiaparelli_results to scrape Schiaparelli Hemisphere Enhanced title and link
    for schiaparelli in schiaparelli_results:
        
        # Create path to schiaparelli_link
        locate_div = schiaparelli.find('div', class_="wide-image-wrapper")
        locate_img = locate_div.img
        # Create variable for schiaparelli_link results
        schiaparelli_link = locate_img['src']
        
        # Creat path to schiaparelli_title
        locate_title = schiaparelli.find('div', class_="content")
        # Create variable for schiaparelli_title results
        schiaparelli_title = locate_title.h2.text
    # Print that scrape is complete to server
    print("Schiaparelli Scrape Complete")
    # ## Create connection and soup for Syrtis Major Hemisphere

    # Create variable for 'https://mars.nasa.gov/news/' to scrape
    mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Create connection to browser to scrape current data. Using browser.visit() with url as argument.
    browser.visit(mars_url)
    # Use .links.find_by_partial_text.() with 'Syrtis Major Hemisphere Enhanced' argument and .click() to click on that buttom and take us to the right page
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()

    # Create variable to pull html from browser. Using browser.html() with url as argument
    html = browser.html
    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')   

    # Create results vaiable to narrow search for Syrtis Major Hemisphere Enhanced title and link
    syrtis_results = soup.find_all('div', class_="container")
    # for loop syrtis_results to scrape Syrtis Major Hemisphere Enhanced title and link
    for syrtis in syrtis_results:
        
        # Create path to extraxt syrtis_link
        locate_div = syrtis.find('div', class_="wide-image-wrapper")
        locate_img = locate_div.img
        # Create variable for syrtis_link results
        syrtis_link = locate_img['src']
        
        # Create path to extraxt syrtis_title
        locate_title = syrtis.find('div', class_="content")
        # Create variable for syrtis_title results
        syrtis_title = locate_title.h2.text
    # Print that scrape is complete to server
    print("Syrtis Major Scrape Complete")    
    # ## Create connection and soup for Valles Marineris Hemisphere

    # Create variable for 'https://mars.nasa.gov/news/' to scrape
    mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Create connection to browser to scrape current data. Using browser.visit() with url as argument.
    browser.visit(mars_url)
    # Use .links.find_by_partial_text.() with 'Valles Marineris Hemisphere Enhanced' argument and .click() to click on that buttom and take us to the right page
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()

    # Create variable to pull html from browser. Using browser.html() with url as argument
    html = browser.html
    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')   

    # Create results vaiable to narrow search for Valles Marineris Hemisphere Enhanced title and link
    valles_marineris_results = soup.find_all('div', class_="container")
    # for loop valles_marineris_results to scrape Valles Marineris Hemisphere Enhanced title and link
    for valles_marineris in valles_marineris_results:
        
        # Create path to extract valles_marineris_link
        locate_div = valles_marineris.find('div', class_="wide-image-wrapper")
        locate_img = locate_div.img
        # Create variable for valles_marineris_link results
        valles_marineris_link = locate_img['src']
        
        # Create path to extract valles_marineris_title
        locate_title = valles_marineris.find('div', class_="content")
        # Create variable for valles_marineris_title results
        valles_marineris_title = locate_title.h2.text
    # Print that scrape is complete to server
    print("Valles Marineris Complete")   

    # ## Hemisphere image urls
    # Create dictionary with all the Mars titles and url links
    hemisphere_image_urls = [
        {'title': cerberus_title, 'img_url': f'{usgs_base_url}{cerberus_link}'},
        {'title': schiaparelli_title, 'img_url': f'{usgs_base_url}{schiaparelli_link}'},
        {'title': syrtis_title, 'img_url': f'{usgs_base_url}{syrtis_link}'},
        {'title': valles_marineris_title, 'img_url': f'{usgs_base_url}{valles_marineris_link}'}
    ]
    # Create variable for hemisphere_image_urls. Store to mars list
    mars["hemisphere_image_urls"] = hemisphere_image_urls
    # return mars
    return mars
    





