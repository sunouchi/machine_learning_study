# -*- coding:utf-8 -*-
from sklearn import datasets, svm, cross_validation

# データの読み込み
iris = datasets.load_iris()

# 学習
svc = svm.SVC();
scores = cross_validation.cross_val_score(svc, iris.data, iris.target, cv=5)

# 結果表示
print scores
print "Accuracy :", scores.mean();
