# sep : 문자열 사이에 들어갈 문자열을 입력
# end : 문장의 끝 부분에 들어갈 문자열을 입력
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

# stdout : 표준출력으로 출력
# stderr : 표준에러로 출력
import sys
print("Python", "Java", file=sys.stdout) 
print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # items() : key와 value를 쌍으로 튜플로 출력해줌
    # print(subject, score)

    print(subject.ljust(5), str(score).rjust(4), sep=":")
    # ljust(n) / rjust(n) : n만큼의 공간을 확보하고 왼쪽/오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ..., 020
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # zfill(n) : n만큼의 공간을 확보하고 값이 없는 빈 공간을 0으로 채움

# 표준 입력
 # input으로 값을 받을 경우 항상 str(문자열)의 형태로 들어옴
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
print(type(answer))
