import json

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


webpage_data = load_jsonl('/home/et/Documents/Ahsan/Data/chaseupfashion.com.jsonl')
for item in webpage_data:
  with open('chaseupfashion.txt', 'a') as f:
    try:
      f.write(str(item['product']['product_type']))
      f.write("\n")
      f.close()
    except:
      pass  