# demo list
# 함수 정의
def times(a,b):
    return a+b, a*b

#함수 호출
result = times(3,4)
print(result)

print("id:%s, name:%s" %("kim", "김유신"))

#세트형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.difference(b))
print(a.intersection(b))

# 형식변환
a = set((1,2,3))
print(type(a))
b = list(a)
b.append(4)
print(b)
c =tuple(b)
print(c)