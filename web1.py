from bs4 import BeautifulSoup

page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

soup = BeautifulSoup(page, "html.parser")

# print(soup.prettify())

#검색
# print(soup.find_all("p"))

# print(soup.find_all("b"))
 
# print(soup.find("p"))

# print(soup.find_all("p", class_="outer-text"))

for tag in soup.find_all("p"):
    title = tag.text
    title2 = title.replace("\n","")
    title3 = title2.replace("\t","")
    print(title3.strip())

