# with를 사용하면 이 전보다 편리하게 file을 쓰고 읽을 수 있음
# close를 해주지 않아도 됨

# pickle을 사용
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# pickle을 사용X
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())