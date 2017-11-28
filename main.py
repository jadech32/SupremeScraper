from classes.logger import Logger
from classes.scraper import Supreme
from classes.tools import Tools
import threading
from classes.proxies import Proxy


log = Logger().log

if __name__ == '__main__':

    supreme = Supreme()
    # Make sure to IP Authenticate your proxies!
    log('Initializing Script..', 'info')
    # jackets, shirts, sweaters, tshirts, sweatshirts, hats, pants, bags, accessories, shoes, skate
    # Tees only default to smallest size available..

    t1 = threading.Thread(target=supreme.findItem, args=(['pin'], [''], 'accessories'))
    t2 = threading.Thread(target=supreme.findItem, args=(['pin'], [''], 'accessories'))
    t3 = threading.Thread(target=supreme.findItem, args=(['pin'], [''], 'accessories'))
    t3.start()
    t2.start()
    t1.start()
    t2.join()
    t1.join()
    t3.join()


