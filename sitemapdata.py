import multiprocessing 
from multiprocessing import Pool
import requests
import json
import redis
import tldextract

client2 = redis.Redis(host = '43.251.253.107', port=1500,db=0)



with open('all787urls.txt', 'r') as f:
    domainNames = [line.strip() for line in f]
print(domainNames)

def basic_func(domain):
    try:  
        ext = tldextract.extract(domain)
        url = ext.domain+'.'+ext.suffix
     
        allinks=client2.smembers(url)
        for link in list(allinks):
            link = link.decode("utf-8")
            if (link.find('/products/') != -1) or (link.find('/collections/') != -1):
                try:  
                    link = link+'.json'
                    response = requests.get(link)
                    json_data = json.loads(response.text)
                    dump_jsonl([json_data], url+'.jsonl',append=True)
                except Exception as e:
                    print(e)    

    except Exception as e:
        print(e)

def dump_jsonl(data, output_path, append=False):
    """
    Write list of objects to a JSON lines file.
    """
    mode = 'a+' if append else 'w'
    with open(output_path, mode, encoding='utf-8') as f:
        for line in data:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
    print('Wrote {} records to {}'.format(len(data), output_path)) 

pool = Pool(processes=50) 
pool.map(basic_func, domainNames)
pool.close()  
