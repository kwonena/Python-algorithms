# open("파일이름", "목적", "한글 깨짐 방지")
# "w" : write(쓰는 것이 가능)
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 파일은 항상 닫아주어야 함

# "a" : append(뒤에 내용을 이어서 쓰기 가능)
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()
