# -*- coding: utf-8 -*-
'''
情感分析
'''
import pandas as pd
import flair
import numpy as np

# videoid = 'vjSljNr7TuY'
# videoid = "workshop_comment1"
sentiment_model = flair.models.TextClassifier.load('en-sentiment')
with open("youtube_video_ids.txt", "r") as file:
    nfile = len(file.readlines())
for i in range(nfile):
    df = pd.read_csv('workshop_comment' + str(i + 1) + '.csv')
    # df = pd.read_csv(videoid +'.csv', header = None, encoding='unicode_escape')

    df = df.dropna()
    df = df.reset_index(drop=True)

    sentiment = []
    score = []

    df.columns = ['comments']

    for sentence in df['comments']:
        if sentence == '' or sentence == np.nan:
            sentiment.append('')
            score.append('')
        else:
            sample = flair.data.Sentence(sentence)
            sentiment_model.predict(sample)

            sentiment.append(sample.labels[0].value)
            score.append(sample.labels[0].score)

    df['Sentiment'] = sentiment
    df['Score'] = score

    df.to_csv('workshop_comment' + str(i + 1) + '_sentiment.csv')
