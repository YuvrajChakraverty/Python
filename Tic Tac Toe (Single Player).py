from datetime import datetime
import random
import os

# Choosing the Symbol

def choose():
    
    global pl,cp,hard,diff
    
    while hard not in ['E','H']: 
        display_grid()
        hard=input("\nSelect Difficulty Level (E or H):  ").upper()
    diff=hard

    while pl not in ['X','O']: 
        display_grid()
        pl=input("\nEnter your Preferred Symbol (X or O):  ").upper()
      
    if pl=='X':
        cp='O'    
    else:
        cp='X'
    
    
    begin=None
    while begin not in ['Y','N']:
        display_grid()
        begin=input('\nWould You Like to go First? (Y/N): ').upper()
    
    if(begin=='Y'):
        player()
    else:
        computer()
    


#  display the Grid       
        
def display_grid():
    
    os.system('cls')
    
    print('\n')
            
    for i in range(3):
        print(' '+r[i][0]+' |  '+r[i][1]+'  | '+r[i][2])
        if(i<2):
            print('-------------')
            
    if(cp_pos!=0):
        print('\n\nThe Computer Played at: '+ str(cp_pos))
            
    
    
# Player's turn

def player():
    
    global r,vacant,cp_pos,first,second,hard,game,session
    
    display_grid()
    
    if vacant==0:
        cp_pos=0
        display_grid()
        print("\nTie Game!")
        print('\nGame Summary: '+game)
        if(diff=='E'):
            session[0][3]+=1
        else:
            session[1][3]+=1
        
    else:
        if vacant>1:  
            pl_input=None
            available_str=[str(n) for n in available]
        
            while pl_input not in available_str:
                display_grid()
                pl_input=input('\nEnter Position (1-9):  ')

            game=game+'You: '+pl_input+'; '

            if(vacant<6):
                hard='E'
            
            if(hard=='H'):
                if((vacant==9) and pl_input=='5'):
                    first='5'
                elif((vacant==9) and (pl_input in ['1','3','7','9'])):
                    first=pl_input
                elif((vacant==7) and (first!=None) and (first!='5')):
                    if(((first in ['1','9']) and (pl_input in ['1','9'])) or ((first in ['3','7']) and (pl_input in ['3','7']))):
                        second=pl_input
                else:
                    pass
                
        else:
            pl_input=available[0]
            game=game+'You: '+str(pl_input)+'; '
            
        pl_input=int(pl_input)
            
        cp_pos=0
            
        i=int((pl_input-1)/3)
        j=(pl_input%3)-1
        if(j==-1):
            j=2
        r[i][j]=pl
        
        vacant-=1
        available.remove(pl_input)
                
        check('p')
        
        
# Computer's turn        

def computer():
    
    global r,vacant,cp_pos,game,session
    
    a=None
    b=None
    prevent=set()
    favorable=set()
    determined=False
    
    if vacant==0:
        cp_pos=0
        display_grid()
        print("\nTie Game!")
        print('\nGame Summary: '+game)
        if(diff=='E'):
            session[0][3]+=1
        else:
            session[1][3]+=1
    else:
        x=[[' ']*3 for i in range(8)]
        
        for i in range(3):
            for j in range(3):
                x[i][j]=r[i][j]
                x[j+3][i]=r[i][j]
                if(i==j):
                    x[6][j]=r[i][j]
                if((i+j)==2):
                    x[7][i]=r[i][j]
                    
        for i in range(8):
            
            if(' ' in x[i]):
                if(x[i].count(cp)==2):
                    ind=x[i].index(' ')
                    if(i<3):
                        a=i
                        b=ind
                    elif(i<6):
                        a=ind
                        b=i-3
                    elif(i==6):
                        a=ind
                        b=ind
                    else:
                        a=ind
                        b=2-ind
                    determined=True
                    break
                    
                elif(x[i].count(pl)==2):
                    ind=x[i].index(' ')
                    if(i<3):
                        prevent.add((i*3)+ind+1)
                    elif(i<6):
                        prevent.add((ind*3)+(i-3)+1)
                    elif(i==6):
                        prevent.add((ind*3)+ind+1)
                    else:
                        prevent.add((ind*3)+(2-ind)+1)
                    
                elif((x[i].count(' ')==2) and (cp in x[i])):
                    ind=[0,0]
                    k=0
                    for j in range(3):
                        if(x[i][j]==' '):
                            ind[k]=j
                            k+=1
                    if(i<3):
                        favorable.add(ind[0]+(3*i)+1)
                        favorable.add(ind[1]+(3*i)+1)
                    elif(i<6):
                        favorable.add((ind[0]*3)+(i-3)+1)
                        favorable.add((ind[1]*3)+(i-3)+1)
                    elif(i==6):
                        favorable.add((ind[0]*3)+ind[0]+1)
                        favorable.add((ind[1]*3)+ind[1]+1)
                    else:
                        favorable.add((ind[0]*3)+(2-ind[0])+1)
                        favorable.add((ind[1]*3)+(2-ind[1])+1)
                
                else:
                    pass
                
        
        chosen=None
        
        prevent=list(prevent)
        favorable=list(favorable)
        
        if(determined==False):
            if(len(prevent)>0):
                random.seed(datetime.now())
                chosen=random.choice(prevent)
            elif(len(favorable)>0):
                if(hard=='H'):
                    if((vacant==6) and (second!=None)):
                        random.seed(datetime.now())
                        chosen=random.choice([2,4,6,8])
                    else:
                        random.seed(datetime.now())
                        chosen=random.choice(favorable)
                else:
                    random.seed(datetime.now())
                    chosen=random.choice(favorable)
            else:
                if(hard=='H'):
                    if(vacant==9):
                        chosen=5
                    elif((vacant==8) and first=='5'):
                        random.seed(datetime.now())
                        chosen=random.choice([1,3,7,9])
                    elif((vacant==8) and (5 in available)):
                        chosen=5
                    else:
                        random.seed(datetime.now())
                        chosen=random.choice(available)
                        
                else:
                    random.seed(datetime.now())
                    chosen=random.choice(available)
                
            a=int((chosen-1)/3)
            b=(chosen%3)-1
            if(b==-1):
                b=2
                
        else:
            chosen=(a*3)+b+1

        game=game+'Comp: '+str(chosen)+'; '       
                
        r[a][b]=cp
        
        vacant-=1
        available.remove(chosen)
        cp_pos=chosen
                        
        check('c')

        
# Checking for win

def check(turn):
    
    global over,session
    
    symbol=None
    x=[[' ']*3 for i in range(4)]
    
    if(turn=='p'):
        symbol=pl
    else:
        symbol=cp
        
    for i in range(3):
        
        for j in range(3):

            x[0][j]=r[i][j]
            x[1][j]=r[j][i]
            if(i==j):
                x[2][i]=r[i][i]
            if((i+j)==2):
                x[3][i]=r[i][j]
            
        for i in range(0,4):
            k=[' ',' ',' ']
            for j in range(0,3):
                k[j]=x[i][j]
            if(k[0]==k[1]==k[2]==symbol):
                over=True
                break
    
            
    if(over):
        display_grid()
        
        if(turn=='p'):
            print('\n\nCongratulations, You Won!!!')
            if(diff=='E'):
                session[0][1]+=1
            else:
                session[1][1]+=1
        else:
            print('\n\nComputer Wins!!!\n\nBetter Luck Next Time.')
            if(diff=='E'):
                session[0][2]+=1
            else:
                session[1][2]+=1

        print('\nGame Summary: '+game)
        
    else:
        if(turn=='p'):
            computer()
        else:
            player()
            
            

# Start            

play='Y'
pl=None
cp=None
first=None
second=None
cp_pos=0
vacant=9
available= [*range(1,10)]
over=False
hard=None
diff=None
game=''
session=[ [0]*4 for i in range(2)]
r=[ [' ']*3 for i in range(3)]
    
print('\nWelcome to Tic Tac Toe')

while(play=='Y'):
    
    display_grid()
    
    pl=None
    cp=None
    first=None
    second=None
    cp_pos=0
    vacant=9
    available= [*range(1,10)]
    over=False
    hard=None
    diff=None
    game=''
    r=[ [' ']*3 for i in range(3)]
    
    choose()
    if(diff=='E'):
        session[0][0]+=1
    else:
        session[1][0]+=1

    play=input('\n\nWant to Play Again? (Y/N): ').upper()
    
os.system('cls')
print('\n\nSession Summary:\n')
print('\nEasy:   Played: '+str(session[0][0])+'; '+'Won: '+str(session[0][1])+'; '+'Lost: '+str(session[0][2])+'; '+'Tie: '+str(session[0][3]))
print('\nHard:   Played: '+str(session[1][0])+'; '+'Won: '+str(session[1][1])+'; '+'Lost: '+str(session[1][2])+'; '+'Tie: '+str(session[1][3]))
print('\nTotal:  Played: '+str(session[0][0]+session[1][0])+'; '+'Won: '+str(session[0][1]+session[1][1])+'; '+'Lost: '+str(session[0][2]+session[1][2])+'; '+'Tie: '+str(session[0][3]+session[1][3]))
print('\n\nThank you for Playing !\n')