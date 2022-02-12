import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'R&DSpend':2, 'Administration':9, 'Marketing':6})

print(r.json())
