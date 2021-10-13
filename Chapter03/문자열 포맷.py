# print("a" + "b")
# print("a" , "b")

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

# %s
print("나는 %s살입니다." % 20) # %s는 모든 표기 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨강"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강")) # 인덱스 순서를 변경할 수 있음

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f를 문장 처음에 써주면 해당 변수로 출력 가능
