'''
Created on Apr 09, 2017

@author: kstine
'''

import requests

urls = ['http://www.visitcookcounty.com/web-cam/gmcam.jpg']

for url in urls:
    print ("downloading: " + url)
    r = requests.get(url)
    with open("gmpicture.jpg" , "wb") as code:
        code.write(r.content)
