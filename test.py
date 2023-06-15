# -*- coding: utf-8 -*-
'''

'''
# @Time    : 2023/6/15 21:13
# @Author  : LINYANZHEN
# @File    : test.py
from sklearn.feature_extraction.text import CountVectorizer
import sklearn

print(sklearn.__version__)
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())
