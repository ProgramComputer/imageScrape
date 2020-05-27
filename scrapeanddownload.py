
#credit to https://code.tutsplus.com/tutorials/compressing-and-extracting-files-in-python--cms-26816 and https://rubikscode.net/2019/12/02/scraping-images-with-python/
from bs4 import BeautifulSoup
import zlib
import requests
import urllib.request
import shutil

import os
import zipfile
 
url = "https://rubikscode.net/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("a", class_='entry-featured-image-url')
 
 
 
 
 
 
 
 
 fantasy_zip = zipfile.ZipFile('C:\\Stories\\Fantasy\\archive.zip', 'w')
 
for folder, subfolders, files in os.walk('C:\\Stories\\Fantasy'):
 
    for file in files:
        if file.endswith('.pdf'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Stories\\Fantasy'), compress_type = zipfile.ZIP_DEFLATED)
 
fantasy_zip.close()
