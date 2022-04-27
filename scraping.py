import os
import multiprocessing 
import sys
import datetime
from multiprocessing import Pool
import requests
import json
import redis
from usp.tree import sitemap_tree_for_homepage
import tldextract
with open('all787urls.txt', 'r') as f:
    siteNames = [line.strip() for line in f]

print(siteNames)

client0 = redis.Redis(host = '43.251.253.107', port=1500,db=0)
def basic_func(domain):
    try:
        tree = sitemap_tree_for_homepage(domain)
        urls = [page.url for page in tree.all_pages()] 
        for item in urls:
            try:
                ext = tldextract.extract(domain)
                url = ext.domain+'.'+ext.suffix
                client0.sadd(url,item)
            except Exception as e:
                print(e)    
    except Exception as e:
        print(e) 

pool = Pool(processes=30) 
pool.map(basic_func, siteNames)
pool.close()       