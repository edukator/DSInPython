# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:59:59 2021

@author: user
"""

def  dene(arr):
     mid=len(arr)//2
     for idx in range(mid,len(arr)):
         arr[idx]=0
         
arr=[1,2,3,4,5,6,7]
dene(arr[4:])
print(arr)