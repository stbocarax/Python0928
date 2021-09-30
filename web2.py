# web2.py
#웹서버와 통신
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#파일에 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")

for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i+1)
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
               
    for item in cartoons:
        title = item.find("a").text
        print(title.strip() )
        f.write(title.strip() + "\n")

f.close()