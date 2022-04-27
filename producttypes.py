import json
import redis
def load_jsonl(input_path) -> list:
    """
    Read list of objects from a JSON lines file.
    """
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}'.format(len(data), input_path))
    return data

client = redis.Redis(host = '43.251.253.107', port=1500,db=1)
webpage_data = load_jsonl('/home/et/Documents/Ahsan/Data/allurebymht.com.jsonl')
# for d in webpage_data:
for item in webpage_data:

  try:
    client.sadd('allProductTypes',item['product']['product_type'])
  except Exception as e:
    print(e)     