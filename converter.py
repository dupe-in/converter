import os
import pydub
# import natsort

# mp3 파일 -> wav 파일로 변환 후 새로운 폴더에 저장

# 현재 mp3 파일의 위치
file_location = 'mp3 파일이 들어있는 폴더의 위치'
file_list = os.listdir(file_location)

# 폴더 내부에 있는 파일 리스트 열람
# file_list = natsort.natsorted(file_list)
# print(file_list)

# 새 폴더의 위치를 지정
fileNum = len(file_list) + 1
a = 1
os.mkdir('wav 파일을 저장할 새 폴더의 위치'.format(a, a))

# mp3를 wav로 변환, mp3 파일은 기존 위치에 두고 새 폴더 내부에 wav를 저장
for i in range(1, fileNum):
    sound = pydub.AudioSegment.from_mp3("mp3 파일의 위치/{}/{}.mp3".format(a, i))
    sound.export("변환된 wav 파일의 위치/00{}/00{}_wav/{}.wav".format(a, a, i), format="wav")