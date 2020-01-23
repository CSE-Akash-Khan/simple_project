
#? In this project we will move our vedio,audio,document file in different different folder from one directory there every file stay togather. so we have to scan our file and have to move different file lets see
#todo: tutorial -- 231

import os, shutil
dict_extention = {
    'audio_extension' : ('.mp3','.m4a','.wav','.flac','MP3'),
    'video_extention' : ('.mp4','mkv','MKV','flv','mpeg'),
    'document_extention' : ('.doc','.pdf','.txt')

}

folderpath = input("enter folder path: ")

def file_finder(file_extention,folder_path):
    files = []
    for file in os.listdir(folder_path):
        for extention in file_extention:
            if file.endswith(extention):
                files.append(file)
    return files

# print(file_finder(document_extention,folderpath))
for extention_type,extention_tuple in dict_extention.items():
    folder_name = extention_type.split('_')[0] + ' files' #? ki namer folder ee file gulo rakha hobe-- ekhane protibare looping er somoy file er namta change hobe
    folder_path = os.path.join(folderpath,folder_name) #?folder tike kothay rakha hobe r sathe je name folder ti hobe-- ekhane protibare folder er name chage hower karone folder er path oo proti looping er somoy alada hobe
    os.mkdir(folder_path)
    for item in file_finder(extention_tuple,folderpath): #?ekhane item er modde thakbe files ja return korbe.jemon first time loop cholle thakbe sokol audio file,then video file the document file je gulo files return korbe
        item_path = os.path.join(folderpath,item) #? item er ekti temporary path banano hoyese
        item_move_path = os.path.join(folder_path,item) #? item tike je folder e move korano hobe seitir path
        shutil.move(item_path,item_move_path)
#     print(file_finder(extention_tuple,folderpath))

#!.....................................modify project.............................
#? uparer project ee kisu problem silo. jodi amra second time run kori ta hole return kore file alredy exist r file na thakle oo folder create hoye jay. so amra chassi sudo file thakley folder create hobe r ta na hole folder create hobena

import os, shutil
dict_extention = {
    'audio_extension' : ('.mp3','.m4a','.wav','.flac','MP3'),
    'video_extention' : ('.mp4','mkv','MKV','flv','mpeg'),
    'document_extention' : ('.doc','.pdf','.txt')
}

folderpath = input("Enter folder path: ")

def file_finder(file_extention,folder_path):
    files = []
    for file in os.listdir(folder_path):
        for extention in file_extention:
            if file.endswith(extention):
                files.append(file)
    return files

def alredy_exist(folder_location,tuple_extention):
    add = 0
    for file in os.listdir(folderpath):
        for extention in tuple_extention:
            if file.endswith(extention):
                add += 1
    return add

for extention_type,extention_tuple in dict_extention.items():
    store = alredy_exist(folderpath,extention_tuple)
     if store > 0:
        folder_name = extention_type.split('_')[0] + ' files'
        folder_path = os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in file_finder(extention_tuple,folderpath):
            item_path = os.path.join(folderpath,item)
            item_move_path = os.path.join(folder_path,item)
            shutil.move(item_path,item_move_path)


#...........use list comprehension...............
# import os, shutil
# dict_extention = {
#     'audio_extension' : ('.mp3','.m4a','.wav','.flac','MP3'),
#     'video_extention' : ('.mp4','mkv','MKV','flv','mpeg'),
#     'document_extention' : ('.doc','.pdf','.txt')
# }

# folderpath = input("Enter folder path: ")

# def file_finder(file_extention,folder_path):
#     return [file for file in os.listdir(folder_path) for extention in file_extention if file.endswith(extention)]

# def alredy_exist(folder_location,tuple_extention):
#     return ['1' for file in os.listdir(folder_location) for extention in tuple_extention if file.endswith(extention)]

# for extention_type,extention_tuple in dict_extention.items():
#     store = alredy_exist(folderpath,extention_tuple)
#     if len(store) > 0: #? its used for list comprehension
#         folder_name = extention_type.split('_')[0] + ' files'
#         folder_path = os.path.join(folderpath,folder_name)
#         os.mkdir(folder_path)
#         for item in file_finder(extention_tuple,folderpath):
#             item_path = os.path.join(folderpath,item)
#             item_move_path = os.path.join(folder_path,item)
#             shutil.move(item_path,item_move_path)
