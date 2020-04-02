import requests
import json
import pandas as pd

# POST to API
payload = {'code': 'DE'}
URL = 'http://127.0.0.1/covid'
print('payload:', json.dumps(payload))
response = requests.post(url=URL, data=json.dumps(payload))
print('response:', response.text)

# Convert to data frame
df = pd.DataFrame.from_dict(json.loads(response.text))
print(df)