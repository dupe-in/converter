# import os
# import natsort
# import playsound

# def search(directory):
#     filenames = os.listdir(directory)
#     print("filesnames :", filenames)
#     print("f_type :", type(filenames))
#     # for filename in filenames:
#     #     full_filename = os.listdir(directory)
#     # print("full_type :", type(full_filename))
#     # string type "number" sorting
#     full_filename = natsort.natsorted(filenames)
#     # print(full_filename)
#     playsound.playsound('1.mp3')


# # 여기서 경로를 설정
# search("C:/Users/ssubi/OneDrive/바탕 화면/연구실/음성 파일/9433")

import os
import pydub
import natsort

file_location = 'C:/Users/ssubi/OneDrive/바탕 화면/연구실/음성 파일'
file_list = os.listdir(file_location)       # save file list
file_list = natsort.natsorted(file_list)    # sort file list
print(file_list)
fileNum = len(file_list) + 1
os.mkdir('C:/Users/ssubi/OneDrive/바탕 화면/연구실/음성 파일/변환 파일')     # make new directory

for i in range(1, fileNum):
    sound = pydub.AudioSegment.from_mp3("C:/Users/ssubi/OneDrive/바탕 화면/연구실/음성 파일/{}.mp3".format(file_list[i]))
    sound.export("C:/Users/ssubi/OneDrive/바탕 화면/연구실/음성 파일/변환 파일/{}.wav".format(i), format="wav")


# sound = pydub.AudioSegment.from_mp3("C:/Users/ssubi/OneDrive/바탕 화면/연구실/음성 파일/9433/{}.mp3".format('1'))
# sound.export("C:/Users/ssubi/OneDrive/바탕 화면/연구실/음성 파일/9433/{}.wav".format('1'), format="wav")
