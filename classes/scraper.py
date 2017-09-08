#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from classes.logger import Logger
from classes.tools import Tools
import webbrowser
import time
log = Logger().log
tools = Tools()

class Supreme:

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
        response = session.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        found = None
        turbo = soup.find(attrs={'class': 'turbolink_scroller'})
        items = turbo.contents # List of items, class=item
        for piece in items:
            product_name = piece.contents[0].contents[1].text
            product_color = piece.contents[0].contents[2].text
            product_url = 'https://www.supremenewyork.com' + piece.contents[0].contents[2].contents[0]['href']

            #print(product_url)
            if all(i in product_name.lower() for i in keywords) and all(i in product_color.lower() for i in color):
                found = True
                log('Found Product: ' + product_name + ' - ' + product_color + ' | ' + product_url, 'success')
                webbrowser.open_new_tab(product_url)

        if found == None:
            log('Item not found/live... retrying', 'error')
            time.sleep(0.5)
            self.findItem(keywords, color, type)




