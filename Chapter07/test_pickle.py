# pickle : 프로그램 상에서 사용하는 데이터를 파일 형태로 저장

import pickle
# profile_file = open("profile.pickle", "wb") # b : binary, pickle 사용시 꼭 써줘야 함
# profile = {"이름" : "권이나", "나이" : 24, "취미" : ["코딩", "게임", "영화"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close() 

# 파일에서 데이터 가져오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close() 