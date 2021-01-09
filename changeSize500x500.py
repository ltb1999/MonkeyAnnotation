import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Replace path by the directory that stores the images
path = r'C:\Users\Lin\Downloads\Lin_1_8_5'
# Make new directory to store the resized pictures
newpath = os.path.join(path,"Resized folder")
print(os.path.isdir(newpath))
if not os.path.isdir(newpath):
    directory = os.mkdir(newpath,0o666)
for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        img = cv2.imread(os.path.join(path,filename), 1)
        newname = filename[:filename.find('.')]+"_resized.jpg"
        # Change new dimension with max size 500x500
        newwidth = 500
        newheight = int(img.shape[0] * newwidth/img.shape[1])
        dim = (newwidth, newheight)
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(os.path.join(newpath,newname),resized)
        # cv2.destroyAllWindows()
    else:
        continue
