
# coding: utf-8

# In[1]:


import nltk
from random import randint
import numpy as np
import random

import string
import pickle
import pandas as pd
import sys

import nltk
import numpy as np
import random
import string # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[3]:


def import_future(X):
    from GAD_FUTURE_EVENTS import future
    return future(X)

