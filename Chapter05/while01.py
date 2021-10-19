customer = "토르"
index = 5
while index >= 1:
    print("{0}님 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

# 무한루프 (Ctrl+c로 강제 종료 가능)
customer2 = "아이언맨"
index2 = 1
while True:
    print("{0}님 커피가 준비 되었습니다. {1}회 호출.".format(customer2, index2))
    index2 += 1
