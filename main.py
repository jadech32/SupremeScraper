from classes.logger import Logger
from classes.scraper import Supreme
from classes.tools import Tools
import threading


log = Logger().log

if __name__ == '__main__':
    supreme = Supreme()
    log('Initializing Script..', 'info')
    # Blimp, Hat
    t1 = threading.Thread(target=supreme.findItem, args=(['blimp'], ['white'], 'accessories'))
    t2 = threading.Thread(target=supreme.findItem, args=(['gonz'], ['green'], 'skate'))
    t1.start()
    t2.start()
    t1.join()
    t2.join()