# key에 대한 중복 허용X
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# 존재하지 않는 vlaue를 출력할 때
# print(cabinet[5]) # 에러메세지 출력
# print(cabinet.get(5)) # None 출력
print(cabinet.get(5, "사용가능")) # 5에 대한 vlaue가 존재하지 않을 때 사용가능 메세지 출력

print(3 in cabinet) # True
print(5 in cabinet) # False

# string 형태의 key도 가능
cabinet = {"A-3": "유재석", "B-100": "김태호"}

# 새로운 vlaue
cabinet["A-3"] = "김종국" # 유재석 -> 김종국으로 vlaue 업데이트
cabinet["C-20"] = "조세호"
print(cabinet)

# vlaue 삭제
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# vlaue만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모든 값 삭제
cabinet.clear()
print(cabinet) # {}