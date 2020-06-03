# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:13:06 2020

@author: nitin
"""

#%%
nlis=[0,1,2,3,4,5,6,7,8]
#%%
def board():
    print("\t\t\tTIC TAC TOE\n\n")
    print("\t      |     |     ")
    print("\t  ",nlis[0]," | ",nlis[1]," | ",nlis[2]," ")
    print("\t _____|_____|_____")
    print("\t      |     |     ")
    print("\t  ",nlis[3]," | ",nlis[4]," | ",nlis[5]," ")
    print("\t _____|_____|_____")
    print("\t      |     |     ")
    print("\t  ",nlis[6]," | ",nlis[7]," | ",nlis[8]," ")
    print("\t      |     |     ")
#%%
def decision():
    if nlis[0]==nlis[1] and nlis[1]==nlis[2]:
        return 1
    elif nlis[3]==nlis[4] and nlis[4]==nlis[5]:
        return 1
    elif nlis[6]==nlis[7] and nlis[7]==nlis[8]:
        return 1
    elif nlis[0]==nlis[3] and nlis[3]==nlis[6]:
        return 1
    elif nlis[1]==nlis[4] and nlis[4]==nlis[7]:
        return 1
    elif nlis[2]==nlis[5] and nlis[5]==nlis[8]:
        return 1
    elif nlis[0]==nlis[4] and nlis[4]==nlis[8]:
        return 1
    elif nlis[2]==nlis[4] and nlis[4]==nlis[6]:
        return 1
    elif nlis[0]!=0 and nlis[1]!=1 and nlis[2]!=2 and nlis[3]!=3 and nlis[4]!=4 and nlis[5]!=5 and nlis[6]!=6 and nlis[7]!=7 and nlis[8]!=8:
        return 0
    else:
        return -1
#%%
def game():
    player=1
    result=-1
    count=0
    while result==-1:
        board()
        player= 1 if count%2==0 else 2
        symbol='X' if player==1 else 'O'
        print("PLAYER",player,"==>")
        choice=int(input("Enter box number: "))
        if choice==0 and nlis[0]==0:
            nlis[0]=symbol
        elif choice==1 and nlis[1]==1:
            nlis[1]=symbol
        elif choice==2 and nlis[2]==2:
            nlis[2]=symbol
        elif choice==3 and nlis[3]==3:
            nlis[3]=symbol
        elif choice==4 and nlis[4]==4:
            nlis[4]=symbol
        elif choice==5 and nlis[5]==5:
            nlis[5]=symbol
        elif choice==6 and nlis[6]==6:
            nlis[6]=symbol
        elif choice==7 and nlis[7]==7:
            nlis[7]=symbol
            
        elif choice==8 and nlis[8]==8:
            nlis[8]=symbol
        elif choice==9 and nlis[9]==9:
            nlis[9]=symbol
        else:
            print("Wrong choice!!")
        result= decision()
        count=count+1
    print("RESULT==>:)")
    if result==1:
        print("PLAYER",player,"WON!!")
    else:
        print("GAME DRAW!!")
#%%
def main():
    game()
        
    
    
    
    
    
    
    
    
    
    