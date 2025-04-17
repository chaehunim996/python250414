# demoForm2.py 
# demoForm2.ui(화면단) + demoForm2.py(로직단) 

#QyQt5 선언 
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹크롤링을 위한 선언
from bs4 import BeautifulSoup
#웹서버에 요청 선언
import urllib.request

import re


#디자인한 파일을 로딩(demoForm2.ui) 
form_class = uic.loadUiType("demoForm2.ui")[0]

#폼클래스를 정의(QMainWindow클래스를 상속)
class DemoForm(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) #UI설정 
    #슬롯메서드를 정의
    def firstClick(self): 
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
        self.label.setText("클리앙 중고장터 크롤링 완료")
    def secondClick(self): 
        self.label.setText("두번째 버튼 클릭했습니다.")
    def thirdClick(self): 
        self.label.setText("세번째 버튼 클릭~~")

#직접 모듈을 실행했는지 진입점 체크 
if __name__ == "__main__": 
    app = QApplication(sys.argv) #QApplication 객체 생성 
    demoForm = DemoForm() #DemoForm 객체 생성 
    demoForm.show() #화면 출력 
    app.exec_() #이벤트 루프 시작