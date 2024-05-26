import json
import pandas as pd

def normalizeJson(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    df = pd.DataFrame(data)
    df.index.name = 'index'
    return df

filePath = 'test.json'
df = normalizeJson(filePath)
df.to_csv('normalized_data.csv', index=False)
