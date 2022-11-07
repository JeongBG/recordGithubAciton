import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/new-releases/2200'
res = requests.get(url, 'lxml')
soup = BeautifulSoup(res.text)

new_arrivals = soup.select('.title_text')
for no, book in enumerate(new_arrivals, 1):
  print(no, book.text.strip())
