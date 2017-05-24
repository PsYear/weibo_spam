import pandas as pd
import xgboost as xgb
import numpy as np

spammer_order = "../feature.json"
raw_file = pd.read_json(open(spammer_order), orient='records')
raw_file.head()

data = raw_file.drop(['is_spammer'], axis=1)
target = raw_file[['is_spammer']]


from sklearn import preprocessing

def norm(data, column_name):
    x = data[column_name].values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    data_norm = pd.DataFrame(x_scaled)
    data[column_name] = data_norm
    return data

norm(data, 'time_interval_mean')
norm(data, 'time_interval_var')

from sklearn.model_selection import GridSearchCV
target['is_spammer']=target['is_spammer'].map(dict(yes=1, no=0))

