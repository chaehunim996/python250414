#demoFile.py

f = open("c:\\work\\test.txt","wt",encoding="uft-8")
f.write("first\nsecond\nthird\n")
f.close()

#읽기
f = open(r"c:\\work\\test.txt","rt",encoding="uft-8")
resurt = f.read()
print(resurt)
f.close()
