# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:20:00 2022
爬虫
@author: steve
"""

from selenium import webdriver

import time
import csv
# 需要爬的youtube影片id
# youtubeid_list = ["0GZSfBuhf6Y", "Gaf_jCnA6mc"]
with open("youtube_video_ids.txt", "r") as f:
    youtubeid_list = f.readlines()
driver = webdriver.Chrome()
video_index = 1
for youtubeid in youtubeid_list:
    driver.get('https://www.youtube.com/watch?v=' + youtubeid)

    # now wait let load the comments and set the wait time and scolling

    initial_value = 1
    next_value = 1

    for i in range(10):
        driver.execute_script("window.scrollTo({},{});".format(initial_value, next_value))
        initial_value = next_value
        next_value += 800
        time.sleep(5)

    comment_div = driver.find_element("xpath", '//*[@id="contents"]')
    comments = comment_div.find_elements("xpath", '//*[@id="content-text"]')
    '''for comment in comments:
        print(comment.text)'''
    print(len(comments))
    # print(type(comments)) # list

    comment_list = []
    for comment in comments:
        if comment != "":
            comment_list.append(comment.text)
            print(comment.text)
            # print (modified)

    # write to a csv file:


    with open('workshop_comment{}.csv'.format(video_index), 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for commentrow in comment_list:
            newline = []
            newline.append(commentrow)
            writer.writerow(newline)
    video_index += 1
