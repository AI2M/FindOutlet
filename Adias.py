from bs4 import BeautifulSoup
import urllib2
import math


offset = 0
num = 0
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
# print pagecount 

Items = page.findAll('div',{'class':'innercard'})
for item in Items :
    sale = item.find('div',{'class':'badge sale'}).span.text.strip().replace('-','').replace('%','')
    name = item.find('div',{'class':'product-info-inner-content clearfix with-badges'}).a.span.text
    img_url = item.find('div',{'class':'image plp-image-bg'}).a.find('img',{'class':'lazyload'})['data-original']
    price = item.find('div',{'class':'clearfix product-info-price-rating price-without-rating'}).div
    sale_price = price.find('span',{'class':'salesprice discount-price'}).text.strip().replace(',','')
    base_price = price.find('span',{'class':'strike'}).find('span',{'class':'baseprice'}).text.strip().replace(',','')
    
    if(int(sale)>=50):
        print "sale > 50"
        
        

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
        if(int(sale)>=50):
            print "sale > 50"


