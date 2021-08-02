import bs4
from bs4 import BeautifulSoup
import requests
from lxml import html
import pandas as pd

# define url as trulia with desired search parameters webpage
url = 'https://www.trulia.com/for_rent/06059_c/3p_beds/2p_baths/0-3600_price/price;a_sort/garage_bamenities/lg_dogs,sm_dogs_pets/'

# get url returned as a Response object
response = requests.get(url)
html_bytes = response.text

# create beautifulsoup object using html parser
soup = BeautifulSoup(html_bytes, 'lxml')

'''
For Trulia, I had to scrape each div tag individually because the data was buried within each card, rather than a nice table'''

pad, cost, rooms, bathrooms, = [], [], [], []

# scrape for all the listing items
streets = soup.find_all('div', attrs={"data-testid": "property-street"})
for street in streets:
	pad.append(street.text)

prices = soup.find_all('div', attrs={"data-testid": "property-price"})
for price in prices:
	cost.append(price.text)

beds = soup.find_all('div', attrs={"data-testid": "property-beds"})
for bed in beds:
	rooms.append(bed.text)

baths = soup.find_all('div', attrs={"data-testid": "property-baths"})
for bath in baths:
	bathrooms.append(bath.text)

d = {"address": pad, "price": cost, "beds": rooms, "bathrooms": bathrooms}
print('TRULIA LISTINGS: (' + url + ')')
print(pd.DataFrame(d))

# for row in rows:
# 	pad = soup.find('div', attrs={"data-testid": "property-street"}).text
# 	price = soup.find('div', attrs={"data-testid": "property-price"}).text
# 	bed = soup.find('div', attrs={"data-testid": "property-beds"}).text
# 	bath = soup.find('div', attrs={"data-testid": "property-baths"}).text

# 	print(pad + ' ' + price + ' ' + bed + ' ' + bath)

'''
rows = soup.find_all('li', attrs={'width': '1,1,0.5,1,0.5'})

pads = []
space = ['/mo', 'Ln', 'Pl', 'Dr', 'Ave', 'St', 'Ct', 'bd', 'ba', 'sqft']
for row in rows:
	a = row.text[row.text.find('$'):row.text.find('Check Availability')]
	if a != '':
		for r in space:
			a = a.replace(r,r + ', ')
			a = a.replace('$','').replace('/mo','')
		pads.append(a)

print(len(pads),pads)
'''


#########################
'''
listings = soup.body.find('ul', attrs={"class": 'Grid__GridContainer-sc-144isrp-1 bQSVOQ'}).find_all('li', attrs={'width': '1,1,0.5,1,0.5'})


# streets = grid.find_all('div', attrs={"data-testid": "property-street"})

prices = grid.find_all('div', attrs={"data-testid": "property-price"})

pads = []

for price in prices:
	pads.append(int(street.text[1:street.text.find('/')].replace(',','')))

print(type(pads[1]))
'''

##########################
# properties = soup.find_all('li', attrs={"width": "1,1,0.5,1,0.5"})
# streets = soup.find_all('div', attrs={"data-testid": "property-street"})

# print(type(streets))
# <a href="/p/ca/huntington-beach/5142-warner-ave-110-huntington-beach-ca-92649--2081191429" data-testid="property-card-link" class="PropertyCard__StyledLink-m1ur0x-3 dgzfOv"><div data-testid="property-street" title="5142 Warner Ave #110" class="Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 dZyoXR">5142 Warner Ave #110</div><div data-testid="property-region" title="Huntington Beach, CA" class="Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 dZyoXR">Huntington Beach, CA</div></a>