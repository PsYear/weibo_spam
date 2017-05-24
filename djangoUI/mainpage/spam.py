# -*- coding: utf-8 -*-
import pickle
import json
import pandas as pd
from mainpage.weibospider import spider_run
from mainpage.feature import get_features
import os
def classify(uid):
  if not os.path.exists('./weibo/%s.txt' % uid):
      spider_run(int(uid))

  user = json.load(open('./weibo/%s.txt' % uid))

  features = get_features(user)
  features['id'] = int(uid)

  model = pickle.load(open('./mainpage/spam.model', 'rb'))

  test_X = pd.DataFrame([features])
  print(test_X)
  ans = model.predict(test_X)

  return ans

if __name__ == '__main__':
  classification('5182188730')
