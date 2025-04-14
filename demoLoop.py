value = 5
while value > 0:
    print(value)
    value -=1

#대부분은 for ~ in ~루프를 사용
list = [100, "애플" , 3.14]
for item in list:
    print(item, type(item))

d = {"apple":100, "kiwi":200}
for item in d.items():
    print(item)