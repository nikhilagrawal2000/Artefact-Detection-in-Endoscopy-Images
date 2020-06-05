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
				c, x1, y1, x2, y2 = line.split(' ')
				x1 = float(x1)
				y1 = float(y1)
				x2 = float(x2)
				y2 = float(y2)  
				# if x1 > 1:
				# 	x1 = 1.0
				# if y1 > 1:
				# 	y1 = 1.0
				# if x1 < 0:
				# 	x1 = 0.0
				# if y1 < 0:
				# 	y1 = 0.0
				# if x2 > 1:
				# 	x2 = 1.0
				# if y2 > 1:
				# 	y2 = 1.0
				# if x2 < 0:
				# 	x2 = 0.0
				# if y2 < 0:
				# 	y2 = 0.0
				x = (x1 + x2)/2.0
				y = (y1 + y2)/2.0
				h = abs(y1 - y2)
				w = abs(x1 - x2)
				# if h > 1:
				# 	h = 1.0
				# if w > 1:
				# 	w = 1.0
				# if h < 0:
				# 	h = 0.0
				# if w < 0:
				# 	w = 0.0
				line_Str = c + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + '\n'
				s = s + line_Str
			#print(s)
			file.close()
			# os.remove(filename)
		tmp = open(filename, 'w')
		tmp.write(s)
		tmp.close()