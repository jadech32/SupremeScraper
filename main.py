from classes.logger import Logger
from classes.scraper import Supreme
from classes.tools import Tools
import threading
from classes.proxies import Proxy
import webbrowser
import time

log = Logger().log

def mobileStockRunner():
    ask = False
    supreme = Supreme()

    # supreme.setOverride(True)

    while ask == False:
        # Put in last week's (not the upcoming drops)
        ask = supreme.mobileStock('06/28') # Needs to be last thursday's date (most recent drop) - The existing date (BEFORE DROP)
        time.sleep(0.3)

    # product placements here
    t4 = threading.Thread(target=supreme.findItemUsingPosition, args=(1, 'accessories'))
    # t5 = threading.Thread(target=supreme.findItemUsingPosition, args=(27, 'tshirts'))
    # t6 = threading.Thread(target=supreme.findItemUsingPosition, args=(33, 'tshirts'))
    t4.start()
    # t5.start()
    # t6.start()

if __name__ == '__main__':

    supreme = Supreme()
    mobileStockRunner()
    # supreme.setOverride(True)
    # Make sure to IP Authenticate your proxies!
    log('Initializing Script..', 'info')
    # jackets, shirts, sweaters, tshirts, sweatshirts, hats, pants, shorts, bags, accessories, shoes, skate
    # Tees only default to smallest size available..
    #
    t1 = threading.Thread(target=supreme.findItem, args=(['vest'], [''], 'accessories'))
    # t2 = threading.Thread(target=supreme.findItem, args=(['mona'], ['black'], 'tshirts'))
    # t3 = threading.Thread(target=supreme.findItem, args=(['swim'], ['white'], 'tshirts'))

    t1.start()
    # t2.start()
    # t3.start()
    # t2.start()
