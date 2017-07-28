import io, sys
import requests
from bs4 import BeautifulSoup

URL = 'http://lantis-net.com/aikatsustars/'

#as Android Chrome
resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; KYV42 Build/1.000AL.27.a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"})
soup = BeautifulSoup(resp.text, 'html.parser')

dl_link = soup.find(class_='radi').find('a')['href']
print(dl_link)
filename = dl_link.split('/')[-1]
print(filename)

r = requests.get(dl_link, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; KYV42 Build/1.000AL.27.a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"})
print('dl done.')

if r.status_code != 200:
    print('not odayaka.')
    e = Exception("HTTP status: " + response.status_code)
    raise e

f = open(filename, 'wb')
f.write(r.content)
f.close()


#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#print(soup.prettify())
