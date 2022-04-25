# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:09:09 2022

@author: jaipa
"""

from sequence_cleaner import sequence_cleaner
a=input('filepath:')
b=int(input('how short is too short: '))
c=int(input('% of unkown nucleotides allowed: '))
sequence_cleaner(a,b,c)