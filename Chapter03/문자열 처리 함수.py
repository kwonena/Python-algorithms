python = "Python is Amazing"
print(python.lower()) # 문자열을 소문자로 변환하는 함수
print(python.upper()) # 문자열을 대문자로 변환하는 함수
print(python[0].isupper()) # 해당 인덱스의 문자가 대문자면 True, 소문자면 False 반환하는 함수
print(len(python)) # 문자열 길이 함수
print(python.replace("Python", "Java")) # 문자열을 다른 문자열로 변경하는 함수

index = python.index("n") # 해당 문자의 위치를 찾아주는 함수
print(index)

# 두번쨰 n의 위치 찾기
index = python.index("n", index + 1) # 찾은 위치 이후에 해당 문자의 위치를 찾아줌
print(index)

print(python.find("Java")) # 해당 문자열이 없으면 -1 반환
print(python.index("Java")) # 해당 문자열이 없으면 에러 반환

print(python.count("n")) # 해당 문자의 개수를 반환하는 함수