# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 19:32:48 2017
@author: Gavrilov
"""

def abstract(x, numberEdit):
    """
    x is a number of symbols in dissertation
    recursion base is a max of symbols for dissertation abstract
    recursion step is a average symbols eliminated per one edit
    return is a number of symbols, which would eliminated per specific numbers of edits
    """
    if x <= 60000:
        return print(x, numberEdit)
    else:
        return abstract(x-12000, numberEdit+1)
    
x = 173000
numberEdit = 0
abstract(x, numberEdit)
