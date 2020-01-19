from sklearn import ensemble
from sklearn import svm
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline


def get_default_classfiers():
    return [
        KNeighborsClassifier(3),
        KNeighborsClassifier(7),
        LogisticRegression(solver='lbfgs', tol=1e-2, max_iter=200, random_state=1337),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        RandomForestClassifier(n_estimators=100, min_samples_leaf=3, random_state=1337),
        GradientBoostingClassifier(n_estimators=100, learning_rate=0.25, max_depth=6,
                                   max_features='sqrt', subsample=0.8, random_state=1337),
        AdaBoostClassifier(random_state=1337),
        GaussianNB(),
        svm.SVC(kernel='poly', gamma='auto'),
    ]


def get_default_classifiers_names():
    return [
        '3-Nearest Neighbors',
        '7-NearestNeighbors',
        'Logistic Regression',
        'Random Forest',
        'Random Forest (more trees)',
        'Gradient Boosting',
        'Ada Boosting',
        'Naive Bayes',
        'Support Vector Machine'
    ]


def get_default_regressors():
    return [
        ensemble.GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                           max_depth=4, max_features='sqrt',
                                           min_samples_leaf=15, min_samples_split=10,
                                           loss='huber', random_state=42),
        ensemble.GradientBoostingRegressor(learning_rate=0.05, max_features='sqrt', loss='huber',
                                           min_impurity_split=None, min_samples_leaf=15,
                                           min_samples_split=10, n_estimators=12000,
                                           random_state=42),
        make_pipeline(preprocessing.RobustScaler(), linear_model.Lasso(alpha=0.0005, random_state=42)),
        make_pipeline(preprocessing.RobustScaler(), linear_model.ElasticNet(alpha=0.0005, l1_ratio=.9,
                                                                            max_iter=10000, random_state=42)),
        ensemble.RandomForestRegressor(n_estimators=200, min_samples_leaf=3, random_state=42),
        ensemble.ExtraTreesRegressor(n_estimators=200, min_samples_leaf=3, random_state=42),
        linear_model.HuberRegressor(),
        linear_model.LinearRegression(),
        svm.SVR(kernel='poly', gamma='auto'),
        KNeighborsRegressor(n_neighbors=5)
    ]


def get_default_regressors_names():
    return [
        'Gradient Boosting 1',
        'Gradient Boosting 2',
        'Lasso',
        'Elastic Net',
        'Random Forest',
        'Extremely Random Forest',
        'Huber Rehressor',
        'Support Vector Machine',
        '5-Nearest-Neighbors'
    ]
