# Webscraping has been block by many websites using CaptCha
# work arounds exists
# most real estate sites have downloadable data in csv format redfin and zillow

import requests
from bs4 import BeautifulSoup
import pandas as pd

sanJoseZipCodes = [94089, 95002, 95008, 95013, 95014, 95032, 95035, 95037, 95050, 95054, 95070, 95110, 95111, 95112, 95113, 95116, 95117, 95118, 95119, 95120, 95121, 95122, 95123, 95124, 95125, 95126, 95127, 95128, 95129, 95130, 95131, 95132, 95133, 95134, 95135, 95136, 95138, 95139, 95140, 95148]

req = requests.get('https://www.century21.com/real-estate/san-jose-ca/LCCASANJOSE')
#req = requests.get('https://www.zillow.com/homes/for_sale/{0}/0_singlestory/days_sort'.format(sanJoseZipCodes[0]))
#req = requests.get('https://www.zillow.com/homes/for_sale/{0}/0_singlestory/days_sort'.format(zipcode))

content = req.content

csvEntryList = []
addrList = []
cityList = []
sqftList = []
priceList = []
bedList = []
bathList = []

def parsePropertyPrimaryInfo(tag):
	
	priceList.append(tag.find("a",'listing-price').get_text(",",strip=True))
	bedList.append(tag.find('div','property-beds').get_text(",",strip=True))
	bathList.append(tag.find('div','property-baths').get_text(",",strip=True))
	sqftList.append(tag.find('div','property-sqft').get_text(",",strip=True))
	addrList.append(tag.find('div','property-address').get_text(",",strip=True))
	cityList.append(tag.find('div','property-city').get_text(",",strip=True))


def buildDictionary():
	d = {}
#	PropColumns=['CITY','ADDRESS','SQ FT','PRICE','BEDS','BATHS']
	d['CITY'] = cityList
	d['ADDRESS'] = addrList
	d['SQ FT'] = sqftList
	d['PRICE'] = priceList
	d['BEDS'] = bedList
	d['BATHS'] = bathList
	return d                

def buildDataFrame ():
	PropColumns=['CITY','ADDRESS','SQ FT','PRICE','BEDS','BATHS']
	data = buildDictionary()
	df = pd.DataFrame(data)
	return df

if "Captcha" in req.text:
    print ("we've been blocked")
else:
	soup = BeautifulSoup(content,'html.parser')
	# print(soup.prettify())
	count =1
	table = {}
	# Century 21 <div class="property-card-primary-info">
	for tag in soup.find_all('div','property-card-primary-info'):
		parsePropertyPrimaryInfo(tag)

	buildDataFrame().to_csv('century21_estates.csv')

	
