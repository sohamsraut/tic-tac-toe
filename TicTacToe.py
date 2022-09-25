#TicTacToe
import random
print('Welcome to Tic Tac Toe!!')
print('In this game you place X and computer places 0')
print('You win when X occupies 3 consecutive places')
print('Computer wins when 0 occupies 3 consecutive places')
print('Here we go!\n')
key={1:'   ',2:'   ',3:'   ',4:'   ',5:'   ',6:'   ',7:'   ',8:'   ',9:'   '}
l=[1,2,3,4,5,6,7,8,9]
#Board for the game
def board():
    print(key[7],key[8],key[9],sep='|')
    print('-+-+-')
    print(key[4],key[5],key[6],sep='|')
    print('-+-+-')
    print(key[1],key[2],key[3],sep='|')
print('Positions are given by:')
print('7|8|9')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('1|2|3')
win=lose=0
#Conditions for winning and losing
def winlosecheck():
    global win,lose
    if key[7]==key[8]==key[9]=='X' or key[4]==key[5]==key[6]=='X' or key[1]==key[2]==key[3]=='X':
        print('You have won!')
        win=1
    elif key[7]==key[5]==key[3]=='X' or key[9]==key[5]==key[1]=='X':
        print('You have won!')
        win=1
    elif key[7]==key[4]==key[1]=='X' or key[8]==key[5]==key[2]=='X' or key[9]==key[6]==key[3]=='X':
        print('You have won!')
        win=1
    elif key[7]==key[8]==key[9]=='0' or key[4]==key[5]==key[6]=='0' or key[1]==key[2]==key[3]=='0':
        print('Computer wins!\nGame over')
        lose=1
    elif key[7]==key[5]==key[3]=='0' or key[9]==key[5]==key[1]=='0':
        print('Computer wins!\nGame over')
        lose=1
    elif key[7]==key[4]==key[1]=='0' or key[8]==key[5]==key[2]=='0' or key[9]==key[6]==key[3]=='0':
        print('Computer wins!\nGame over')
        lose=1
while True:
    if win==1 or lose==1:
        break
    user=int(input('\nEnter position to put X: '))
    if user not in key:
        print('Invalid position try again')
        continue
    elif key[user]=='   ':
        key[user]='X'
        l.remove(user)
        board()
        winlosecheck()
        if l !=[]:
            comp=random.randint(1,9)
            while comp not in l:
                comp=random.randint(1,9)
            else:
                l.remove(comp)
        elif l==[] and win!=1 and lose!=1:
            print('Tie!')
            break
        if win!=1:
            print('\nComputer plays:')
            key[comp]='0'
            board()
            winlosecheck()
    elif key[user]!='   ':
        print('Invalid position try again')
        
            

                

        
        

