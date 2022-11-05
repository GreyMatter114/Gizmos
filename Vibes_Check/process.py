import pandas as pd
import numpy as np
import pickle
# Importing the dataset
from sklearn.feature_extraction.text import CountVectorizer

def train(cv):
    dataset = pd.read_csv('../IMDB Dataset.csv', delimiter = ',')
    # Cleaning the texts
    corpus=[]
    for i in range(0, 1000):
        review =dataset['review'][i]
        corpus.append(review)

    # Creating the Bag of Words model
    y = dataset.iloc[:, 1].values
    y=y[:1000]
    X=cv.fit_transform(corpus).toarray()
    # Splitting the dataset into the Training set and Test set
    # Training the Naive Bayes model on the Training set
    from sklearn.naive_bayes import BernoulliNB
    classifier = BernoulliNB()
    classifier.fit(X, y)
    pickle.dump(classifier,open('Save.pkl','wb+'))
# Predicting the Test set results
def main(n):
    muse=['negative','positive']
    cv=CountVectorizer(max_features=len(n.split())-1)
    train(cv)
    classifier=pickle.load(open('Save.pkl','rb'))
    y_pred = classifier.predict(cv.fit_transform([n]).toarray())
    return muse.index(y_pred)
