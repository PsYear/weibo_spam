import os
import re
import json
import jieba
import numpy as np
from datetime import datetime

import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# stop_words = [word.strip() for word in open('stop_word.txt', 'r').readlines()]
# stop_words += [' ']

def str2time(s):
    ans = None
    if s.startswith('今天'):
        ans = datetime.today()
        t = datetime.strptime(s.split(' ')[1], '%H:%M')
        ans = ans.replace(hour = t.hour, minute = t.minute)
        return ans
    try:
        ans = datetime.strptime(s, '%m月%d日 %H:%M')
        ans = ans.replace(year = datetime.today().year)
        return ans
    except:
        try:
            ans = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
            return ans
        except:
            return None

def get_features(user):
    vector = {
        'reputation'            : 0,
        'mention'               : 0,
        'hashtag'               : 0,
        'url'                   : 0,
        'text_similarity'       : 0,
        'time_interval_mean'    : 0,
        'time_interval_var'     : 0,
        'post_num'              : 0,

        'active_day_ratio'      : 0,
        'active_day_num'        : 0,
#         'follow_ratio'          : 0,
#         'figure_RRT'            : 0,
        'comment_num'          : 0,
#         'figure_at_every'       : 0,
#         'late_night_times'      : 0,
#         'figure_at_sigle'       : 0,
#         'figure_at'             : 0,

        'followers_num'         : 0, # new added
        'following_num'         : 0,
        'content_length'        : 0,

        'upvote_num'            : 0,
        'forwarded_num'           : 0,
        'forward_weibo_num'     : 0
    }

    # 声望：关注他的人与他关注的人之比
    vector['reputation'] = float(user['followers_num']) / float(user['following_num'])
    vector['followers_num'] = float(user['followers_num'])
    vector['following_num'] = float(user['following_num'])

    # '@'次数和'#'次数：
    vector['mention'] = 0
    vector['hashtag'] = 0
    vector['url']     = 0
    posts   = []
    time_intervals    = []
    prev_time         = None
    post_lens = []
    comment_num = 0
    upvote_num = 0
    forwarded_num = 0
    forward_weibo_num = 0

    days_set = set()

    for post in user['weibo']:
        if '@' in post['content']:
            vector['mention'] += 1
        if '#' in post['content']:
            vector['hashtag'] += 1
        if 'http://' in post['content']:
            vector['url'] += 1
        # words = list(jieba.cut(post['content']))
        # words = [word for word in words if word not in stop_words]
        # posts.append(' '.join(words))

        curr_time = str2time(' '.join(post['time'].split()[:2]))
        if curr_time == None:
            continue
        if prev_time != None:
            time_intervals.append((prev_time - curr_time).seconds)
            days_set.add((prev_time - curr_time).days)

        prev_time = curr_time

        post_lens.append(len(post['content']))
        comment_num += int(post['comment'])
        upvote_num += int(post['upvote'])
        forwarded_num += int(post['forward'])
        forward_weibo_num += int(post['forward_flag'])

    if len(time_intervals) > 0:
        vector['time_interval_mean'] = np.mean(time_intervals)
        vector['time_interval_var'] = np.var(time_intervals)

    vector['content_length'] = np.mean(post_lens)

    vector['post_num'] = int(user['weibos_num'])
    vector['comment_num'] = comment_num
    vector['active_day_num'] = len(days_set)
    if max(days_set) == 0:
        print(user)
        vector['active_day_ratio'] = 0
    else:
        vector['active_day_ratio'] = 1.0*len(days_set)/max(days_set)
    vector['upvote_num'] = upvote_num
    vector['forwarded_num'] = forwarded_num
    vector['forward_weibo_num'] = forward_weibo_num

    # posts之间的文本相似度
    # try:
    #     vectorizer = CountVectorizer()
    #     transformer = TfidfTransformer()
    #     tfidf = transformer.fit_transform(vectorizer.fit_transform(posts))
    #     matrix = (tfidf * tfidf.T).A
    #     vector['text_similarity'] = np.mean(matrix)
    # except:
    #     print(user)
    vector['text_similarity'] = 1
    return vector
