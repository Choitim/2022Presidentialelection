import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EC%A0%9C20%EB%8C%80+%EB%8C%80%ED%86%B5%EB%A0%B9%EC%84%A0%EA%B1%B0+%EA%B3%B5%EC%95%BD")
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")


for link in links:
    title = link.text
    url = link.attrs['href']

print(title, url)
