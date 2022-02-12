import requests

url = '<your_app_url>/predict_api' #Get the <your_app_url> from https://console.cloud.google.com/run/detail/us-central1/<your_app_name>/general
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})
print(r) ### if you get 403 it is permission issue, successful request will return 200
print(r.json())
