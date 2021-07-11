# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:19:57 2019

@author: Ayush Garg
"""

import random

movies=['dangal','pk','dhadak','secret superstar','jungle book','roy','raid','bahubali']


def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if(letters[i]==' '):
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if(c==0):
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if(ref[i]==' ' or ref[i]==letter):
            temp.append(ref[i])
        else:
            if(qn_list[i]=='*'):
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new   

def play():
    p1name=input('PLAYER1! PLEASE ENTER YOUR NAME : ')
    p2name=input('PLAYER2! PLEASE ENTER YOUR NAME : ')
    pp1=0
    pp2=0
    turn=0
    willing=True
    while(willing):
        if(turn%2==0):
            #PLAYER1
            print(p1name,' YOUR TURN ')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while(not_said):
                letter=input('YOUR LETTER : ')
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    decision=input('PRESS 1 TO GUESS THE MOVIE OR 0 TO UNLOCK ANOTHER LETTER : ')
                    if(decision==1):
                        ans=input('YOUR ANSWER : ')
                        if(ans==picked_movie):
                            pp1=pp1+1
                            print('CORRECT')
                            not_said=False
                            print(p1name,' YOUR SCORE : ',pp1)
                        else:
                            print('WRONG ANSWER.TRY AGAIN.')
                else:
                    print(letter,' NOT FOUND ')
            choice=input('PRESS 1 TO CONTINUE OR 0 TO QUIT : ')
            if(choice==0):
                print(p1name,' YOUR SCORE : ',pp1)
                print(p2name,' YOUR SCORE : ',pp2)
                print('THANKS FOR PLAYING')
                print('HAVE A NICE DAY.')
                willing=False
        else:
            #PLAYER2
            print(p2name,' YOUR TURN ')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while(not_said):
                letter=input('YOUR LETTER : ')
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    decision=input('PRESS 1 TO GUESS THE MOVIE OR 0 TO UNLOCK ANOTHER LETTER : ')
                    if(decision==1):
                        ans=input('YOUR ANSWER : ')
                        if(ans==picked_movie):
                            pp2=pp2+1
                            print('CORRECT')
                            not_said=False
                            print(p2name,' YOUR SCORE : ',pp2)
                        else:
                            print('WRONG ANSWER.TRY AGAIN.')
                else:
                    print(letter,' NOT FOUND ')
            choice=input('PRESS 1 TO CONTINUE OR 0 TO QUIT : ')
            if(choice==0):
                print(p1name,' YOUR SCORE : ',pp1)
                print(p2name,' YOUR SCORE : ',pp2)
                print('THANKS FOR PLAYING')
                print('HAVE A NICE DAY.')
                willing=False
        turn=turn+1                        
    
play()    
