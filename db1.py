# db1.py 
import sqlite3
#먼저 메모리에만 저장(임시)
# con = sqlite3.connect(":memory:")
#커서 객체를 생성
con = sqlite3.connect("test.db")

cur = con.cursor()
#테이블 구조를 만들기(테이블 스키마 생성)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 데이터 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 데이터를 파라메터 처리
name = "gildong"
phoneNum = "010-123"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNum))

datalist = (("tom", "010-333"),("dsp","010-567"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

# #검색을 해서 결과 보기 
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

print("-----1건----")
print(cur.fetchone())
print("-----2건----")
cur.execute("select * from PhoneBook;")
print(cur.fetchmany(2))
print("-----모두----")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
