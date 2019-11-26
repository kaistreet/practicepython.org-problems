#Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
from urllib.request import urlopen
from bs4 import BeautifulSoup
site = urlopen('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
soup = BeautifulSoup(site,'html.parser')
article = soup.find("article",class_="article main-content").text
print(article)
