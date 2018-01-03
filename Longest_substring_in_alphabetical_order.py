# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:50:49 2017
@author: Gavrilov
"""
s = 'azcbobobegghakl'
counter = 0 #counter
length = 0 #length
end = 0 #end

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        counter += 1 #all below is to form var on length
        if counter > length: #to establish length
            length = counter
            end = i + 1
    else:
        counter = 0 
begin = end - length
print('Longest substring in alphabetical order is: ', s[begin:end + 1])
