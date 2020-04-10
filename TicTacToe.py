import sys

 
def TicTacToe():
    '''Creates a game named Tic Tac Toe which 2 players can play'''
    
    numPad = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
    lineDisplay = {'Hori':'--','Vert':'|'}
    
    #Lets Player 1 choose a character to use
    player1_char = input('Player-1 choose your character: ')
    
    if player1_char in numPad.values():
        print('Character cannot be a number')
        TicTacToe()
        
    #Lets Player 2 choose a character to use
    player2_char = input('Player-2 choose your character: ')
    
    if player2_char in numPad.values():
        print('Character cannot be a number')
        TicTacToe()
    
    #Checks if the players are ready to play. If yes, proceeds with the game else exits the game
    readiness_input = input('Are you ready to play? ')
    
    if readiness_input.lower() == 'no':
        sys.exit('Bye!')
    elif readiness_input.lower() == 'yes':
        pass
    else:
        print('Wrong Input')
        TicTacToe()
    
    
    
    numPadDisplay(numPad,lineDisplay)
    
    player1_wins = 0
    player2_wins = 0
    num_times = 1
    curr_player  = 1
    taken_positions = {'Player_1':[],'Player_2':[]}
    pos_occupied = 0
    posValid = 0
    
    while player1_wins == 0 and player2_wins == 0 and num_times <= 9:
        if pos_occupied == 0:
            curr_position = input(f'Player {curr_player} enter your position: ')
        elif pos_occupied == 1:
            curr_position = input(f'Position {curr_position} is taken, enter another position: ')
        elif posValid == 0:
            curr_position = input(f'Position {curr_position} is invalid, enter another position: ')

        posValid = positionValidity(curr_position)
        
        if posValid == 1:
            pos_occupied = positionCheck(curr_position,taken_positions,curr_player)
            if pos_occupied == 1:
                continue
            else:
                winPlayer = checkWin(curr_player,taken_positions)
                if winPlayer == 1:
                    print(f'Player {curr_player} Wins')
                    print('Game Over!')
                    if curr_player == 1:
                        player1_wins = 1
                    else:
                        player2_wins = 1
                    formatNumPad(numPad,lineDisplay,taken_positions,player1_char,player2_char)
                    break
                else:
                    formatNumPad(numPad,lineDisplay,taken_positions,player1_char,player2_char)
                    if curr_player == 1:
                        curr_player = 2
                    elif curr_player == 2:
                        curr_player = 1
        else:
            continue
            
        num_times+=1
    
    if player1_wins == 0 and player2_wins == 0:
        sys.exit('Sorry!No one wins')

def formatNumPad(numPad,lineDisplay,taken_positions,player1_char,player2_char):
    for item in taken_positions.keys():
        for item1 in taken_positions[item]:
            if item == 'Player_1':
                numPad[item1] = player1_char
            elif item == 'Player_2':
                numPad[item1] = player2_char
    
    numPadDisplay(numPad,lineDisplay)
    
def numPadDisplay(n1,n2):
    nums = n1
    
    lines = n2
    
    print('      '+lines['Vert']+'      '+lines['Vert']+'      ')
    print('   '+nums['1']+'  '+lines['Vert']+'   '+nums['2']+'  '+lines['Vert']+'   '+nums['3']+'   ')
    print('      '+lines['Vert']+'      '+lines['Vert']+'      ')
    print(lines['Hori']*9)
    print('      '+lines['Vert']+'      '+lines['Vert']+'      ')
    print('   '+nums['4']+'  '+lines['Vert']+'   '+nums['5']+'  '+lines['Vert']+'   '+nums['6']+'   ')
    print('      '+lines['Vert']+'      '+lines['Vert']+'      ')
    print(lines['Hori']*9)
    print('      '+lines['Vert']+'      '+lines['Vert']+'      ')
    print('   '+nums['7']+'  '+lines['Vert']+'   '+nums['8']+'  '+lines['Vert']+'   '+nums['9']+'   ')
    print('      '+lines['Vert']+'      '+lines['Vert']+'      ')

def positionValidity(num):
    validPos = ['1','2','3','4','5','6','7','8','9']
    posValid = 0
    if num in validPos:
        posValid = 1
    
    return posValid

def positionCheck(num,taken_positions,curr_player):
    pos_list = []
    pos_occupied = 0
    for item in taken_positions.values():
        x=0
        while x < len(item):
            pos_list.append(item[x])
            x+=1
    
    pos_list.sort()
    
    if num in pos_list:
        pos_occupied = 1
    else:
        if curr_player == 1:
            taken_positions['Player_1'].append(num)
        else:
            taken_positions['Player_2'].append(num)
    
    return pos_occupied
            
def checkWin(curr_player,taken_positions):
    winPos = [['1','2','3'],['1','4','7'],['1','5','9'],['2','5','8'],['3','5','7'],['3','6','9'],['4','5','6'],['7','8','9']]
    winPlayer = 0
    
    for item in winPos:
        if sorted(list(set(sorted(taken_positions[f'Player_{curr_player}'])) & set(item))) == item:
            winPlayer = 1
    
    return winPlayer

if __name__ == '__main__':
    TicTacToe()