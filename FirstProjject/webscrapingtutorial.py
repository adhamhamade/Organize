import requests
res = requests.get('https://subscene.com/subtitle/download?mac=YjwNXAT16vE7xw35oLJ0GU6WD8cRh2XM4iCyvwIkHXz8vwXC6zvqqeUUQbv87kYdi7z0clx3CUPD30-4mZZKXZg4-6TDWeOPT8NNXQeOFP_i9mqhoagBdpHfvNU2XNF10')

res.status_code == requests.codes.ok

playFile = open('izombie.zip', 'wb')

for chunk in res.iter_content(100000):
        playFile.write(chunk)

#print(res.text[:250])


playFile.close()



'''import requests, bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select('#author')

print(elems[0].getText())
'''
