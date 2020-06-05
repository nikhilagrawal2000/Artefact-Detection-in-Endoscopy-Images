import glob
import os
import numpy as np
import sys
import cv2
current_dir = "C:/Users/nikhil/ENDO_CV/EAD2020_dataType_framesOnly/gt_bbox_/gt_bbox_with_bottom_left_&_top_right"
current_dir_img = "C:/Users/nikhil/ENDO_CV/EAD2020_dataType_framesOnly/frames/"
files = {}
class_names = ["specularity", "saturation", "artifact", "blur", "contrast", "bubbles", "instrument", "blood"]
file_tmp = open("annotate.txt", 'w')
s_tmp = ""
for filename in os.listdir(current_dir):
	# print(filename)
	# filename_tmp = filename
	filename_tmp = filename
	filename = current_dir + '/' + filename
	filename_img = current_dir_img + filename_tmp[:-4] + ".jpg"
	img = cv2.imread(filename_img)[:, :, ::-1]
	size_1 = float(img.shape[0])
	size_2 = float(img.shape[1])
	if os.path.isfile(filename) and filename.endswith(".txt") and not filename in files:
		# print(filename)
		s = ""
		with open(r"{}".format(filename), "r+") as file:
			# print(filename)
			# print("File : ", file)
			files[filename] = file.readlines()
			for line in files[filename]:
				c, x_mid, y_mid, w, h = line.split(' ')
				x_mid = float(x_mid)
				y_mid = float(y_mid)
				w = float(w)
				h = float(h)
				x_bottom_left = x_mid - (w/2.0)
				y_bottom_left = y_mid - (h/2.0)
				x_top_right = x_mid + (w/2.0)
				y_top_right = y_mid + (h/2.0)
				x_bottom_left = (int)(x_bottom_left*size_2)
				y_bottom_left = (int)(y_bottom_left*size_1)
				x_top_right = (int)(x_top_right*size_2)
				y_top_right = (int)(y_top_right*size_1)
				line_Str = str(x_bottom_left) + " " + str(y_bottom_left) + " " + str(x_top_right) + " " + str(y_top_right) + " " + c + '\n'
				s = s + line_Str
				line_tmp = filename_img + "," + str(x_bottom_left) + "," + str(y_bottom_left) + "," + str(x_top_right) + "," + str(y_top_right) + "," + class_names[int(c)] + '\n'
				s_tmp = s_tmp + line_tmp
			print(s)
			file.close()
			# os.remove(filename)
		tmp = open(filename, 'w')
		tmp.write(s)
		tmp.close()
file_tmp.write(s_tmp)
file_tmp.close()