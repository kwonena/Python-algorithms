# 리스트 []

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) # []

# 다양한 자료형을 함께 사용할 수 있음
num_list = [5, 4, 3, 2, 1]
mix_list = ["이나", 20, True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

