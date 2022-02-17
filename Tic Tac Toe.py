
#tic tac toe

def choose():
    global x
    global p1
    global p2
    
    while p1 not in ['X','O']:
        
        p1=input("PLayer 1 enter your symbol (X or O)").upper()
    
    
    if p1=='X':
        p2='O'
        x='X'
        
    else:
        p2='X'
        x='O'
        
def display():
    
    # from IPython.display import clear_output
    # clear_output()
    import os
    os.system('cls')
    
    print('\n'+r[1]+'  |  '+r[2]+'  |  '+r[3])
    print('-------------')
    print(r[4]+'  |  '+r[5]+'  |  '+r[6])
    print('-------------')
    print(r[7]+'  |  '+r[8]+'  |  '+r[9])
    

def game(r):
    global x
    global y
    
    y=0
    available=[1,2,3,4,5,6,7,8,9]
    
    while win==False and y!=9:
        
        position=0
       
        if x==p1:
            while position not in available:
                position=int(input('\nPlayer 1 enter position (1-9)'))
            
            available[position-1]='0'
            r[position]=p1
            display()
            check()
            x=p2
            y+=1
        
        else:
            while position not in available:
                position=int(input('\nPlayer 2 enter position (1-9)'))
            
            available[position-1]='0'
            r[position]=p2
            display()
            check()
            x=p1
            y+=1
            
            
def check():
    global win
    if r[1]==x and r[2]==x and r[3]==x :
        win=True
    elif r[4]==x and r[5]==x and r[6]==x :
        win=True
    elif r[7]==x and r[8]==x and r[9]==x :
        win=True
    elif r[1]==x and r[4]==x and r[7]==x :
        win=True
    elif r[2]==x and r[5]==x and r[8]==x :
        win=True
    elif r[3]==x and r[6]==x and r[9]==x :
        win=True
    elif r[1]==x and r[5]==x and r[9]==x :
        win=True
    elif r[3]==x and r[5]==x and r[7]==x :
        win=True
    else:
        pass
    
    
def winner():
    
    if(win==False and y==9):
        print('\n\nTie Game !!!')
    elif x==p2:
        print('\nPlayer 1 Wins!!!')
    else:
        print('\nPlayer 2 Wins!!!')


play='Y'
x=' '
p1=' '
p2=' '


while play=='Y':
    global win
    global r
    
    win=False
    r=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    
    print('\nWelcome to tic tac toe')
    choose()
    display()
    game(r)
    winner()
    play=input('\n\nWant to play again? (Y/N)')
    play=play.upper()
    
print('\n\nThank you for playing !')

    

