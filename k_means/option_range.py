#!/usr/bin/python

"""
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
import math
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

max_ = 0
min_ = 0xffffffff
for person in data_dict:
  # value = data_dict[person]["exercised_stock_options"]
  value = data_dict[person]["salary"]
  if math.isnan(float(value)):
    continue
  max_ = max(max_, value)
  min_ = min(min_, value)
print max_
print min_
