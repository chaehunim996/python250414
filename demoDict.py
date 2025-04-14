#demoDict.py
color = {"appple":"red", "banana":"yellow"}
print(color)
print(len(color))
print(color["appple"])
#입력
color["cherry"] = "red"
print(color)
#삭제
del color["appple"]
print(color)

for item in color.items():
    print(item)


#boolean 형식
print(1<2)
print(1!=2)
print(1==2)
print(True and True and True)
print(True and True and False)
print(True and False and False)