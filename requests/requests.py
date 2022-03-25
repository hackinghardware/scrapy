import requests

r = requests.get('https://quotes.toscrape.com/')

# do a request
print(r)
# status code
#print(r.status_code)
# Headers
#print(r.headers['content-type'])
# Encoding
#print(r.encoding)
# body text
#print(r.text)
# body json
#print(r.json())

#print('---------------------------------------------------------------------')
#payload = {'term': 'rusia'}
#r = requests.get('https://www.larepublica.co/buscar?', params=payload)
#r = requests.get(r.url)
#print(r.json())

