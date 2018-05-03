# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:20:09 2018

@author: dell

model_test
"""

def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='')
            print(each_item)