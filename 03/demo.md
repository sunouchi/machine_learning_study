# TensorFlow Tutorials - MNIST For ML Beginners
[MNIST For ML Beginners](https://www.tensorflow.org/versions/r0.9/tutorials/mnist/beginners/index.html)

## Softmax Regression とは
- 日本語：ソフトマックス回帰
- 入力データを確率ベクトル（非負数で、かつ和が1）に変換する

## Cross Entropy とは
- 日本語：交差エントロピー
- コスト関数（損失関数）のひとつ
- コスト関数とは：訓練のためには何が良いモデルなのか定義する必要がある。良いモデルからどれぐらい外れているかを返す関数
- 出力が確率ベクトルである必要がある。そのためにSoftmax関数による正規化を行う

## Gradient Descent とは
- 日本語：勾配降下法
- Cross Entropyの誤差を最小化する
- [こんなイメージ](https://www.google.co.jp/search?q=gradient+descent&espv=2&biw=1251&bih=1034&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjt2rzWnNHNAhVFjJQKHTmyDy4Q_AUIBigB)

## 参考記事
- Sessionについて: [TensorFlowで始める深層学習(2)サンプルコードから読み解くデータフロー・グラフ/Pythonエコシステム](http://developers.gnavi.co.jp/entry/tensorflow-deeplearning-2_1)
