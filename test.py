import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/new-releases/2200'
res = requests.get(url, 'lxml')
soup = BeautifulSoup(res.text)

new_arrivals = soup.select('.title_text')
for no, book in enumerate(new_arrivals, 1):
  print(no, book.text.strip()) # strip은 앞,뒤 공백을 없애고 글자만 가지고 오는 것.
