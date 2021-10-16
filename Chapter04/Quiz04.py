# Quiz) 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받는 이벤트이다.

# 조건1 : 20명이 참여하였고 아이디는 1~20이라고 가정
# 조건2 : 무작위 추첨, 중복X
# 조건3 : random 모듈의 suffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst) # 리스트 무작위 정렬
print(lst)
print(sample(lst, 1)) # 두번째 인자의 개수만큼 리스트에서 랜덤한 숫자를 출력함

from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users) # users의 type을 list로 변경

shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")