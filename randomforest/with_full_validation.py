"""
Random Forest rough validation process..

1 Devide train and test data
2 Hyperparameter tuning for train data
3 Output precision, accuracy and recall

"""

import myutil
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random

# X, y = myutil.X_y('/users/yui/projects/accumu/feature/feature.csv', shuffled=True)
X = list()
y = list()
with open('/users/yui/projects/accumu/feature/feature.csv') as f:
    lines = f.read().split('\n')
    random.shuffle(lines)
    for line in lines:
        if len(line) < 4:
            continue
        X.append([float(x) for x in line.split(',')[5:-1]])
        y.append(float(line.split(',')[-1]))
# 1 Devide train and test data
train_X, train_y, test_X, test_y = myutil.devide_train_test(X, y, 0.8)

# 2 Hyperparamter tuning for train data
myutil.tune_hyperparameters(train_X, train_y, random_search=True, grid_search=False)
clf = RandomForestClassifier(min_samples_split=2, bootstrap=True, criterion='entropy', min_samples_leaf=1, max_features=1, max_depth=None)
clf.fit(train_X, train_y)

# 3 Output precision, accuracy and recall
print(myutil.validate(clf, test_X, test_y))



