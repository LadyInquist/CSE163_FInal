import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def ml_regressor(data):
    data = data[["budget", "score", "company", "director", "rating", "genre", "runtime", "gross", "votes"]]
    features = data.loc[:, data.columns != "score"]
    features = pd.get_dummies(features)
    labels = data["score"]
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    # Compute training accuracy
    train_predictions = model.predict(features_train)
    print('Train R2:',
            r2_score(labels_train, train_predictions))
    # Compute test accuracy
    test_predictions = model.predict(features_test)
    print('Test  R2:',
            r2_score(labels_test, test_predictions))

def data_preprocess(data):
    r = data['rating'] == "R"
    pg = data['rating'] == "PG"
    pg13 = data['rating'] == "PG-13"
    data = data[r | pg | pg13].copy()
    data = data[["budget", "score", "company", "director"]]
    features = data.loc[:, data.columns != "score"]
    features = pd.get_dummies(features)
    labels = data["score"]
    mse_scores = {}
    for i in range(1, 5, 1):
        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=i/10)
        model = DecisionTreeRegressor()
        model.fit(features_train, labels_train)
        test_predictions = model.predict(features_test)
        mse_scores[i] = r2_score(labels_test, test_predictions)
    print(mse_scores)

def ml_classifier(self):
    data = data[["budget", "score", "rating", "company"]]
    features = data.loc[:, data.columns != "rating"]
    features = pd.get_dummies(features)
    labels = data["rating"]
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(features_train, labels_train)

    # Compute training accuracy
    train_predictions = model.predict(features_train)
    print(train_predictions)
    print(labels_train)
    print('Train accuracy:', accuracy_score(labels_train,
                                            train_predictions))

    # Compute test accuracy
    test_predictions = model.predict(features_test)
    print('Test  accuracy:',
            accuracy_score(labels_test, test_predictions))
def to_month(release_date):
    release_date = str(release_date).split('(')[0]
    if len(release_date.strip().split(' ')) >= 3:
        month = dt.datetime.strptime(release_date.strip(),
                                    "%B %d, %Y")
        return int(month.month)
    else:
        return None
# Might not need this function at all actually


def movies_by_weekday(data):
    """
    Assuming that the data parameter is the IMDB dataframe,
    plots lines of best fit for both budget and profit
    as a factor of IMDB score.
    """
    r = data['rating'] == "R"
    pg = data['rating'] == "PG"
    pg13 = data['rating'] == "PG-13"
    data = data[r | pg | pg13].copy()
    data['month'] = data["released"].apply(to_month)
    data = data.sort_values('month')
    print(data)
    data = data[["rating", "score", "genre", "budget", "company", "runtime",
                "month"]]

    sns.catplot(x='month', col='rating', kind='count', data=data)
    plt.savefig('/home/weekday2.png')
