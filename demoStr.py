#정규표현식
import re

result = re.search("[0-9]*th","  35th")
print(result)
print(result.group())

# result = re.match("[0-9*th]"," 35th")
# print(result)
# print(result.group())

result = re.search("apple","this is apple")
print(result.group())

result = re.search("\d{4}","올해는 2025년입니다")
print(result.group())

result = re.search("\d{5}","우리동네는 51000")
print(result.group())
