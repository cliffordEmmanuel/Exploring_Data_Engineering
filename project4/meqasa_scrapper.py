"""
This script provides scrapes the real estate listings webpage: meqasa https://meqasa.com/houses-for-rent-in-ghana
to collect information for houses up for rent in Ghana.
Results are saved into a csv file for further analysis.
"""


import re
import datetime
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def house_info(houses):
    """
    This method scrapes the first page of the meqasa house listings for housing information..
    """
    house_names = []
    house_beds = []
    house_showers = []
    house_garages = []
    house_areas = []
    house_descriptions = []
    house_prices = []
    currencies = []
    rent_periods = []
    house_urls = []
    house_address = []
    posted_times = []
    
    for listing in houses:
        url = base_url + listing.find('a').attrs['href']
        property_name = listing.find('h2').text.strip()
        address = listing.find('h2').text.strip().split('for rent at ')[1]
        bed = isNone(listing.find('li', {'class':'bed'}))
        shower = isNone(listing.find('li',{'class': 'shower'}))  
        garage = isNone(listing.find('li', {'class': 'garage'}))
        area = isNone(listing.find('li', {'class': 'area'})) 
        price, currency, rent_period = isPriceQuoted(listing.find('p',{'class': 'h3'}).text)     
        
        
        # clicking the listing page to get the description and the updated time info
        current_item = requests.get(url)
        current_item_soup = BeautifulSoup(current_item.content, 'lxml')
        house = current_item_soup.find('div', {'class': 'bottom-one-column-details'})
        description = house.find('div', {'class': 'description'}).find('p').text
        posted_time = current_item_soup.find('p', {'class':'listed-by-text'}).text.replace('Updated on ', '').replace(' by:', '')

        
        # alright now putting everything inside append all the info
        house_names.append(property_name)
        house_beds.append(bed)
        house_showers.append(shower)
        house_garages.append(garage)
        house_areas.append(area)
        house_descriptions.append(description)
        house_prices.append(price)
        currencies.append(currency)
        rent_periods.append(rent_period)
        house_urls.append(url)
        house_address.append(address)
        posted_times.append(posted_time)
        
    # now creating a dataframe of the lists
    df_houses = pd.DataFrame({'Property' : house_names,
                              'Beds' : house_beds,
                              'Showers' : house_showers,
                              'Garages' : house_garages,
                              'Areas' : house_areas,
                              'Description' : house_descriptions,
                              'Price' : house_prices,
                              'Currency' : currencies,
                              'Rent_period' : rent_periods,
                              'Url' : house_urls,
                              'Address' : house_address,
                              'Time_posted' : posted_times})
    return(df_houses)


def isNone(var):
    """
    This is just a utility function to check if element contains a value or not.
    """
    if var is None:
        return 0
    else:
        return var.text


def isPriceQuoted(var):
    """
    This is a utility function to get the price, rent_period and currency from the p element quoted as price.
    """
    if 'GH₵' in var:
        n = var.strip().replace('PriceGH₵', '').split('/')
        price = n[0].strip() # getting the price
        rent_period = n[1].strip()  # getting the rent_period
        currency = 'GH₵'
    elif '$' in var:
        m = var.strip().replace('Price$', '').split('/')
        price = m[0].strip()  # getting the price
        rent_period = m[-1].strip()  # getting the rent_period
        currency = '$'
    else:
        price = 'disclosed on request'
        currency = 'disclosed on request'
        rent_period = 'disclosed on request'
    return price, currency, rent_period


def save_data(df):
    """
    Saves results to a csv adding the timestamp to the file name.
    """
    file_time = datetime.datetime.now()
    file_time = file_time.strftime('%Y-%m-%d')
    file_name = 'meqasa_'+file_time+'.csv'
    
    df.to_csv(file_name, index=False)

df_final = pd.DataFrame([])
base_url = 'https://meqasa.com/'
results = requests.get('https://meqasa.com/houses-for-rent-in-ghana')
soup = BeautifulSoup(results.content, 'lxml')
houses = soup.find_all('div', {'class': 'row mqs-featured-prop-inner-wrap clickable'})

if __name__ == "__main__":
    df_final = house_info(houses)
    save_data(df_final)