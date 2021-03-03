#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(raw_input())
    
    nameList = []
    
    for N_itr in xrange(N):
        firstNameEmailID = raw_input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if(emailID.split('@')[1] == 'gmail.com'):
            nameList.append(firstName)
            
    nameList = sorted(nameList)
    
    for name in nameList:
        print(name)
