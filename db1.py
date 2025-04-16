# db1.py
import sqlite3

# 연결객체 리턴(메모리에서 작업)
con = sqlite3.connect(":memory:")
#커서객체 리턴
cur = con.cursor()

#테이블 구조 생성
cur.execute("create table PhoneBook(name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values('derick','010-2222-3333');")
#입력 파라메터 처리
name = "홍길동"
phonenumber = "010-1111-2222"
cur.execute("insert into PhoneBook values(?,?);",(name,phonenumber))

#다중의 레코드 입력(행데이터입력)
datalist = (("전우치","010-2222-5555"),("이순신","010-3333-0000"))
cur.executemany("insert into PhoneBook values(?,?);",datalist)
#검색
cur.execute("select * from PhoneBook;" )
for row in cur:
    print(row)


