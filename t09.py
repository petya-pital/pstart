# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:12:25 2018

@author: Петя
"""
#s = ['9','9','9']
#list(map(float,s))
#print(s)
#print(float(s))
dstf = list(map(float,input('print your stuff there\n').split(',')))
print(dstf)
#for t in dstf :
#    float(t)
#print(dstf)
    
    
print('style nigers: %i /%i/ %i'%(tuple(dstf) ))