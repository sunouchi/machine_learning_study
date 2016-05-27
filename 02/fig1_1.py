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

# すべてのパターンを描画する
pairs = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
for i, (p0, p1) in enumerate(pairs):
    plt.subplot(2, 3, i+1)
    for t, marker, c in zip(xrange(3), '>ox', 'rgb'):
        plt.scatter(features[target==t, p0],
                    features[target==t, p1],
                    marker=marker,
                    c=c)
        plt.xlabel(feature_names[p0])
        plt.ylabel(feature_names[p1])
        plt.xticks([])
        plt.yticks([])

plt.show()

