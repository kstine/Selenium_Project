'''
Created on Jan 11, 2017

@author: kstine
'''

import requests
import zipfile

urls = ['https://www.irs.gov/pub/irs-soi/eo1.csv', 'https://www.irs.gov/pub/irs-soi/eo2.csv', 'https://www.irs.gov/pub/irs-soi/eo3.csv']
files = ['eo1.csv', 'eo2.csv', 'eo3.csv']
i=0
for url in urls:
    print ("downloading: " + url)
    r = requests.get(url)
    with open(files[i] , "wb") as code:
        code.write(r.content)
    i=i+1

z = zipfile.ZipFile("irs.zip", "w")

for f in files:
    z.write(f)
    
z.close()

# craurl = 'http://www.cra-arc.gc.ca/ebci/haip/srch/downloadbasic-eng.action?k=&amp;s=registered&amp;p=1&amp;b=true'
# 
# print ("downloading: " + craurl)
# cr = requests.get(craurl)
# cr.content