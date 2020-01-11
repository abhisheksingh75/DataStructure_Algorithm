#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    DP = [[False for col in range(len(a)+1)]for row in range(len(b)+1)]
    DP[0][0]  =  True 
    for i in range(len(DP[0])-1):
        if a[i].islower() ==  True:
            DP[0][i+1] = True
        else:
            break

    for b_pos in range(1,len(DP)):
        for a_pos in range(1, len(DP[0])):
            if DP[b_pos-1][a_pos-1] == True:
                if a[a_pos-1] == b[b_pos-1] or chr(ord(a[a_pos-1])-32) == b[b_pos-1]:
                    DP[b_pos][a_pos] = DP[b_pos-1][a_pos-1]
                elif a[a_pos-1].islower() == True:
                    DP[b_pos][a_pos] = DP[b_pos][a_pos-1]
            elif a[a_pos-1].islower() == True:
                    DP[b_pos][a_pos] = DP[b_pos][a_pos-1]
    #print(DP)               
    if DP[len(DP)-1][len(DP[0])-1] == True:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        #fptr.write(result + '\n')
        print("\n"+result)
        

    #fptr.close()
