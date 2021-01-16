#########################
# Generating transparent images for 
#    1, 
#    2, 
# auther: Mingzhen Shao
# Data: Jan, 14, 2021

import cv2
import os
import glob
import numpy as np

def saturation(img_rgb, scale):

    img_hsv = cv2.cvtColor(img_rgb, cv2.cv2.COLOR_BGR2HSV).astype("float32")
    (h, s, v) = cv2.split(img_hsv)
    s = s * scale
    s = np.clip(s, 0, 255)
    img_hsv = cv2.merge([h, s, v])
    img_rgb = cv2.cvtColor(img_hsv.astype("uint8"), cv2.COLOR_HSV2BGR)
    
    return img_rgb   
    
def opacity(img_rgb, scale):
    img_rgba = cv2.cvtColor(img_rgb, cv2.cv2.COLOR_BGR2BGRA)
    #print(img_rgba.shape)
    img = np.array(img_rgba, dtype=np.float64)
    img /= 255.0

    a_channel = np.ones(img[:,:,0].shape, dtype=np.float)/100.0
    
    img[:,:,3] = img[:,:,3] * a_channel 

    img_out = np.uint8(img * 255)
    #print(img_out.shape)
   
    return img_out
    

scale = 100

if(not os.path.exists("Generated")):
    os.mkdir("Generated")

#Loading images in Input

for file in glob.glob('./Input/*.jpg'):
    path_name = os.path.join(os.path.abspath('./Input'), file)
    print(file)
    try:
        img_rgb = cv2.imread(file)
      
#        img_out = saturation(img_rgb, scale)
        img_out = opacity(img_rgb, scale)
        output_path = "./Generated/" + file.split('/')[-1].split('.jpg')[0] + str(scale) + '.png'       #png is the type that can save transparence.
       
    #    print(img_out)
    #    print(output_path)
        cv2.imwrite(output_path, img_out)
    
    except Exception as e:
        print(e)
        print("There must be something you want to print!!!")
        pass
        