# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:50:02 2019

@author: Ayush Garg
"""

import string

dict={}
data=""
file=open("op_file.txt","w")

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
    
print(dict)    
    
with open("ip_file.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("END OF FILE!!")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        #print(data)
        
print("OPEN FILE TO SEE MESSAGE")  
file.close()      