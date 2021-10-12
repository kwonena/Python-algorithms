from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성

# 0을 포함하고 싶지 않을 때 +1 해줌
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

# 뒤의 값 미만으로 출력
print(randrange(1, 46)) # 1 ~ 46미만의 임의의 값 생성

# 양쪽 값을 모두 포함해서 출력
print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성