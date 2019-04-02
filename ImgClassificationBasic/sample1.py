from img_classify import img_analysis
import os

from gensim.models import KeyedVectors

model_bin_file = "w2v.glove.6B.300d.bin"
model = KeyedVectors.load_word2vec_format(model_bin_file, binary=True)
st=raw_input("Enter Picture name ")
print st
path="./input/"+st
word_list=img_analysis(path)
print("Image : ",st)
print("Top predictions : ")
for w in word_list:
    print(w)
for w in word_list:

    keyword = str(w[1]).replace("_","")
    
    print("Word : ",keyword)
    print ("Synonyms : ")
    try:
        print(model.wv.most_similar(positive=keyword))
    except:
        pass
    print("\n----------------------\n")
