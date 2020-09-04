import os
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

#os.path.isfile(os.path.join(Data_dir, name))

target_dir = sys.argv[1]
os.chdir(target_dir)
os.system("mkdir propety_tmp")

for file in os.listdir('./'):
#    print(files)
#    for file in files:
    path_name = os.path.join(os.path.abspath('./'), file)
    #print(file)
    if(os.path.isfile(path_name)):
        img_path = path_name
        dir_path = os.path.join('propety_tmp', file)
        res = jpg_mode_check(img_path)
        if(res):
            print(img_path + "  GOOD BOY!")
            subprocess.call("cp " + img_path + ' ' + dir_path)
   
#jpg_mode_check("./demo.jpg")

#pause = input("Give something")        # Using this for Ubuntu Python3 & raw_input for Python2!



#For Windows ONLY!
os.system("pause")
