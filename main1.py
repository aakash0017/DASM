
# coding: utf-8

# In[1]:


import nltk
from random import randint
import numpy as np
import random
import string
import pickle
import pandas as pd


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def __init__(self):
    self.name=name
def returnname(self):
    self.name = request.form['name']

    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)


