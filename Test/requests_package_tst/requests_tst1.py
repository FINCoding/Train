import requests
# user
r = requests.get('https://api.github.com/events')

# print(r.status_code)
# r.encoding
# print(r.text)
print(r.json())