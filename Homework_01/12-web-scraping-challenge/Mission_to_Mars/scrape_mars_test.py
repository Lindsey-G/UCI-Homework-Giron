{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 482,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import dependencies\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create connection to NASA browser and soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 483,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 86.0.4240\n",
      "[WDM] - Get LATEST driver version for 86.0.4240\n",
      "[WDM] - Driver [C:\\Users\\The Dark Knight\\.wdm\\drivers\\chromedriver\\win32\\86.0.4240.22\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Set up splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 484,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable for 'https://mars.nasa.gov/news/' to scrape\n",
    "nasa_url = 'https://mars.nasa.gov/news/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 485,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create connection to browser to scrape current data. Using browser.visit() with url as argument.\n",
    "browser.visit(nasa_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 486,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable to pull html from browser. Using browser.html() with url as argument\n",
    "html = browser.html\n",
    "\n",
    "# Create soup with bs() with html vairable \n",
    "soup = bs(html, 'html.parser')   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 544,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print soup with .prettify()\n",
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 488,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Quit browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NASA Mars News\n",
    "Scrape latest article title and subtext"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 489,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create results vaiable to get narrow our search \n",
    "results = soup.find_all('ul', class_=\"item_list\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 490,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---------------\n",
      "MOXIE Could Help Future Rockets Launch Off Mars\n",
      "NASA's Perseverance rover carries a device to convert Martian air into oxygen that, if produced on a larger scale, could be used not just for breathing, but also for fuel.\n",
      "Scrape Completed\n"
     ]
    }
   ],
   "source": [
    "# \n",
    "for result in results:\n",
    "    try:\n",
    "        news_title = result.find('div', class_=\"content_title\").text\n",
    "                      \n",
    "        news_p = result.find('div', class_=\"rollover_description_inner\").text\n",
    "         \n",
    "        \n",
    "        if news_title:\n",
    "            print('---------------')\n",
    "            print(news_title)\n",
    "            print(news_p)\n",
    "    except AttributeError as e:\n",
    "        print(e)\n",
    "            \n",
    "print(\"Scrape Completed\")\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create connection to JPL browser and soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 492,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 86.0.4240\n",
      "[WDM] - Get LATEST driver version for 86.0.4240\n",
      "[WDM] - Driver [C:\\Users\\The Dark Knight\\.wdm\\drivers\\chromedriver\\win32\\86.0.4240.22\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Set up splinter for jpl\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 499,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable for 'https://www.jpl.nasa.gov/spaceimages/' to scrape\n",
    "jpl_url = 'https://www.jpl.nasa.gov/spaceimages/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 500,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create connection to browser to scrape current data. Using browser.visit() with url as argument.\n",
    "browser.visit(jpl_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 501,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.links.find_by_partial_text('FULL IMAGE').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 502,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable to pull html from browser. Using browser.html() with url as argument\n",
    "html = browser.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 503,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create soup with bs() with html vairable \n",
    "soup = bs(html, 'html.parser')  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 545,
   "metadata": {},
   "outputs": [],
   "source": [
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 505,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 506,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<a class=\"button fancybox\" data-description=\"The structure of the Sun's corona shows well in this image from NASA's Solar TErrestrial RElations Observatory (STEREO).\" data-fancybox-group=\"images\" data-fancybox-href=\"/spaceimages/images/mediumsize/PIA09320_ip.jpg\" data-link=\"/spaceimages/details.php?id=PIA09320\" data-title=\"Full Disk Image of the Sun, March 26, 2007\" id=\"full_image\">\n",
       " \t\t\t\t\tFULL IMAGE\n",
       " \t\t\t\t  </a>,\n",
       " <a class=\"button\" href=\"\">\n",
       " \t\t\t\tMORE\n",
       " \t\t\t  </a>,\n",
       " <a class=\"button\" href=\"/spaceimages/details.php?id=PIA09320 \" target=\"_top\">more info     </a>]"
      ]
     },
     "execution_count": 506,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "image_results = soup.find_all('a', class_=\"button\")\n",
    "image_results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 507,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'data-fancybox-href'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-507-ff3766c2103b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#('li', class_=\"fancybox-thumb-active\")\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mimage\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mimage_results\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mimage_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mimage\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'data-fancybox-href'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[0mfeatured_image_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34mf'https://www.jpl.nasa.gov/spaceimages{image_url}'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\bs4\\element.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   1404\u001b[0m         \"\"\"tag[key] returns the value of the 'key' attribute for the Tag,\n\u001b[0;32m   1405\u001b[0m         and throws an exception if it's not there.\"\"\"\n\u001b[1;32m-> 1406\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mattrs\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1407\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1408\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__iter__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'data-fancybox-href'"
     ]
    }
   ],
   "source": [
    "#('li', class_=\"fancybox-thumb-active\")\n",
    "for image in image_results:\n",
    "    image_url = image['data-fancybox-href']\n",
    "    featured_image_url = f'https://www.jpl.nasa.gov/spaceimages{image_url}'\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 508,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/spaceimages/images/mediumsize/PIA09320_ip.jpg'"
      ]
     },
     "execution_count": 508,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 509,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_url = \"https://space-facts.com/mars/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 510,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 510,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(mars_url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Mars Hemispheres\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create connection and soup for Cerberus Hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 547,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 86.0.4240\n",
      "[WDM] - Get LATEST driver version for 86.0.4240\n",
      "[WDM] - Driver [C:\\Users\\The Dark Knight\\.wdm\\drivers\\chromedriver\\win32\\86.0.4240.22\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Set up splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 548,
   "metadata": {},
   "outputs": [],
   "source": [
    "# creat base url for each image\n",
    "usgs_base_url = 'https://astrogeology.usgs.gov'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 549,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable for 'https://mars.nasa.gov/news/' to scrape\n",
    "mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 550,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create connection to browser to scrape current data. Using browser.visit() with url as argument.\n",
    "browser.visit(mars_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 551,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 552,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable to pull html from browser. Using browser.html() with url as argument\n",
    "html = browser.html\n",
    "\n",
    "# Create soup with bs() with html vairable \n",
    "soup = bs(html, 'html.parser')   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 554,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print soup with .prettify()\n",
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 559,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 558,
   "metadata": {},
   "outputs": [],
   "source": [
    "cerberus_results = soup.find_all('div', class_=\"container\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 572,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n",
      "/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\n"
     ]
    }
   ],
   "source": [
    "for cerberus in cerberus_results:\n",
    "    locate_div = cerberus.find('div', class_=\"wide-image-wrapper\")\n",
    "    locate_img = locate_image_div.img\n",
    "    cerberus_link = locate_img['src']\n",
    "    \n",
    "    locate_title = cerberus.find('div', class_=\"content\")\n",
    "    cerberus_title = locate_title.h2.text\n",
    "print(cerberus_title)\n",
    "print(cerberus_link)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create connection and soup for Schiaparelli Hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 573,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 86.0.4240\n",
      "[WDM] - Get LATEST driver version for 86.0.4240\n",
      "[WDM] - Driver [C:\\Users\\The Dark Knight\\.wdm\\drivers\\chromedriver\\win32\\86.0.4240.22\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Set up splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 574,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable for 'https://mars.nasa.gov/news/' to scrape\n",
    "mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 575,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create connection to browser to scrape current data. Using browser.visit() with url as argument.\n",
    "browser.visit(mars_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 576,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 577,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable to pull html from browser. Using browser.html() with url as argument\n",
    "html = browser.html\n",
    "\n",
    "# Create soup with bs() with html vairable \n",
    "soup = bs(html, 'html.parser')   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print soup with .prettify()\n",
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 579,
   "metadata": {},
   "outputs": [],
   "source": [
    "schiaparelli_results = soup.find_all('div', class_=\"container\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 581,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Schiaparelli Hemisphere Enhanced\n",
      "/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\n"
     ]
    }
   ],
   "source": [
    "for schiaparelli in schiaparelli_results:\n",
    "    locate_div = schiaparelli.find('div', class_=\"wide-image-wrapper\")\n",
    "    locate_img = locate_image_div.img\n",
    "    schiaparelli_link = locate_img['src']\n",
    "    \n",
    "    locate_title = schiaparelli.find('div', class_=\"content\")\n",
    "    schiaparelli_title = locate_title.h2.text\n",
    "print(schiaparelli_title)\n",
    "print(schiaparelli_link)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create connection and soup for Syrtis Major Hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 582,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 86.0.4240\n",
      "[WDM] - Get LATEST driver version for 86.0.4240\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Driver [C:\\Users\\The Dark Knight\\.wdm\\drivers\\chromedriver\\win32\\86.0.4240.22\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "# Set up splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 583,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable for 'https://mars.nasa.gov/news/' to scrape\n",
    "mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 584,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create connection to browser to scrape current data. Using browser.visit() with url as argument.\n",
    "browser.visit(mars_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 585,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 586,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable to pull html from browser. Using browser.html() with url as argument\n",
    "html = browser.html\n",
    "\n",
    "# Create soup with bs() with html vairable \n",
    "soup = bs(html, 'html.parser')   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 587,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print soup with .prettify()\n",
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 588,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 589,
   "metadata": {},
   "outputs": [],
   "source": [
    "syrtis_results = soup.find_all('div', class_=\"container\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 590,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Syrtis Major Hemisphere Enhanced\n",
      "/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\n"
     ]
    }
   ],
   "source": [
    "for syrtis in syrtis_results:\n",
    "    locate_div = syrtis.find('div', class_=\"wide-image-wrapper\")\n",
    "    locate_img = locate_image_div.img\n",
    "    syrtis_link = locate_img['src']\n",
    "    \n",
    "    locate_title = syrtis.find('div', class_=\"content\")\n",
    "    syrtis_title = locate_title.h2.text\n",
    "print(syrtis_title)\n",
    "print(syrtis_link)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create connection and soup for Valles Marineris Hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 595,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 86.0.4240\n",
      "[WDM] - Get LATEST driver version for 86.0.4240\n",
      "[WDM] - Driver [C:\\Users\\The Dark Knight\\.wdm\\drivers\\chromedriver\\win32\\86.0.4240.22\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Set up splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 596,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable for 'https://mars.nasa.gov/news/' to scrape\n",
    "mars_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 597,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create connection to browser to scrape current data. Using browser.visit() with url as argument.\n",
    "browser.visit(mars_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 598,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 599,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create variable to pull html from browser. Using browser.html() with url as argument\n",
    "html = browser.html\n",
    "\n",
    "# Create soup with bs() with html vairable \n",
    "soup = bs(html, 'html.parser')   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 600,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print soup with .prettify()\n",
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 601,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 604,
   "metadata": {},
   "outputs": [],
   "source": [
    "valles_marineris_results = soup.find_all('div', class_=\"container\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 605,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valles Marineris Hemisphere Enhanced\n",
      "/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\n"
     ]
    }
   ],
   "source": [
    "for valles_marineris in valles_marineris_results:\n",
    "    locate_div = valles_marineris.find('div', class_=\"wide-image-wrapper\")\n",
    "    locate_img = locate_image_div.img\n",
    "    valles_marineris_link = locate_img['src']\n",
    "    \n",
    "    locate_title = valles_marineris.find('div', class_=\"content\")\n",
    "    valles_marineris_title = locate_title.h2.text\n",
    "print(valles_marineris_title)\n",
    "print(valles_marineris_link)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hemisphere image urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 607,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png'}]"
      ]
     },
     "execution_count": 607,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls = [\n",
    "    {'title': cerberus_title, 'img_url': f'{usgs_base_url}{cerberus_link}'},\n",
    "    {'title': schiaparelli_title, 'img_url': f'{usgs_base_url}{schiaparelli_link}'},\n",
    "    {'title': syrtis_title, 'img_url': f'{usgs_base_url}{syrtis_link}'},\n",
    "    {'title': valles_marineris_title, 'img_url': f'{usgs_base_url}{valles_marineris_link}'}\n",
    "]\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
