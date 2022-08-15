import os
import pydub

def mp3_converter(dir_loc):
    # dir_loc 폴더에 있는 모든 파일 읽어오기
    file_list = os.listdir(dir_loc)

    # 폴더 내부에 있는 파일 리스트 열람
    file_list_mp3 = []
    for file in file_list:
        if file.endswith('.mp3'):
            file_list_mp3.append(file)

    fileNum = len(file_list) + 1
    
    save_dir = dir_loc.split('/')[-1] + '_wav'
    temp_dir = dir_loc.split('/')[:-1]
    temp_dir = '/'.join(temp_dir)
    temp = os.listdir(temp_dir)
    if not save_dir in temp:
        os.mkdir(temp_dir + '/' + save_dir)

    for f_name in file_list_mp3:
        sound = pydub.AudioSegment.from_file(dir_loc + '/' + f_name)
        converted_file_name = f_name.replace('mp3', 'wav')
        final_dir =  '{}/{}/{}'.format(temp_dir, save_dir, converted_file_name)
        # sound.export(temp_dir + '/' + save_dir + '/' + converted_file_name , format="wav")
        sound.export(final_dir, format="wav")

if __name__=='__main__':
    target_dir = 'mp3 파일 위치'
    mp3_converter(target_dir)