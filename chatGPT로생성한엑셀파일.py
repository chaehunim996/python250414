import openpyxl
import random

# 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Products"

# 헤더 추가
headers = ["제품ID", "제품명", "수량", "가격"]
ws.append(headers)

# 샘플 데이터 생성
product_names = ["TV", "냉장고", "세탁기", "에어컨", "전자레인지", "청소기", "컴퓨터", "스피커", "프린터", "모니터"]

for i in range(1, 101):  # 100개의 데이터 생성
    product_id = f"P{i:03d}"  # 제품ID (P001, P002, ...)
    product_name = random.choice(product_names)  # 랜덤 제품명 선택
    quantity = random.randint(1, 50)  # 수량 (1~50 랜덤)
    price = random.randint(10000, 1000000)  # 가격 (1만~100만 랜덤)
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save("products.xlsx")
print("products.xlsx 파일이 생성되었습니다.")