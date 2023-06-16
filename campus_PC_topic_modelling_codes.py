# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:41:55 2021
LDA
@author: steve
"""

import pandas as pd
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from gensim import matutils, models
import scipy.sparse
from collections import Counter
import argparse
import os
parser = argparse.ArgumentParser(description='youtube comment scrap and analysis')
parser.add_argument("--topic_num", type=int, default=2, help="LDA topic number")
args = parser.parse_args()
# how many files you have?
# nfile = 1
# 获取当前工作目录
current_directory = os.getcwd()

# 获取当前目录下以"workshop_comment"为前缀的csv文件列表
nfile = len([file for file in os.listdir(current_directory) if file.startswith("workshop_comment") and file.endswith(".csv")])

add_stop_words = ["really", "ve"]

stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)

stop_words = list(stop_words)

comment_list = []
# number of files
for i in range(nfile):
    df = pd.read_csv('workshop_comment' + str(i + 1) + '.csv')
    comment = ""
    for c in df.values:
        comment = comment + " " + str(c[0])
    comment_words_afterstop = ' '.join(
        [word.lower() for word in comment.split() if word.lower() not in stop_words and len(word) > 2])
    comment_list.append(comment_words_afterstop)

# check for commom adj in both groups
# for allcomments in comment_list:
#     counts = Counter(allcomments.split()).most_common(10)
#     print ( '\n' )
#     print (counts)

df = pd.DataFrame(comment_list, columns=['comments'])

# create a document-term matrix with only nouns
cvn = CountVectorizer(stop_words=stop_words)
data_cvn = cvn.fit_transform(df.comments)
# 此处有坑，sklearn版本过低，请安装1.2.2版本，否则会报错没有get_feature_names_out()方法
data_dtmn = pd.DataFrame(data_cvn.toarray(), columns=cvn.get_feature_names_out())
data_dtmn.index = df.index
df.to_csv("vjSljNr7TuY.csv")
# Create the gensim corpus
corpusn = matutils.Sparse2Corpus(scipy.sparse.csr_matrix(data_dtmn.transpose()))

# Create the vocabulary dictionary
id2wordn = dict((v, k) for k, v in cvn.vocabulary_.items())

ldan = models.LdaModel(corpus=corpusn, num_topics=args.topic_num, id2word=id2wordn, passes=30)
count = 0
for tp in ldan.print_topics():
    count += 1
    print("TOPIC " + str(count) + ":" + str(tp) + '\n')
print('\n')
corpus_transformed = ldan[corpusn]

print('----Topic Assignment ----')
count = 0
for a in corpus_transformed:
    count += 1
    print('Video ' + str(count) + ':')
    print(a)

# print(type(stop_words))
