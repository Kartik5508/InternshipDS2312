# Web Scrapping Assignment-3


```python
!pip install selenium
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: selenium in c:\users\le\appdata\roaming\python\python310\site-packages (4.17.2)
    Requirement already satisfied: certifi>=2021.10.8 in c:\programdata\anaconda3\lib\site-packages (from selenium) (2022.12.7)
    Requirement already satisfied: urllib3[socks]<3,>=1.26 in c:\programdata\anaconda3\lib\site-packages (from selenium) (1.26.14)
    Requirement already satisfied: trio-websocket~=0.9 in c:\users\le\appdata\roaming\python\python310\site-packages (from selenium) (0.11.1)
    Requirement already satisfied: trio~=0.17 in c:\users\le\appdata\roaming\python\python310\site-packages (from selenium) (0.24.0)
    Requirement already satisfied: typing_extensions>=4.9.0 in c:\users\le\appdata\roaming\python\python310\site-packages (from selenium) (4.9.0)
    Requirement already satisfied: cffi>=1.14 in c:\programdata\anaconda3\lib\site-packages (from trio~=0.17->selenium) (1.15.1)
    Requirement already satisfied: sortedcontainers in c:\programdata\anaconda3\lib\site-packages (from trio~=0.17->selenium) (2.4.0)
    Requirement already satisfied: exceptiongroup in c:\users\le\appdata\roaming\python\python310\site-packages (from trio~=0.17->selenium) (1.2.0)
    Requirement already satisfied: attrs>=20.1.0 in c:\programdata\anaconda3\lib\site-packages (from trio~=0.17->selenium) (22.1.0)
    Requirement already satisfied: sniffio>=1.3.0 in c:\users\le\appdata\roaming\python\python310\site-packages (from trio~=0.17->selenium) (1.3.0)
    Requirement already satisfied: outcome in c:\users\le\appdata\roaming\python\python310\site-packages (from trio~=0.17->selenium) (1.3.0.post0)
    Requirement already satisfied: idna in c:\programdata\anaconda3\lib\site-packages (from trio~=0.17->selenium) (3.4)
    Requirement already satisfied: wsproto>=0.14 in c:\users\le\appdata\roaming\python\python310\site-packages (from trio-websocket~=0.9->selenium) (1.2.0)
    Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in c:\programdata\anaconda3\lib\site-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)
    Requirement already satisfied: pycparser in c:\programdata\anaconda3\lib\site-packages (from cffi>=1.14->trio~=0.17->selenium) (2.21)
    Requirement already satisfied: h11<1,>=0.9.0 in c:\users\le\appdata\roaming\python\python310\site-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)
    


```python
import pandas as pd
import selenium
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
import requests
import re
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
```

Ques1-Write a python program which searches all the product under a particular product from www.amazon.in. The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for guitars.


```python
driver=webdriver.Edge()
```


```python
url = "https://www.amazon.in/"

```


```python
driver.get(url)
```


```python
user_input = input('Enter the product that we want to search : ')
```

    Enter the product that we want to search : Guitar
    


```python
search = driver.find_element(By.ID,"twotabsearchtextbox")
search

```




    <selenium.webdriver.remote.webelement.WebElement (session="fd9a449dc5b8b56895f97b99a73e70c9", element="ADFB65D9375490A346E68111FE4067F1_element_15")>




```python
search.send_keys(user_input)
```


```python
search_btn = driver.find_element(By.XPATH,"//div[@class='nav-search-submit nav-sprite']/span/input")

# clicking on search button
search_btn.click()
```

Ques2-In the above question, now scrape the following details of each product listed in first 3 pages of your search 
results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then 
scrape all the products available under that product name. Details to be scraped are: "Brand 
Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
“Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 


```python
urls = []          # empty list
for i in range(0,3):      # for loop to scrape 3 pages
    page_url = driver.find_elements(By.XPATH,"//a[@class='a-link-normal a-text-normal']")
    for i in page_url:
        urls.append(i.get_attribute("href"))
        next_btn = driver.find_element(By_XPATH,"//li[@class='a-last']/a")
        time.sleep(3)
urls
```




    []




```python
len(urls)
```




    0



I am facing problem into it, It is giving me an error

Ques3 Write a python program to access the search bar and search button on images.google.com and scrape 10 
images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’


```python
# geting the webpage of mentioned url
url = "http://images.google.com/"

# creating empty list
urls = []
data = []

search_item = ["Fruits","Cars","Machine Learning"]
for item in search_item:
    driver.get(url)
    time.sleep(5)
    
    # finding webelement for search_bar
    search_bar = driver.find_element_By_tagName("input")
    
    # sending keys to get the keyword for search bar
    search_bar.send_keys(str(item))
    
    # clicking on search button
    search_button = driver.find_element_by_xpath("//button[@class='Tg7LZd']").click()
    
    # scroling down the webpage to get some more images
    for _ in range(500):
        driver.execute_script("window.scrollBy(0,100)")
        
        imgs = driver.find_elements_by_xpath("//img[@class='rg_i Q4LuWd']")
    img_url = []
    for image in imgs:
        source = image.get_attribute('src')
        if source is not None:
            if(source[0:4] == 'http'):
                img_url.append(source)
    for i in img_url[:100]:
        urls.append(i)
        
for i in range(len(urls)):
    if i >= 300:
        break
    print("Doenloading {0} of {1} images" .format(i,300))
    response = requests.get(urls[i])
    
    file = open(r"E:\google\images"+str(i)+".jpg","wb")
    
    file.write(response.content)

```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[58], line 14
         11 time.sleep(5)
         13 # finding webelement for search_bar
    ---> 14 search_bar = driver.find_element_By_tagName("input")
         16 # sending keys to get the keyword for search bar
         17 search_bar.send_keys(str(item))
    

    AttributeError: 'WebDriver' object has no attribute 'find_element_By_tagName'


i am unable to solve this error

Q4 : Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, “Secondary Camera”, “Display Size”, “Display Resolution”, “Processor”, “Processor Cores”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV.

I am unable to solve this code

Q5 : Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.


```python
driver=webdriver.Edge()
```


```python
url = 'https://www.google.co.in/maps'
driver.get(url)
time.sleep(2)
```


```python
City = input('Enter City name that has to be searched : ')
search_bar = driver.find_element(By.ID,'searchboxinput')
search_bar.click()
time.sleep(2)

#sending keys to find cities
search_bar.send_keys(City)

#checking for webelement and clicking on search button
search_btn = driver.find_element(By.ID,'searchbox-searchbutton')
search_btn.click()
time.sleep(2)

try:
    url_str = driver.current_url
    print("URL Extracted: ", url_str)
    latitude_longitude = re.findall(r'@(.*)data',url_str)
    if len(latitude_longitude):
        lat_lng_list = latitude_longitude[0].split(",")
        if len(lat_lng_list)>=2:
            latitude = lat_lng_list[0]
            longitude = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(latitude, longitude))
except Exception as e:
        print("Error: ", str(e))
```

    Enter City name that has to be searched : jaipur
    URL Extracted:  https://www.google.co.in/maps/place/Jaipur,+Rajasthan/@26.8848282,75.4608793,10z/data=!3m1!4b1!4m6!3m5!1s0x396c4adf4c57e281:0xce1c63a0cf22e09!8m2!3d26.9124336!4d75.7872709!16zL20vMDE2NzIy?entry=ttu
    Latitude = 26.8848282, Longitude = 75.4608793
    

Ques6: Write a program to scrap all the available details of best gaming laptops from digit.in.

I am unable to do it 

Ques7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
“Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”

Ques8 Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted 
from any YouTube Video. 
9. Write a python program to s

9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
“London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
reviews, privates from price, dorms from price, facilities and property description.

I having lots of problem in exception handling, I have a so much doubt into it< I will clear it in doubt clearing session. I am working on it


```python

```
