# 출석번호가 1, 2, 3, 4, 5인 학생들 번호 앞에
# 100을 붙이기로 함 -> 101, 102, ...
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students2 = ["Iron man", "Thor", "I am groot"]
students2 = [len(i) for i in students2]
print(students2)

# 학생 이름을 대문자로 변환
students3 = ["Iron man", "Thor", "I am groot"]
students3 = [i.upper() for i in students3]
print(students3)