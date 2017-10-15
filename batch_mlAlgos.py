
#Decision tree
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
print(iris.feature_names)
print(iris.data)
print(iris.target)
print(iris.target_names)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

import graphviz
dot_data = tree.export_graphviz(clf,out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")
# http://scikit-learn.org/stable/modules/tree.html#decision-trees
# https://medium.com/towards-data-science/decision-trees-and-random-forests-for-classification-and-regression-pt-1-dbb65a458df

# Random Forrest
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=4,
                           n_informative=2, n_redundant=0,
                           random_state=0, shuffle=False)
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)
# RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#             max_depth=2, max_features='auto', max_leaf_nodes=None,
#             min_impurity_decrease=0.0, min_impurity_split=None,
#             min_samples_leaf=1, min_samples_split=2,
#             min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#             oob_score=False, random_state=0, verbose=0, warm_start=False)

# n_estimators=10 number of trees in forrest
#criterian  - quality of a split
# max_features - number of features to consider when looking for the best split:


print(clf.feature_importances_)
print(clf.predict([[0, 0, 0, 0]]))

# https://medium.com/machine-learning-101/chapter-5-random-forest-classifier-56dc7425c3e1
# http://www.kdnuggets.com/2016/09/reandom-forest-criminal-tutorial.html