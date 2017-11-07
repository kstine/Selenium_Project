'''
Created on Apr 09, 2017

@author: kstine
'''

import requests
from datetime import datetime
import os

urls = ['https://www.visitcookcounty.com/wp-content/uploads/webcams/gmcam.jpg']
header = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
fileLocation = "Desktop/GMWEBCAMPICS"
nowTime = datetime.now()

for url in urls:
    print ("downloading: " + url)
    fileName = "gmcam_" + nowTime.strftime('%Y%m%d_%H%M%S') + ".jpg"
    response = requests.get(url, stream=True, headers=header)
    handle = open(os.path.join(os.path.expanduser('~'), fileLocation, fileName) , "wb")
    print ("Status code: " + response.status_code.__str__())
    for chunk in response.iter_content(chunk_size=128):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    
response.close()
