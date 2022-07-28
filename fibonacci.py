# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 22:04:34 2022

@author: karan
"""

class fibonacci:
    ''' the iterable fibonacci creates fibonacci series'''
    def __init__(self,number):
        if not isinstance(number, int):
            raise ValueError
        self.number=number
        self.a=0
        self.b=1
        self.count=-1;
    def __iter__(self):
        '''returns the instane object whch is an iterator'''
        return self
    def __next__(self):
        '''defines the instance object as an itereator'''
        
        self.count+=1
        if self.count>self.number:
            raise StopIteration

        if self.count==1:
            return 1
        elif self.count==0:
            return 0
        elif self.count<0:
            raise StopIteration
        else:
            self.c=self.a+self.b
            self.a=self.b
            self.b=self.c
            return (self.c)
           