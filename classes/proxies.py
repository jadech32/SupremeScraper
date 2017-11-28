#!/usr/bin/env python3
import threading
import requests
from xmltodict import parse
import json
import re
import webbrowser
from classes.logger import Logger
from classes.tools import Tools
import time
import csv
from random import randint
import itertools
log = Logger().log

class Proxy:

    def __init__(self):
        self.proxies = self.importProxy()
        self.countOG = len(self.proxies) - 1
        self.count = randint(0, len(self.proxies) - 1)

    def importProxy(self):

        moreResults = list()
        with open('config/proxies.txt', newline='') as inputfile:
            for row in csv.reader(inputfile):
                splitted = row[0].split(":")

                if len(splitted) == 2:
                    proxObj = {
                        'http': 'http://' + row[0],
                        'https': 'https://' + row[0]
                    }
                    moreResults.append(proxObj)

                if len(splitted) == 4:
                    proxObj = {
                        'http': 'http://' + splitted[2] + ':' + splitted[3] + '@' + splitted[0] + ':' + splitted[1],
                        'https': 'https://' + splitted[2] + ':' + splitted[3] + '@' + splitted[0] + ':' + splitted[1]
                    }
                    moreResults.append(proxObj)

        return moreResults

    def getProxy(self):
        return self.proxies

    def countProxy(self):
        if self.count == 0:
            self.count = self.countOG
        else:
            self.count = self.count - 1
        return self.count

