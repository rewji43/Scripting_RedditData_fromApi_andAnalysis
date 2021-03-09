#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
import praw
import re
import pymongo
from pymongo import MongoClient
import json
import pandas as pd
import emoji
import datetime as dt


# In[48]:


def get_date(created):
    return dt.datetime.fromtimestamp(created)


# In[63]:


#ทำการสร้าง db ของ mongo โดยจะใช้เป็นพื้นที่ localhost
client = MongoClient('localhost',27017)
db = client.reddit_db
reddit_collection = db.reddit_collection
reddit_collection.create_index([('id',pymongo.ASCENDING)] , unique = False)


# In[70]:


if __name__ == '__main__':
    #Set ค่าต่างๆสำหรับในการใช้ api
    reddit = praw.Reddit(client_id = 'yaMdjnRgR55yvQ',                         client_secret='HWv6UlEMDqwbKRDoyICDPHkZ1jM',                          user_agent='Rewji',                          username='rewji',                          password='rewwin0973189054')

    subreddit = reddit.subreddit('BlackPink')  #ค้นหาจากตรงนี้

    for submission in subreddit.top(limit=1000):
        topics_dict = { 
                    "title": submission.title,
                    "score": submission.score,
                    "id": submission.id,
                    "url":submission.url,
                    "comms_num": submission.num_comments, 
                    "created": submission.created, 
                    "body": submission.selftext
                }
        #เมื่อได้ข้อมูลแล้วให้ทำการ insert ลง db ที่สร้างขึ้นมาตอนแรกเลย โดย format ที่นำเข้า db จะเป็น json
        try:
            db.reddit_collection.insert(topics_dict)
            print('ok')
            
        #ดัก error ที่จะเกิดตอน insert
        except Exception as e:
            print(e)
            print('error')


# In[ ]:




