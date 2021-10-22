# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 여자 : 키(m) x 키(m) x 21
# 남자 : 키(m) x 키(m) x 22

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height, gender): # 키 m 단위
    if gender == "여자":
        return height * height * 21
    else:
        return height * height * 22

height = 158 # cm 단위
gender = "여자"
weight = round(std_weight(height / 100, gender), 2) # round(숫자, 소수 n자리)
print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, weight))
