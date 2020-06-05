import glob
import os
import numpy as np
import sys
current_dir = "C:/Users/nikhil/ENDO_CV/EAD2020_dataType_framesOnly/labels_aug"

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
				c, x_mid, y_mid, w, h = line.split(' ')
				x_mid = float(x_mid)
				y_mid = float(y_mid)
				w = float(w)
				h = float(h)
				w = abs(w)
				h = abs(h)
				if x_mid - w/2.0 <= 0.0 :
					continue
				if x_mid + w/2.0 >= 1.0 :
					continue
				if y_mid - h/2.0 <= 0.0 :
					continue
				if y_mid + h/2.0 <= 1.0 :
					continue
				# x = (x1 + w)/2.0
				# y = (y1 + h)/2.0
				# h = abs(y1 - h)
				# w = abs(x1 - w)
				line_Str = c + " " + str(x_mid) + " " + str(y_mid) + " " + str(w) + " " + str(h) + '\n'
				s = s + line_Str
			print(s)
			file.close()
			# os.remove(filename)
		tmp = open(filename, 'w')
		tmp.write(s)
		tmp.close()