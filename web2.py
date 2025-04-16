
#웹크롤링을 위한 선언
from bs4 import BeautifulSoup
#웹서버에 요청 선언
import urllib.request

import re

#파일로 저장
f = open("clien.txt", "wt", encoding="utf-8")

#페이지 처리
for i in range(0, 10):
    url = "https://www.clien.net/service/board/sold?od=T31&catagory=0&po=" + str(i)
    print(url)
    response = urllib.request.urlopen(url)
    page = response.read().decode("utf-8", "ignore")
    soup = BeautifulSoup(page, "html.parser")
    list = soup.find_all("span", attrs={"data-role": "list-title-text"})

    for tag in list:
        title = tag.text.strip()  # 제목 가져오기
        title = title.replace("\n", "")  # 줄바꿈 제거
        if re.search("맥북", title):  # 제목에 "맥북"이 포함된 경우
            print(title)
            f.write(title + "\n")

"""
<span class="subject_fixed" data-role ="list-title-text" title ="새제품 MacBook Pro 14인치 블랙">
</span>
"""
f.close()  # 파일 닫기