# 지역변수 : 함수내에서만 사용
# 전역변수 : 프로그램내에서 모두 사용

gun = 10 # 전역 변수

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무를 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))