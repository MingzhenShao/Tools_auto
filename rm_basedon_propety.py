'''
#Remove folders based on assigned propety
parameter type: python rm_basedon_propety.py img_dir dump_dir

The dump name: IMG_20200818120000_FrameNum[777]
The image name: 10X_AB1234_IMG_20200818_120000.jpg

#Mingzhen Shao
#2020/8/17
'''

import os
import glob
import shutil
import exifread
import subprocess
import sys

def jpg_mode_check(img_path):
    demo = open(img_path, 'rb')
    tags = exifread.process_file(demo)

    #print(tags.keys())
  #  print(tags)
    #print(tags['EXIF UserComment'].values)
    try:
        comment = tags['EXIF UserComment'].values.strip()
        comment_list = comment.split('; ')
        #print(comment_list)

        dict_comment = {}
        for tmp_member in comment_list:
            member = tmp_member.strip()
         #   print(member, member.split(': ')[0], member.split(': ')[1])
            try:
                dict_comment[member.split(': ')[0]] = member.split(': ')[1]
            except Exception:
                continue
           # list_comment.append(tmp_member.strip())
  #      print(dict_comment)
        if(dict_comment['sceneMode'] != "32768"):
            print(img_path + "  NG!")
            return False
        else:
            return True
            
    except Exception:
        print(img_path + "  File Error!")
        return False
   
    return False
#exit_data = img._getexif()

def get_folder_match_err(dump_dir, file, dump_save_path):
## This is a goog way to avoid moving the folders with the same folder name by in wrong size (the files inside is not the same name)
        #pass
    flag = 0
    forder_name = file.split('.jpg')[0]
    key_word_list = forder_name.split('_')
#    print(forder_name)
    file_name = key_word_list[-2]+key_word_list[-1]
    
#    print(file_name)
    for fold in os.listdir(dump_dir):
        path_name = os.path.join(os.path.abspath(dump_dir), fold)
        if(os.path.isdir(path_name)):
     #       if(flag == 1):
      #          break
       #     continue
            if(len(fold.split('_'))>2):
                match_key = fold.split('_')[1]
            else:
                continue
            
            match_key_vary = str(int(match_key[:14])-1)  
      
            if(file_name == match_key[:14] or file_name == match_key_vary):     
            #    dump_dir = os.path.join(root_dump, dir_dump)
           #     print(raw_name, match_key)
              #  print(root_dump)
                try:
                    shutil.copytree(path_name, os.path.join(dump_save_path, fold))
                except Exception:
                    continue

          #      os.system('cp -r '+ str(path_name) + ' ' + dump_save_path)       
                
                # the folder_name should not have space!!!


    

target_dir = sys.argv[1]
os.chdir(target_dir)
os.system("mkdir propety_tmp")

dump_dir = sys.argv[2]

for file in os.listdir('./'):
#    print(files)
#    for file in files:
    path_name = os.path.join(os.path.abspath('./'), file)
    #print(file)
    if(os.path.isfile(path_name)):
        img_path = path_name
        dir_path = './propety_tmp'
        res = jpg_mode_check(img_path)
        if(res):
            print(img_path + "  GOOD BOY!")
            subprocess.call("cp " + img_path + ' ' + dir_path)
            dump_save_path = os.path.join(os.path.abspath('./'), 'propety_tmp/')
            get_folder_match_err(dump_dir, file, dump_save_path)
   
#jpg_mode_check("./demo.jpg")

#pause = input("Give something")        # Using this for Ubuntu Python3 & raw_input for Python2!

#For Windows ONLY!
os.system("pause")

