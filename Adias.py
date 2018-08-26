from bs4 import BeautifulSoup
import urllib2
import math
import time
from copy import copy, deepcopy
import json

#decalre variable
offset = 0
numMen = 0
numMen_new = 0
SearchCount = 0

w, h = 5,2000
DataMen = [['null' for x in range(w)] for y in range(h)]
DataMen_new = [['null' for x in range(w)] for y in range(h)]
DataMen_new_new = [['null' for x in range(w)] for y in range(h/4)]
#end decalre variable

# while True:

#setup request

site = "https://www.adidas.co.th/en/men-outlet?start="+str(offset)
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(site, headers=hdr)
get = urllib2.urlopen(req)
page = BeautifulSoup(get,'html.parser')
count = float(page.find('p',{'class':'count'}).text.strip().replace('(','').replace(')','').replace('Products',''))
pagecount = int(math.ceil(count/48))

#end setup request


#getData

Items = page.findAll('div',{'class':'innercard'})
for item in Items :
    sale = item.find('div',{'class':'badge sale'}).span.text.strip().replace('-','').replace('%','')
    name = item.find('div',{'class':'product-info-inner-content clearfix with-badges'}).a.span.text
    img_url = item.find('div',{'class':'image plp-image-bg'}).a.find('img',{'class':'lazyload'})['data-original']
    price = item.find('div',{'class':'clearfix product-info-price-rating price-without-rating'}).div
    sale_price = price.find('span',{'class':'salesprice discount-price'}).text.strip().replace(',','')
    base_price = price.find('span',{'class':'strike'}).find('span',{'class':'baseprice'}).text.strip().replace(',','')
    
    if(SearchCount==0):
        if(int(sale)>=50):
            DataMen[numMen][0] = name
            DataMen[numMen][1] = sale
            DataMen[numMen][2] = sale_price
            DataMen[numMen][3] = base_price
            DataMen[numMen][4] = img_url
            numMen=numMen+1
    else:
        if(int(sale)>=50):
            DataMen_new[numMen][0] = name
            DataMen_new[numMen][1] = sale
            DataMen_new[numMen][2] = sale_price
            DataMen_new[numMen][3] = base_price
            DataMen_new[numMen][4] = img_url
            numMen_new=numMen_new+1
        
        

for cur in range(1,pagecount):
    offset = cur*48
    site = "https://www.adidas.co.th/en/men-outlet?start="+str(offset)

    req = urllib2.Request(site, headers=hdr)
    get = urllib2.urlopen(req)
    page = BeautifulSoup(get,'html.parser')

    Items = page.findAll('div',{'class':'innercard'})
    for item in Items :
        sale = item.find('div',{'class':'badge sale'}).span.text.strip().replace('-','').replace('%','')
        name = item.find('div',{'class':'product-info-inner-content clearfix with-badges'}).a.span.text
        img_url = item.find('div',{'class':'image plp-image-bg'}).a.find('img',{'class':'lazyload'})['data-original']
        price = item.find('div',{'class':'clearfix product-info-price-rating price-without-rating'}).div
        sale_price = price.find('span',{'class':'salesprice discount-price'}).text.strip().replace(',','')
        base_price = price.find('span',{'class':'strike'}).find('span',{'class':'baseprice'}).text.strip().replace(',','')
        
        if(SearchCount==0):
            if(int(sale)>=50):
                DataMen[numMen][0] = name
                DataMen[numMen][1] = sale
                DataMen[numMen][2] = sale_price
                DataMen[numMen][3] = base_price
                DataMen[numMen][4] = img_url
                numMen=numMen+1
        else:
            if(int(sale)>=50):
                DataMen_new[numMen][0] = name
                DataMen_new[numMen][1] = sale
                DataMen_new[numMen][2] = sale_price
                DataMen_new[numMen][3] = base_price
                DataMen_new[numMen][4] = img_url
                numMen_new=numMen_new+1

#end getData

#detect duplicate
newitem = 0
if(SearchCount>0):
    for i in range(0,numMen):
        for j in range(0,numMen_new):
            if(DataMen_new[j][0]==DataMen[i][0]):
                print ("null")
            else:
                DataMen_new_new[newitem][0] = DataMen_new[j][0]
                DataMen_new_new[newitem][1] = DataMen_new[j][1]
                DataMen_new_new[newitem][2] = DataMen_new[j][2]
                DataMen_new_new[newitem][3] = DataMen_new[j][3]
                DataMen_new_new[newitem][4] = DataMen_new[j][4]
                newitem = newitem+1

#end detect duplicate

#send DataMen_new_new by api
print json.dumps(DataMen_new_new)
#end send DataMen_new_new by api


#reset variable
SearchCount = SearchCount+1
DataMen = DataMen_new
numMen = numMen_new
numMen_new = 0
offset = 0

#end reset variable

# print (DataMen[0][0])
