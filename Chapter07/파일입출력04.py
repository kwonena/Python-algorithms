# 리스트에 값을 넣어서 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 가져온 뒤 list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()