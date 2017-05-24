# -*- coding: utf-8 -*-

import pickle
import json
import pandas as pd
from weibospider import spider_run
from feature import get_features

def classify(uid):

  spider_run(uid)

  user = json.load('./weibo/%s.txt' % uid)

  features = get_features(user)

  model = pickle.load('./spam.model')

  test_X = pd.DataFrame.from_dict(features)

  ans = model.predict(test_X)

  return ans

if __name__ == '__main__':
  classification('2865101843')