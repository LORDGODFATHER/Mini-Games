# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 00:39:49 2019

@author: Ayush Garg
"""

def magic_square(n):
    magicsquare=[]
    for i in range(n):
        list=[]
        for j in range(n):
            list.append(0)
        magicsquare.append(list)

    i=n//2
    j=n-1
    num=1
    
    while(num<=n*n):     
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(j==n):
                j=0
            if(i==-1):
                i=n-1
                
        if(magicsquare[i][j]!=0):
            i=i+1
            j=j-2
            continue
        else:
            magicsquare[i][j]=num
            num=num+1
            
        i=i-1
        j=j+1
    
    print("THE SUM OF EACH ROW/COLUMN/DIAGONAL IS : "+str(n*(n**2 + 1)//2))
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end=" ")
        print()

print("ENTER SIZE OF MAGIC SQUARE = ",end="")
n=int(input())        
magic_square(n)        