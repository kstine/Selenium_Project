'''
Created on Jan 11, 2017

@author: kstine
'''

import requests

urls = ['https://www.irs.gov/pub/irs-soi/eo1.csv', 'https://www.irs.gov/pub/irs-soi/eo2.csv', 'https://www.irs.gov/pub/irs-soi/eo3.csv']

for url in urls:
    print ("downloading: " + url)
    r = requests.get(url)
    with open(url[-7:] , "wb") as code:
        code.write(r.content)
