#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib


# In[2]:


def general_classification(data):
    df=pd.read_csv(r'/home/aakash/Downloads/Anxiety - Sheet1.csv')
    X=df.Questions
    y = df.type
    text_clf_svm = Pipeline([('vect', CountVectorizer()),
                          ('tfidf', TfidfTransformer()),
                          ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
                                            alpha=1e-3, n_iter=5, random_state=42)),
    ])

    text_clf_svm.fit(X,y)
    predicted_svm = text_clf_svm.predict(data)
    predicted_svm=joblib.dumb(predicted_svm,'General_classifiaction.plk')
    return predicted_svm


# In[3]:


def GAD(data):
    #df=pd.read_csv(r'')
    #X=df.Questions
    #y = df.type
    #text_clf_svm = Pipeline([('vect', CountVectorizer()),
     #                     ('tfidf', TfidfTransformer()),
      #                    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
       #                                     alpha=1e-3, n_iter=5, random_state=42)),
    #])

    #text_clf_svm.fit(X,y)
    #predicted_svm = text_clf_svm.predict(data)
    #return predicted_svm
    return 


# In[4]:


def emotional_change(data):
    #df=pd.read_csv(r'')
    #X=df.Questions
    #y = df.type
    #text_clf_svm = Pipeline([('vect', CountVectorizer()),
     #                     ('tfidf', TfidfTransformer()),
      #                    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
       #                                     alpha=1e-3, n_iter=5, random_state=42)),
    #])

    #text_clf_svm.fit(X,y)
    #predicted_svm = text_clf_svm.predict(data)
    #return predicted_svm
    return ""


# In[5]:


def physical_change(data):
    #df=pd.read_csv(r'')
    #X=df.Questions
    #y = df.type
    #text_clf_svm = Pipeline([('vect', CountVectorizer()),
     #                     ('tfidf', TfidfTransformer()),
      #                    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
       #                                     alpha=1e-3, n_iter=5, random_state=42)),
    #])

    #text_clf_svm.fit(X,y)
    #predicted_svm = text_clf_svm.predict(data)
    #return predicted_svm
    return ""


# In[6]:


def social_change(data):
    #df=pd.read_csv(r'')
    #X=df.Questions
    #y = df.type
    #text_clf_svm = Pipeline([('vect', CountVectorizer()),
     #                     ('tfidf', TfidfTransformer()),
      #                    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
       #                                     alpha=1e-3, n_iter=5, random_state=42)),
    #])

    #text_clf_svm.fit(X,y)
    #predicted_svm = text_clf_svm.predict(data)
    #return predicted_svm
    return ""


# In[ ]:





# In[7]:


def sleep_disturbances(data):
    #df=pd.read_csv(r'')
    #X=df.Questions
    #y = df.type
    #text_clf_svm = Pipeline([('vect', CountVectorizer()),
     #                     ('tfidf', TfidfTransformer()),
      #                    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
       #                                     alpha=1e-3, n_iter=5, random_state=42)),
    #])

    #text_clf_svm.fit(X,y)
    #predicted_svm = text_clf_svm.predict(data)
    #return predicted_svm
    return ""


# In[8]:


def poor_school_performance(data):
    #df=pd.read_csv(r'')
    #X=df.Questions
    #y = df.type
    #text_clf_svm = Pipeline([('vect', CountVectorizer()),
     #                     ('tfidf', TfidfTransformer()),
      #                    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
       #                                     alpha=1e-3, n_iter=5, random_state=42)),
    #])

    #text_clf_svm.fit(X,y)
    #predicted_svm = text_clf_svm.predict(data)
    #return predicted_svm
    return ""


# In[9]:


def panic_attack(data):
    #df=pd.read_csv(r'')
    #X=df.Questions
    #y = df.type
    #text_clf_svm = Pipeline([('vect', CountVectorizer()),
     #                     ('tfidf', TfidfTransformer()),
      #                    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
       #                                     alpha=1e-3, n_iter=5, random_state=42)),
    #])

    #text_clf_svm.fit(X,y)
    #predicted_svm = text_clf_svm.predict(data)
    #return predicted_svm
    return ""

