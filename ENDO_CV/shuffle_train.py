import random
lines = open('train_shuffle.txt').readlines()
random.shuffle(lines)
open('train_shuffle.txt', 'w').writelines(lines)