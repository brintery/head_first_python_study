# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:38:00 2018

@author: dell
"""


class Athlete:
    def __init__(self, name=None, dob=None, times=[]):
        self.name = name
        self.dob = dob
        self.times = times


    def sanitize(self, time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return time_string
        (mins, secs) = time_string.split(splitter)
        return(mins+'.'+secs)
    
    
    def get_coach_data(self, file_name):
        try:
            with open(file_name) as f:
                data = f.readline().strip().split(',')
                self.name = data.pop(0)
                self.dob = data.pop(0)
                self.times = str(sorted([self.sanitize(line) for line in data])[0:3])
            return self
        except IOError as e:
            print('file error: ', str(e))
            return(None)

''' 
with open('james.txt') as jaf:
    james = jaf.readline().strip().split(',')

with open('julie.txt') as juf:
    julie = juf.readline().strip().split(',')
    
    
with open('mikey.txt') as mif:
    mikey = mif.readline().strip().split(',')
    
with open('sarah.txt') as saf:
    sarah = saf.readline().strip().split(',')

 
clean_james = [sanitize(line) for line in james]
clean_julie = [sanitize(line) for line in julie]
clean_mikey = [sanitize(line) for line in mikey]
clean_sarah = [sanitize(line) for line in sarah]



james = get_coach_data("james2.txt")
julie = get_coach_data("julie2.txt")
mikey = get_coach_data("mikey2.txt")
sarah = get_coach_data("sarah2.txt")
'''
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name, sarah_dob, sorted(set([sanitize(line) for line in sarah]))[0:3])

print(sorted(set([sanitize(line) for line in james]))[0:3])
print(sorted(set([sanitize(line) for line in julie]))[0:3])
print(sorted(set([sanitize(line) for line in mikey]))[0:3])
print(sorted(set([sanitize(line) for line in sarah]))[0:3])

james = Athlete().get_coach_data('james2.txt')
print(james.name, james.times)
