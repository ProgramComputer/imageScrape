
#credit to https://code.tutsplus.com/tutorials/compressing-and-extracting-files-in-python--cms-26816 and https://rubikscode.net/2019/12/02/scraping-images-with-python/
import cloudscraper
from bs4 import BeautifulSoup
import zlib
import requests
import urllib.request
import shutil
import errno
import os
import zipfile
import argparse
import os

parser = argparse.ArgumentParser(description='Scrape images')
parser.add_argument('url', nargs='+', 
                    help='The url to scrape',required=True)
 parser.add_argument('tag', nargs='+', 
                    help="name of the tag that is the parent of the <img> tag default is 'div'",default = 'div')
parser.add_argument('classs' , nargs='+', 
                    help='the class of the tag that is the parent of the <img> tag default is none',default = '')
parser.add_argument('path', nargs=1,
                 default='C:\Downloads',
                    help='the path to where the files will download default is C:\Downloads')
parser.add_argument('-i', dest='type', nargs = ?, default= '.jpg',help = 'image type the default is .jpg')
parser.add_argument('attribute',nargs = '?', default = 'data-src', help='the attribute to be scraped default is data-src')
parser.add_argument('-x', nargs=2, dest='ends', default='1',dest=, type=int, help= "must contain two arguments to download multiple images. Find the numerical variable and insert '{x}' in url to allow this")
parser.add_argument('-s', nargs=?, dest='step',default='1',type=int, help= "increment of the sequence")

args = parser.parse_args()
url = args.url
type_ = args.type
attribute = args.attribute
if "{x}" in url:
    args.ends[0]=1
    args.ends[1]=1

for x in range(args.ends[0], args.ends[1],args.step):
    #define the name of the directory to be created
    path = f"{args.path}//extract/{x}"
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #try:
    #os.mkdir(path)
    #except OSError:
    #   print ("Creation of the directory %s failed" % path)
    #else:
    #   print ("Successfully created the directory %s " % path)
    def download_image(image,position = 0):
        
        response = requests.get(image, stream=True) #[0]
        #realname = ''.join(e for e in image[1] if e.isalnum())
        

        file = open(f"{path}/{position}{type_}" , 'wb') #C://images//bs//{}.jpg 
        
    
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, file)
        del response

    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    
    response = scraper.get(url).text

    soup = BeautifulSoup(response, "html.parser")

    aas = soup.find_all(args.tag, class_= args.classs) #find_all()

    image_info = []

    for a in aas:
        image_tag = a.findChildren("img")
        image_info.append(image_tag[0][f"{attribute}"])#, image_tag[0]["alt"])
    for i in range(0, len(image_info)):
        download_image(image_info[i],i) 
    
    fantasy_zip = zipfile.ZipFile(f'{path}.zip', 'w') #C:\\Stories\\Fantasy\\archive.zip ||||| Third parameter ', compression = zipfile.ZIP_DEFLATED'
 
    for folder, subfolders, files in os.walk(f'{path}'): #C:\\Stories\\Fantasy\\archive.zip
 
        for file in files:
            if file.endswith(f'{type_}'):
                fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), f'{path}'), compress_type = zipfile.ZIP_DEFLATED)    #fantasy_zip.write(os.path.join(folder, file), file, compress_type = zipfile.ZIP_DEFLATED)
 
    fantasy_zip.close()
print("FINISH")
