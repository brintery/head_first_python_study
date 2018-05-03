# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:34:08 2018

@author: dell

athletemodel
"""


import pickle
from athletelist import AthleteList
from athletelist import sanitize


def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline().strip().split(',')
        return AthleteList(data.pop(0), data.pop(0), [sanitize(each_data) for each_data in data])
    except IOError as e:
        print('file error: ', str(e))
        return(None)


def put_to_store(file_list):
    all_athletes = {}
    for file in file_list:
        ath = get_coach_data(file)
        all_athletes[ath.name] = ath
    
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as e:
        print("file error (put_to_store): ", str(e))
        
    return(all_athletes)


def get_from_store():
    all_athletes = {}
    
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as e:
        print("file error (get_from_store): ", str(e))
    
    return(all_athletes)


