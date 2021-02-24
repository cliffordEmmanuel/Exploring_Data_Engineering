"""
This script provides scrapes an eccomerce platform for ads on electronic devices: tonaton https://tonaton.com/en
Results are saved into a csv file for further analysis.
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime


def device_info(device_ads):
    """this function extracts the attributes for each ads and returns the result in a dataframe"""
    
    # create the lists for all attributes
    devices_name_list = []
    locations_list = []
    category_list = []
    currency_list = []
    price_list = []
    
    for ad in device_ads:
        # getting each attributes
        device_name = ad.find('span',{'class':'title--3yncE'}).text
        location    = ad.find('div', {'class': 'description--2-ez3'}).text.split(',')[0]
        category    = ad.find('div', {'class': 'description--2-ez3'}).text.split(',')[1]
        currency    = ad.find('div', {'class': 'price--3SnqI color--t0tGX'}).text.split(' ')[0]
        price       = ad.find('div', {'class': 'price--3SnqI color--t0tGX'}).text.split(' ')[1]
        
        # appending to a list
        devices_name_list.append(device_name)
        locations_list.append(location)
        category_list.append(category)
        currency_list.append(currency)
        price_list.append(price)

    
    # putting the results in a dataframe
    df_devices = pd.DataFrame({'DeviceName': devices_name_list, 
                               'Category': category_list,
                               'LocationPosted': locations_list,
                               'Price': price_list,
                               'Currency': currency_list })
    return df_devices

def next_page(page_number, url):
    """this function returns the next page to be scraped to be scraped"""
    next_url = url + '?by_paying_member=0&sort=date&buy_now=0&page=' + str(page_number)
    page = requests.get(next_url)
    if page.status_code == 200:
        print(f'Sraping page {page_number}...')
    else:
        print('Error occured in page load')
        
    return page


# saving to a csv file..
def save_data(df):
    """this function converts a dataframe into a csv file appending the current date and time """
    file_time = datetime.datetime.now()
    file_time = file_time.strftime('%Y-%m-%d')
    file_name = 'Electronics_Ads_tonaton'+file_time+'.csv'
    
    df.to_csv(file_name, index=False) 
    
    
# method for scraping
def scrape_data(url, number_of_pages):
    """this function takes in the url of the website and the number of pages to be scraped and returns a csv file of the scraped information"""
    
    for page_num in range(1, number_of_pages+1):
        page = next_page(page_num, url)
        
        # Store the webpage content into a variable 
        src = page.content
        # Step 3: Initialize the beautiful soup object with the src variable
        soup = BeautifulSoup(src, 'lxml')
    
        # getting the ads 
        device_ads = soup.find_all('li', {'class':'normal--2QYVk gtm-normal-ad'})

        # extract the data from the ads
        df = device_info(device_ads)
        global scraped_data_df
        scraped_data_df = scraped_data_df.append(df)
    
    # save to csv format
    save_data(scraped_data_df)
    print('Scraping Complete!!\nFile Saved')

if __name__ == "__main__":
    scraped_data_df = pd.DataFrame([])
    url = 'https://www.tonaton.com/en/ads/ghana/electronics'

    number_of_pages = int(input('Enter the number of pages to be scraped...'))

    print('**********************')
    print('***Scraping tonaton***')
    scrape_data(url, number_of_pages)