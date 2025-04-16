import requests
from bs4 import BeautifulSoup

# 검색어 URL (반도체)
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# User-Agent 설정 (크롤링 방지 우회용)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# 요청 보내기
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 기사 제목 추출
titles = soup.select('a.news_tit')  # 뉴스 제목이 있는 a 태그 (news_tit 클래스)

print("📄 신문 기사 제목 목록:")
for idx, title in enumerate(titles, 1):
    print(f"{idx}. {title['title']}")
