from img_classify import img_analysis
import os

from gensim.models import KeyedVectors
str=raw_input("Enter Picture name ")
print str
path="./input/"+str
word_list=img_analysis(path)
print("Top predictions : ")
for w in word_list:
    print(w)

