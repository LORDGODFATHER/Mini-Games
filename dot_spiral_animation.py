# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:41:23 2019

@author: Ayush Garg
"""

from random import randint
import turtle

turtle.bgcolor("black")
tur=turtle.Turtle()

dot_distance=25
tur.penup()
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]
tur.setpos(-250,250)

def spiral(m,n):
    row=0
    col=0
    flag=0
    clr=randint(0,10)
    tur.color(list_color[clr])
    
    while(row<m and col<n):
        if(flag==1):
            tur.right(90)
        #printing firt row from remaining rows
        for i in range(col,n):
            tur.dot()
            tur.forward(dot_distance)
        row=row+1
        flag=1
        tur.right(90)
        
        #printing last column from remaining columns
        clr=randint(0,10)
        tur.color(list_color[clr])
        for i in range(row,m):
            tur.dot()
            tur.forward(dot_distance)
        n=n-1
        tur.right(90)
        
        #printing last row from remaining rows
        clr=randint(0,10)
        tur.color(list_color[clr])
        if(row<m):
            for i in range(n-1,col-1,-1):
                tur.dot()
                tur.forward(dot_distance)
            m=m-1
            tur.right(90)
 
        #printing first column from remaining columns
        clr=randint(0,10)
        tur.color(list_color[clr])
        if(col<n):
            for i in range(m-1,row-1,-1):
                tur.dot()
                tur.forward(dot_distance)
            col=col+1
            
spiral(20,20)
turtle.done()            