
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


from GAD_FUTURE_EVENTS import future
from GAD_PAST_BEHAVIOURS import past_behaviour
from GAD_PERONAL_ABILITIES import perosnal_abiities
from GAD_SOCIAL_ACCEPTANCE import social_acceptance
from GAD_POOR_PERFORMANCE import performance

from EMOTIONAL_CHANG_OUTBURST import outburst
from EMOTIONAL_CHANGE_DIFFICULTY_IN_CONCENTRATION import difficult_in_concentration
from EMOTIONAL_CHANGE_IRRITAIBILITY import Irritaibility
from EMOTIONAL_CHANGE_RESTLESSNESS import restlessness

from SOCIAL_AVOIDING_EA import avoiding_extracirricular
from SOCIAL_AVOIDING_FRIENDS import avoiding_friends
from SOCIAL_ISOLATION import isolation
from SOCIAL_SPENDING_TIME_ALONE import spending_increased_time_alone

from PHYSICAL_ACHES_MIGRAINS import aches_migrains
from PHYSICAL_EATING_HABIT import eating_habit
from PHYSICAL_FATIGUE import fatiguet
from PHYSICAL_UNEXPLAINED_ACHES import fatiguet

from SLEEP_DISTURBANCES_DIFFICULTY_SLEEPING import difficulty_falling_asleep
from SLEEP_DISTURBANCES_NIGHTMARES import nightmares
from SLEEP_DISTURBANCES_NOT_FRESH import not_freshed
from SLEEP_DISTURBANCES_STAYING_SLEEPING import difficulty_staying_asleep



# In[4]:


#this function gives domain i.e 7 sub categories including gad,emotional,physical,social,etc
def check_general_classification(X):
    with open('general_classification.pkl', 'rb') as file:  
        general_classification = pickle.load(file)
    return general_classification.predict(pd.Series(X))
#fuctions below this line will give sub domains on the basis of class predicted by check_general_classification
def gad(X):
    with open('GAD.pkl', 'rb') as file:  
        gad = pickle.load(file)
        return gad.predict(pd.Series(X))
def emotional_change(X):
    with open('emotional_change.pkl', 'rb') as file:  
        emotional_change = pickle.load(file)
    return emotional_change.predict(pd.Series(X))
def panik_attack(X):
    with open('panic attack.pkl', 'rb') as file:  
        panik_attack = pickle.load(file)
    return panik_attack.predict(pd.Series(X))
def poor_performance(X):
    with open('poor_performance.pkl', 'rb') as file:  
        poor_performance = pickle.load(file)
    return poor_performance.predict(pd.Series(X))
def sleep_disturbances(X):
    with open('sleep_disturbances.pkl', 'rb') as file:  
        sleep_disturbances = pickle.load(file)
    return sleep_disturbances.predict(pd.Series(X))
def social_change(X):
    with open('social_change.pkl', 'rb') as file:  
        social_change = pickle.load(file)
    return social_change.predict(pd.Series(X))
def physical_change(X):
    with open('physical_change.pkl', 'rb') as file:  
        physical_change = pickle.load(file)
    return physical_change.predict(pd.Series(X))
def happy_side(X):
    with open('happy_sad.pkl', 'rb') as file:  
        happy_sad = pickle.load(file)
    return happy_sad.predict(pd.Series(X))

        


# In[3]:


def solution(X):
    while True:
            pred_class=check_general_classification(X)
            if pred_class=="Generalized Anxiety Disorder":

                        sub_domain=gad(X)
                        if sub_domain=='Future Events':
                            a=future('future')
                            return a
                        if sub_domain=='past behaviour and incident':
                            a=past_behaviour('past')
                            return a
                            
                        if sub_domain=='Social acceptance':
                            a=social_acceptance('thinking too much')
                            return a
                        if sub_domain=='Performance':
                            a=poor_performance('give your best')
                            return a
                        if sub_domain=='Personal abilities':
                            a=perosnal_abiities('Self doubt will eat your confidence away')
                            return a
            if pred_class=="Emotional Change":
                    sub_domain=emotional_change(X)
                    if sub_domain=='Difficulty concentrating':
                        a=difficult_in_concentration('focussing')
                        return a
                        
                    if sub_domain=='Irritability':
                        a=Irritaibility('frustated')
                        return a    
                    if sub_domain=='Restlessness':
                        a=restlessness('bothering')
                        return a
                    if sub_domain=='Unexplained outbursts':
                        a=restlessness('feelings')
                        return a
            if pred_class=="Social changes":
                sub_domain=social_change(X)
                if sub_domain=='Avoiding extracurricular activities':
                    a=avoiding_extracirricular('anxiety')
                    return a
                if sub_domain=='Avoiding interactions with friends':
                    a=avoiding_friends('overthink')
                    return a
                if sub_domain=='Isolating from peer group':
                            
                    a=isolation('overthink')
                    return a
                if sub_domain=='spending increased time alone':
                            
                    a=spending_increased_time_alone('people')
                    return a
            if pred_class=="Physical":
                sub_domain=physical_change(X)
                   
                if sub_domain=='changing in eating habits':
                        a=eating_habit('zone')
                        return (a)
                if sub_domain=='excessive fatique':

                        a=fatiguet('overworried')
                        return a
                if sub_domain=='frequent headaches migranes':

                        a=aches_migrains('emotionally')
                        return a
                if sub_domain=='unexplained aches and pains':
                        a=fatiguet('overworried')
                        return a
            if pred_class=="Sleep Disturbances":
                sub_domain=sleep_disturbance(X)
                if sub_domain=='difficulty falling asleep':
                                                            
                    a=difficulty_falling_asleep('contributes')
                    return a
                                
                if sub_domain=='difficulty staying asleep':
                    a=difficulty_staying_asleep('minds')
                    return a
                if sub_domain=='frequently nightmares':

                    a=nightmares('essentially')
                    return a
                if sub_domain=='not feeling refreshed after sleep':

                    a=not_freshed('cycle')
                    return a



