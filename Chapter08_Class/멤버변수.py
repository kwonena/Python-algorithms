# 멤버변수 : 클래스 내에서 정의된 변수
class Unit:
    def __init__(self, name, hp, damage):  # self를 제외한 모든 값을 입력해줘야 함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


# 레이스 : 공중 유닛
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # 기능 업그레이드 되었다고 가정

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 파이썬은 객체에 변수를 새로 만들어서 사용 가능
