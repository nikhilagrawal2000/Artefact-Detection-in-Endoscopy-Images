import glob
import os
import numpy as np
import sys
current_dir = "C:/Users/nikhil/ENDO_CV/EAD2020_dataType_framesOnly/labels_aug_sheared"

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
				x_left_top, y_left_top, x_right_bottom, y_right_bottom, c = line.split()
				x_left_top = float(x_left_top)
				y_left_top = float(y_left_top)
				x_right_bottom = float(x_right_bottom)
				y_right_bottom = float(y_right_bottom)
				c = float(c)
				c = int(c)
				line_Str = str(c) + " " + str(x_left_top) + " " + str(y_left_top) + " " + str(x_right_bottom) + " " + str(y_right_bottom) + '\n'
				s = s + line_Str
			#print(s)
			file.close()
			# os.remove(filename)
		tmp = open(filename, 'w')
		tmp.write(s)
		tmp.close()