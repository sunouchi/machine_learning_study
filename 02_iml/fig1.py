# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# アイリスのデータセットを読み込む
data = load_iris()

# 各データを変数に設定
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target]

# plt.scatter(feature_names, features[0])
for t, marker, c in zip(xrange(3), '>ox', 'rgb'):
    sepal_length = features[target == t,0]
    sepal_width = features[target == t,1]
    plt.scatter(sepal_length,
                sepal_width,
                marker=marker,
                c=c)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
plt.show()
