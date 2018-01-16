# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:25:22 2018

@author: Gavrilov
"""

scores = [3.0, 1.0, 0.2]

import math

exp = [math.exp(i) for i in scores] 
#https://docs.python.org/3/library/math.html#math.exp

exp_sum = sum(exp)
softmax = [i/exp_sum for i in scores]
print(softmax)