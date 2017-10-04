from classes.logger import Logger
from classes.scraper import Supreme
from classes.tools import Tools
import threading


log = Logger().log

if __name__ == '__main__':
    supreme = Supreme()
    # Make sure to IP Authenticate your proxies!
    log('Initializing Script..', 'info')
    # jackets, shirts, sweaters, tshirts, sweatshirts, hats, pants, bags, accessories, shoes, skate
    #t1 = threading.Thread(target=supreme.findItem, args=(['clipper'], ['red'], 'accessories'))
    t2 = threading.Thread(target=supreme.findItem, args=(['velour'], ['black'], 'sweaters')) #???
   # t3 = threading.Thread(target=supreme.findItem, args=(['plant', 'tee'], ['pale'], 'tshirts'))
    #t2 = threading.Thread(target=supreme.findItem, args=(['knife'], [''], 'accessories'))
    #t1.start()
    t2.start()
   # t3.start()
   # t1.join()
    t2.join()
   # t3.join()