import requests

r = requests.get('https://api.github.com/events')
r.text

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.url)
