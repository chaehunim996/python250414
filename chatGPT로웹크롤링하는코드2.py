import requests
from bs4 import BeautifulSoup

# 검색어 (예: "반도체")
query = "반도체"
url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}"

# User-Agent 설정 (없으면 차단될 수 있음)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# 페이지 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 신문기사 제목 추출 (네이버 뉴스 영역의 구조 활용)
titles = soup.select(".news_tit")  # 기사 제목 링크 클래스

print("📰 기사 제목 리스트:")
for idx, title in enumerate(titles, 1):
    print(f"{idx}. {title.get_text()} - {title['href']}")
