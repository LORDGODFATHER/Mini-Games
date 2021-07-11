# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:20:34 2019

@author: Ayush Garg
"""

import numpy

board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1symbol='X'
p2symbol='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if(board[r][c]==symbol):
                count=count+1
        if(count==3):
            print(symbol,' WON')
            return True
    return False

def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if(board[r][c]==symbol):
                count=count+1
        if(count==3):
            print(symbol,' WON')
            return True
    return False

def check_diagonals(symbol):
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol):
        print(symbol,' WON')
        return True
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol):
        print(symbol,' WON')
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input('ENTER ROW(1 OR 2 OR 3):'))
        col=int(input('ENTER COLUMN(1 OR 2 OR 3):'))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='_'):
            break
        else:
            print('INVALID INPUT!.PLEASE ENTER AGAIN')
    board[row-1][col-1]=symbol        

def play():
    for turn in range(9):
        if(turn%2==0):
            print('X TURN')
            place(p1symbol)
            if won(p1symbol):
                break
        else:
            print('O TURN')
            place(p2symbol)
            if won(p2symbol):
                break
    if(not(won(p1symbol)) and not(won(p2symbol))):
        print('DRAW!!')
        
play()                  