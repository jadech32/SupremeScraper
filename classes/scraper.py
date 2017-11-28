#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from classes.logger import Logger
from classes.tools import Tools
from classes.proxies import Proxy
import webbrowser
import time
from requests.adapters import HTTPAdapter
log = Logger().log
tools = Tools()
empty_warn = 0

class Supreme:
    proxy = Proxy()
    def __init__(self):
        self.jackets = 'http://www.supremenewyork.com/shop/all/jackets'
        self.shirts = 'http://www.supremenewyork.com/shop/all/shirts'
        self.sweaters = 'http://www.supremenewyork.com/shop/all/tops_sweaters'
        self.tshirts = 'http://www.supremenewyork.com/shop/all/t-shirts'
        self.sweatshirts = 'http://www.supremenewyork.com/shop/all/sweatshirts'
        self.hats = 'http://www.supremenewyork.com/shop/all/hats'
        self.pants = 'http://www.supremenewyork.com/shop/all/pants'
        self.bags = 'http://www.supremenewyork.com/shop/all/bags'
        self.accessories = 'http://www.supremenewyork.com/shop/all/accessories'
        self.shoes = 'http://www.supremenewyork.com/shop/all/shoes'
        self.skate = 'http://www.supremenewyork.com/shop/all/skate'

    def returnType(self, type):
        return {
            'jackets': self.jackets,
            'shirts': self.shirts,
            'sweaters': self.sweaters,
            'tshirts': self.tshirts,
            'sweatshirts': self.sweatshirts,
            'hats': self.hats,
            'pants': self.pants,
            'bags': self.bags,
            'accessories': self.accessories,
            'shoes': self.shoes,
            'skate': self.skate
        }[type]

    def findItem(self, keywords, color, type):

        session = requests.Session()
        url = self.returnType(type)


        if not self.proxy.getProxy():
            global empty_warn
            if empty_warn == 0:
                log('Not using any proxies','yellow')
                empty_warn = 1
        else:
            current_proxy = self.proxy.getProxy()[self.proxy.countProxy()]
            '''
            session2 = requests.session()
            rersp2 = session2.get("http://ip-api.com/json",proxies=current_proxy)
            print(rersp2.json())
            '''
            log('Using proxy ' + str(current_proxy),'yellow')

            session.mount('https://', HTTPAdapter(max_retries=1))
            response = session.get(url, proxies=current_proxy, timeout=1.1)
            if(response.status_code != 200):
                log('Proxy banned' + str(response.status_code),'info')
                time.sleep(0.6)
                self.findItem(keywords, color, type)

        soup = BeautifulSoup(response.content, 'html.parser')

        found = None
        turbo = soup.find(attrs={'class': 'turbolink_scroller'})

        items = turbo.contents # List of items, class=item

        for piece in items:
            #print(piece)
            product_name = piece.contents[0].contents[1].text
            product_color = piece.contents[0].contents[2].text
            product_url = 'https://www.supremenewyork.com' + piece.contents[0].contents[2].contents[0]['href']
            #print(product_name)
            if all(i in product_name.lower() for i in keywords) and all(i in product_color.lower() for i in color):
                found = True
                log('Found Product: ' + product_name + ' - ' + product_color + ' | ' + product_url, 'success')
                webbrowser.open_new_tab(product_url)

        if found == None:
            log('Item not found/live... retrying', 'error')
            time.sleep(0.6)
            self.findItem(keywords, color, type)




