import glob
import os
import numpy as np
import sys
current_dir = "C:/Users/nikhil/ENDO_CV/EAD2020_dataType_framesOnly/labels"
files = {}
 
for filename in os.listdir(current_dir):
    # print(filename)
    # filename_tmp = filename
    filename = current_dir + '/' + filename
    if os.path.isfile(filename) and filename.endswith(".txt") and not filename in files:
        # print(filename)
        s = ""
        with open(r"{}".format(filename), "r+") as file:
            # print(filename)
            # print("File : ", file)
            files[filename] = file.readlines()
            for line in files[filename]:
                c, x_left, y_left, w, h = line.split(' ')
                x_left = float(x_left)
                y_left = float(y_left)
                w = float(w)
                h = float(h)
                x_mid = x_left + (w/2.0)
                y_mid = y_left - (h/2.0)
                line_Str = c + " " + str(x_mid) + " " + str(y_mid) + " " + str(w) + " " + str(h) + '\n'
                s = s + line_Str
            print(s)
            file.close()
            # os.remove(filename)
        tmp = open(filename, 'w')
        tmp.write(s)
        tmp.close()