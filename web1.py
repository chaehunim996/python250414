# web1.py
#웹 클롤링을 위한 선언
from bs4 import BeautifulSoup

# 웹페이지를 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

# BeautifulSoup 객체 생성
soup = BeautifulSoup(page, "html.parser")
#전체페이지 출력
#print(soup.prettify())
#<p> 태그를 찾음
print(soup.find_all("p")) # 모든 p 태그를 찾음
#<p> 태그를 찾음
print(soup.find("p")) # 첫 번째 p 태그를 찾음

#<p> 태그의 개수 출력
print(len(soup.find_all("p"))) # p 태그의 개수 출력

#<p> 태그의 내용 출력
for p in soup.find_all("p"):
    print(p.string) # p 태그의 내용 출력

#조건검색: <p class="outer-text"> 태그를 찾음
print(soup.find_all("p", class_="outer-text")) # 모든 p 태그를 찾음

#최근에는 attr속성 검색
print(soup.find_all("p",attrs={"class": "outer-text"}))

#id속성 검색
print(soup.find_all("p",id="first"))

#<p>의 text 속성 검색:태그 내부의 컨텐츠만 가져오기
for tag in soup.find_all("p"):
    title = tag.text 
    title = title.replace("\n", "") # 줄바꿈 제거
    print(title) 

    