# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:51:45 2021

@author: Rakin Shahriar
"""

#h,m,s = map(int,input().split())

try:
    h,m,s = map(int,input().split())
    if(h<12 and h>0 and m<60 and s<60):
        print((12-h),":",(60-m),":",(60-s))
    elif(h==12):
        print(12,":",(60-m),":",(60-s))
    else:
        print("Sorry! Invalid input.")
except ValueError:
    print("Sorry! Input type not correct.")