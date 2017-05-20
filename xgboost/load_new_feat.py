# coding: utf-8
import pandas as pd

def load_old_feat():
    spammer_order = "../data/spammer_order.csv"
    feat_list = ['post_num', 'follower_num', 'followee_num', 'content_similar',
     'figure_jing', 'figure_url', 'figure_face', 'figure_RRT', 'figure_face_every',
     'figure_jing_every', 'figure_url_every', 'figure_url_single', 'figure_jing_single',
     'figure_at', 'figure_at_every', 'figure_at_single', 'average_repost', 'average_comm',
     'late_night_times', 'is_regular', 'shorttime_times', 'active_day_ratio', 'day_interval_variance',
     'day_in_variance', 'follow_ratio']

    raw_file = pd.read_csv(spammer_order)
    data = raw_file[feat_list]
    target = raw_file[['is_spammer']]
    return data, target

def load_feat():
    spammer_order = "../feature.json"
    all_feat_list = ['figure_RRT', 'average_comm', 'figure_at_sigle', 'hashtag', 'reputation',
                     'late_night_times', 'followee_num', 'follow_ratio', 'post_num', 'figure_at',
                     'active_day_ratio', 'mention', 'day_interval_variance', 'figure_at_every',
                     'test_similarity', 'text_similarity', 'url', 'time_interval_mean', 'time_interval_var']

    raw_file = pd.read_json(open(spammer_order), orient='records')

    idx_title = ['id'] + all_feat_list + ['is_spammer']
    raw_file.rename(columns={i: idx_title[i] for i in range(21)}, inplace=True)

    aval_feat_list = ['hashtag', 'reputation', 'post_num', 'mention', 'test_similarity', 'url', 'time_interval_mean',
                     'time_interval_var']
    data = raw_file[aval_feat_list]
    target = raw_file[['is_spammer']]

    return data, target
