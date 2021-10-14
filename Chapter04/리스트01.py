# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있나요?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탔습니다
subway.append("하하")
print(subway)

# 정형돈씨가 유재석, 조세호 사이에 탔습니다
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냅니다
# 뒤에서 차례대로 빠짐
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있나요?
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
