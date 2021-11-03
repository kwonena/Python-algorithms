# __init__ : 파이썬의 생성자, 객체 생성시 자동으로 호출되는 부분
class Unit:
    def __init__(self, name, hp, damage):  # self를 제외한 모든 값을 입력해줘야 함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


# 객체 : 클래스로부터 만들어지는 것
marine1 = Unit("마린", 40, 5)  # Unit 클래스의 인스턴스
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
