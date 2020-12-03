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
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():

    browser = init_browser()
    mission_to_mars_data = {}

    # Create variable for 'https://mars.nasa.gov/news/' to scrape
    nasa_url = 'https://mars.nasa.gov/news/'

    # Create connection to browser to scrape current data. Using browser.visit() with url as argument.
    browser.visit(nasa_url)

    # Create variable to pull html from browser. Using browser.html() with url as argument
    html = browser.html

    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')   

    # Print soup with .prettify()
    print(soup.prettify())

    # Quit browser
    browser.quit()

    # # NASA Mars News
    # Scrape latest article title and subtext

    # Create results vaiable to narrow search for news title and subtext 
    results = soup.find_all('ul', class_="item_list")

    # for loop results to scrape news_title and news_p
    for result in results:
        # try an dexpect to handle any errors
        try:
            # variable for news_title from result 
            news_title = result.find('div', class_="content_title").text
            # variable for news_p from result              
            news_p = result.find('div', class_="rollover_description_inner").text
            
            # print results
            if (news_title and news_p):
                print('--------------------------------------------')
                print(news_title)
                print('--------------------------------------------')
                print(news_p)
                print('--------------------------------------------')
        except AttributeError as e:
            print(e)
    # State that scrape is complete           
    print("Scrape Completed")
            
    # ## Create connection to JPL browser and soup

    # Set up splinter for JPL
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Create variable for 'https://www.jpl.nasa.gov/spaceimages/' to scrape
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/'

    # Create connection to browser to scrape current data. Using browser.visit() with url as argument.
    browser.visit(jpl_url)

    # Use .links.find_by_partial_text.() with 'FULL IMAGE' argument and .click() to click on that buttom and take us to the right page
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # Create variable to pull html from browser. Using browser.html() with url as argument
    html = browser.html

    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')  

    print(soup.prettify())

    # Quit browser
    browser.quit()

    # ## JPL Mars Space Images - Featured Image

    # Create results vaiable to narrow search for latest featured image
    image_results = soup.find_all('a', class_="button")
    image_results

    # for loop image_results to scrape image_url and featured_image_url
    for image in image_results:
        # Create variable to extract image_url and featured_image_url
        image_url = image['data-fancybox-href']
        featured_image_url = f'https://www.jpl.nasa.gov{image_url}'
        
    # Display featured_image_url and test link works
    featured_image_url

    # ## Mars Facts

    # Create variable for mars url 
    mars_url = "https://space-facts.com/mars/"

    # Using pd.read_html() with mars_url as argument to read in table
    tables = pd.read_html(mars_url)
    tables
    
    # ## Mars Hemispheres
    
    # ## Create connection and soup for Cerberus Hemisphere

    # Set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # creat base url for each image
    usgs_base_url = 'https://astrogeology.usgs.gov'

    # Create variable for 'https://mars.nasa.gov/news/' to scrape
    mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Create connection to browser to scrape current data. Using browser.visit() with url as argument.
    browser.visit(mars_url)

    # Use .links.find_by_partial_text.() with 'Cerberus Hemisphere Enhanced' argument and .click() to click on that buttom and take us to the right page
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()

    # Create variable to pull html from browser. Using browser.html() with url as argument
    html = browser.html

    # Create soup with bs() with html vairable 
    soup = bs(html, 'html.parser')   

    # Print soup with .prettify()
    print(soup.prettify())

    # Quit browser
    browser.quit()

    # Create results vaiable to narrow search for Cerberus Hemisphere Enhanced title and link
    cerberus_results = soup.find_all('div', class_="container")

    # for loop cerberus_results to scrape Cerberus Hemisphere Enhanced title and link
    for cerberus in cerberus_results:
        
        # Create path to extract cerberus_link
        locate_div = cerberus.find('div', class_="wide-image-wrapper")
        locate_img = locate_div.img
        cerberus_link = locate_img['src']
        
        # Create path to extraxt cerberus_title
        locate_title = cerberus.find('div', class_="content")
        cerberus_title = locate_title.h2.text

    # Display variables
    print(cerberus_title)
    print(cerberus_link)

    # ## Create connection and soup for Schiaparelli Hemisphere

    # Set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

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

    # Print soup with .prettify()
    print(soup.prettify())

    # Quit browser
    browser.quit()

    # Create results vaiable to narrow search for Schiaparelli Hemisphere Enhanced title and link
    schiaparelli_results = soup.find_all('div', class_="container")

    # for loop schiaparelli_results to scrape Schiaparelli Hemisphere Enhanced title and link
    for schiaparelli in schiaparelli_results:
        
        # Create path to schiaparelli_link
        locate_div = schiaparelli.find('div', class_="wide-image-wrapper")
        locate_img = locate_div.img
        schiaparelli_link = locate_img['src']
        
        # Creat path to schiaparelli_title
        locate_title = schiaparelli.find('div', class_="content")
        schiaparelli_title = locate_title.h2.text
        
    # Display variables
    print(schiaparelli_title)
    print(schiaparelli_link)

    # ## Create connection and soup for Syrtis Major Hemisphere

    # Set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

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

    # Print soup with .prettify()
    print(soup.prettify())

    # Quiut browser
    browser.quit()

    # Create results vaiable to narrow search for Syrtis Major Hemisphere Enhanced title and link
    syrtis_results = soup.find_all('div', class_="container")

    # for loop syrtis_results to scrape Syrtis Major Hemisphere Enhanced title and link
    for syrtis in syrtis_results:
        
        # Create path to extraxt syrtis_link
        locate_div = syrtis.find('div', class_="wide-image-wrapper")
        locate_img = locate_div.img
        syrtis_link = locate_img['src']
        
        # Create path to extraxt syrtis_title
        locate_title = syrtis.find('div', class_="content")
        syrtis_title = locate_title.h2.text
        
    # Display variables
    print(syrtis_title)
    print(syrtis_link)

    # ## Create connection and soup for Valles Marineris Hemisphere

    # Set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

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

    # Print soup with .prettify()
    print(soup.prettify())

    # Quit browser
    browser.quit()

    # Create results vaiable to narrow search for Valles Marineris Hemisphere Enhanced title and link
    valles_marineris_results = soup.find_all('div', class_="container")

    # for loop valles_marineris_results to scrape Valles Marineris Hemisphere Enhanced title and link
    for valles_marineris in valles_marineris_results:
        
        # Create path to extract valles_marineris_link
        locate_div = valles_marineris.find('div', class_="wide-image-wrapper")
        locate_img = locate_div.img
        valles_marineris_link = locate_img['src']
        
        # Create path to extract valles_marineris_title
        locate_title = valles_marineris.find('div', class_="content")
        valles_marineris_title = locate_title.h2.text
        
    # Display variables
    print(valles_marineris_title)
    print(valles_marineris_link)

    # ## Hemisphere image urls

    # Create dictionary with all the Mars titles and url links
    hemisphere_image_urls = [
        {'title': cerberus_title, 'img_url': f'{usgs_base_url}{cerberus_link}'},
        {'title': schiaparelli_title, 'img_url': f'{usgs_base_url}{schiaparelli_link}'},
        {'title': syrtis_title, 'img_url': f'{usgs_base_url}{syrtis_link}'},
        {'title': valles_marineris_title, 'img_url': f'{usgs_base_url}{valles_marineris_link}'}
    ]
    hemisphere_image_urls

    





