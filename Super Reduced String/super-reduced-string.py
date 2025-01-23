#!/bin/python3


import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    result =[]
    for i in range (len(s)):
      if len(result)==0 or result[-1] != s[i]:
        result.append(s[i])
      else:
        result.pop()
    
    
    if len(result) == 0:
      return "Empty String"
    else:
      return "".join(result)
    
      

if __name__ == '__main__':
    

    s = input()
    
    print(superReducedString(s)) 

