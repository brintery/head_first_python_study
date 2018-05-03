# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:27:16 2018

@author: dell

athletelist
"""

class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)
    
    @property    
    def top3(self):
        return(sorted([sanitize(line) for line in self])[0:3])



def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return(mins+'.'+secs)

'''
def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline().strip().split(',')
        return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as e:
        print('file error: ', str(e))
        return(None)


james = get_coach_data('james2.txt')
print(james.top3())
'''