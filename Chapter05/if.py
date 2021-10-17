# weather = "비"
weather = input("오늘 날씨는 어때요?") # input() : 사용자 입력 함수
if weather == "비" or weather == "눈": # or을 통해 조건을 다양화 시킬 수 있음
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

temp = int(input("오늘 기온은 어때요?"))
# input() 함수는 문자열로 입력을 받기 때문에 int로 감싸면서 자료형을 변경해줌 
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨예요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")