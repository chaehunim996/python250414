import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 검색어 설정
query = "반도체"
url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}"

# 요청 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# HTML 요청 및 파싱
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.select(".news_tit")  # 기사 제목의 클래스

# 엑셀 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "News Results"

# 헤더 작성
ws.append(["번호", "기사 제목", "링크"])

# 데이터 작성
for idx, title in enumerate(titles, 1):
    ws.append([idx, title.get_text(), title['href']])

# 엑셀 파일 저장
wb.save("results.xlsx")
print("✅ results.xlsx 파일 저장 완료!")
