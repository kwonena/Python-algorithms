# 키워드 값으로 입력하면 순서가 바뀌어도 함수에 나열된 순서로 출력됨
def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")