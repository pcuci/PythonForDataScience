#!/usr/bin/env python
import urllib
urllib.urlretrieve("https://www.kaggle.com/c/bioresponse/download/train.csv", filename="data/train.csv")
urllib.urlretrieve("https://www.kaggle.com/c/bioresponse/download/test.csv", filename="data/test.csv")
urllib.urlretrieve("https://www.kaggle.com/c/bioresponse/download/svm_benchmark.csv", filename="data/svm_benchmark.csv")
