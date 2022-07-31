import os
# import natsort

# mp3 파일 -> wav 파일로 변환 후 새로운 폴더에 저장

# 현재 mp3 파일의 위치
file_location = 'mp3 파일이 들어있는 폴더의 위치'
file_list = os.listdir(file_location)       # save file list

# 폴더 내부에 있는 파일 리스트 열람
# file_list = natsort.natsorted(file_list)    # sort file list
# print(file_list)

# 새 폴더의 위치를 지정
fileNum = len(file_list) + 1
a = 1
os.mkdir('파일을 저장할 새 폴더의 위치{}/00{}_wav'.format(a, a))

# mp3를 wav로 변환, 기존 mp3 파일 자체를 wav로 바꿈
for i in range(1, fileNum):
    os.renames('mp3 파일의 위치{}/{}.mp3'.format(a, i), '변환된 wav 파일의 위치/00{}/00{}_wav/{}.wav'.format(a, a, i))
