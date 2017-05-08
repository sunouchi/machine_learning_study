# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# アイリスのデータセットを読み込む
data = load_iris()

# データを変数に格納する
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
species = data['target_names'][data['target']]

# versicolorとvirginicaを変数に格納する
setosa = (species == 'setosa')
features = features[~setosa]
species = species[~setosa]
virginica = (species == 'virginica')

# グラフの基準を設定する
t = 1.75
p0,p1 = 3,2

# グラフを描画する
xmin,xmax = [features[:,p0].min() * .9, features[:,p0].max() * 1.1]
ymin,ymax = [features[:,p1].min() * .9, features[:,p1].max() * 1.1]
plt.fill_between([t,xmax], [ymin,ymin], [ymax,ymax], color=(.7,.7,.7))
plt.fill_between([xmin,t], [ymin,ymin], [ymax,ymax], color=(1,1,1))
plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.plot([t,t], [ymin,ymax], 'k--', lw=2)
plt.plot([t-.1,t-.1], [ymin,ymax], 'k:', lw=2)
plt.scatter(features[species=='versicolor', p0],
            features[species=='versicolor', p1],
            marker='o',
            c='r')
plt.scatter(features[species=='virginica', p0],
            features[species=='virginica', p1],
            marker='x',
            c='b')

plt.show()

