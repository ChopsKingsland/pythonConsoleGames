from os import system, name
from sty import Style, RgbFg, fg, bg, ef, rs

tttArray = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
moves = 0
gameEnd = False
inputMove = ""
letter = ""
number = 0
abc = {"A": 0, "B": 1, "C": 2}
player = 1
winner = ""
fg.yellow = Style(RgbFg(255, 255, 0))
fg.green = Style(RgbFg(0, 255, 0))


def printBoard():
    print('  1 2 3')
    print('A ' + ' '.join(tttArray[0]))
    print('B ' + ' '.join(tttArray[1]))
    print('C ' + ' '.join(tttArray[2]))

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


while gameEnd == False:
    clear()
    printBoard()
    inputMove = input('Where would you like to play your turn? ')




    if inputMove[0].upper() == 'A' or inputMove[0].upper() == 'B' or inputMove[0].upper() == 'C':
        if inputMove[1] == '1' or inputMove[1] == '2' or inputMove[1] == '3':
            letter = inputMove[0].upper()
            number = int(inputMove[1]) - 1
            if tttArray[abc[letter]][number] == '-':
                if player == 1:
                    tttArray[abc[letter]][number] = fg.yellow + 'X' + fg.rs
                    player = 2
                elif player == 2:
                    tttArray[abc[letter]][number] = fg.green + 'O' + fg.rs
                    player = 1
            
    
    if tttArray[0][0] == 'X' and tttArray[1][0] == 'X' and tttArray[2][0] == 'X':
        winner = "X"
        gameEnd = True
    elif tttArray[0][1] == 'X' and tttArray[1][1] == 'X' and tttArray[2][1] == 'X':
        winner = "X"
        gameEnd = True
    elif tttArray[0][2] == 'X' and tttArray[1][2] == 'X' and tttArray[2][2] == 'X':
        winner = "X"
        gameEnd = True
    elif tttArray[0][0] == 'X' and tttArray[0][1] == 'X' and tttArray[0][2] == 'X':
        winner = "X"
        gameEnd = True
    elif tttArray[1][0] == 'X' and tttArray[1][1] == 'X' and tttArray[1][2] == 'X':
        winner = "X"
        gameEnd = True
    elif tttArray[2][0] == 'X' and tttArray[2][1] == 'X' and tttArray[2][2] == 'X':
        winner = "X"
        gameEnd = True
    elif tttArray[0][0] == 'X' and tttArray[1][1] == 'X' and tttArray[2][2] == 'X':
        winner = "X"
        gameEnd = True
    elif tttArray[0][2] == 'X' and tttArray[1][1] == 'X' and tttArray[2][0] == 'X':
        winner = "X"
        gameEnd = True

    if tttArray[0][0] == 'O' and tttArray[1][0] == 'O' and tttArray[2][0] == 'O':
        winner = "O"
        gameEnd = True
    elif tttArray[0][1] == 'O' and tttArray[1][1] == 'O' and tttArray[2][1] == 'O':
        winner = "O"
        gameEnd = True
    elif tttArray[0][2] == 'O' and tttArray[1][2] == 'O' and tttArray[2][2] == 'O':
        winner = "O"
        gameEnd = True
    elif tttArray[0][0] == 'O' and tttArray[0][1] == 'O' and tttArray[0][2] == 'O':
        winner = "O"
        gameEnd = True
    elif tttArray[1][0] == 'O' and tttArray[1][1] == 'O' and tttArray[1][2] == 'O':
        winner = "O"
        gameEnd = True
    elif tttArray[2][0] == 'O' and tttArray[2][1] == 'O' and tttArray[2][2] == 'O':
        winner = "O"
        gameEnd = True
    elif tttArray[0][0] == 'O' and tttArray[1][1] == 'O' and tttArray[2][2] == 'O':
        winner = "O"
        gameEnd = True
    elif tttArray[0][2] == 'O' and tttArray[1][1] == 'O' and tttArray[2][0] == 'O':
        winner = "O"
        gameEnd = True
    
    if "-" not in tttArray[0] and "-" not in tttArray[1] and "-" not in tttArray[2]:
        winner = "-"
        gameEnd = True

clear()       
printBoard()                
# print('end')
if winner == 'X':
    # print("Player X won")
    print("""
 _______   __                                                  __                        __                     
|       \\ |  \\                                               _/  \\                      |  \\                    
| $$$$$$$\\| $$  ______   __    __   ______    ______        |   $$         __   __   __  \\$$ _______    _______ 
| $$__/ $$| $$ |      \\ |  \\  |  \\ /      \\  /      \\        \\$$$$        |  \\ |  \\ |  \\|  \\|       \\  /       \\
| $$    $$| $$  \\$$$$$$\\| $$  | $$|  $$$$$$\\|  $$$$$$\\        | $$        | $$ | $$ | $$| $$| $$$$$$$\\|  $$$$$$$
| $$$$$$$ | $$ /      $$| $$  | $$| $$    $$| $$   \\$$        | $$        | $$ | $$ | $$| $$| $$  | $$ \\$$    \\ 
| $$      | $$|  $$$$$$$| $$__/ $$| $$$$$$$$| $$             _| $$_       | $$_/ $$_/ $$| $$| $$  | $$ _\\$$$$$$\\
| $$      | $$ \\$$    $$ \\$$    $$ \\$$     \\| $$            |   $$ \\       \\$$   $$   $$| $$| $$  | $$|       $$
 \\$$       \\$$  \\$$$$$$$ _\\$$$$$$$  \\$$$$$$$ \\$$             \\$$$$$$        \\$$$$$\\$$$$  \\$$ \\$$   \\$$ \\$$$$$$$ 
                        |  \\__| $$                                                                              
                         \\$$    $$                                                                              
                          \\$$$$$$                                                                               
    """)
elif winner == 'O':
    # print('Player O won')
    print("""
 _______   __                                                 ______                       __                     
|       \\ |  \\                                               /      \\                     |  \\                    
| $$$$$$$\\| $$  ______   __    __   ______    ______        |  $$$$$$\\       __   __   __  \\$$ _______    _______ 
| $$__/ $$| $$ |      \\ |  \\  |  \\ /      \\  /      \\        \\$$__| $$      |  \\ |  \\ |  \\|  \\|       \\  /       \\
| $$    $$| $$  \\$$$$$$\\| $$  | $$|  $$$$$$\\|  $$$$$$\\       /      $$      | $$ | $$ | $$| $$| $$$$$$$\\|  $$$$$$$
| $$$$$$$ | $$ /      $$| $$  | $$| $$    $$| $$   \\$$      |  $$$$$$       | $$ | $$ | $$| $$| $$  | $$ \\$$    \\ 
| $$      | $$|  $$$$$$$| $$__/ $$| $$$$$$$$| $$            | $$_____       | $$_/ $$_/ $$| $$| $$  | $$ _\\$$$$$$\\
| $$      | $$ \\$$    $$ \\$$    $$ \\$$     \\| $$            | $$     \\       \\$$   $$   $$| $$| $$  | $$|       $$
 \\$$       \\$$  \\$$$$$$$ _\\$$$$$$$  \\$$$$$$$ \\$$             \\$$$$$$$$        \\$$$$$\\$$$$  \\$$ \\$$   \\$$ \\$$$$$$$ 
                        |  \\__| $$                                                                                
                         \\$$    $$                                                                                
                          \\$$$$$$                                                                                 
    """)
else:
    # print('Draw')
    print("""
 _______                                   
|       \\                                  
| $$$$$$$\\  ______   ______   __   __   __ 
| $$  | $$ /      \\ |      \\ |  \\ |  \\ |  \\
| $$  | $$|  $$$$$$\\ \\$$$$$$\\| $$ | $$ | $$
| $$  | $$| $$   \\$$/      $$| $$ | $$ | $$
| $$__/ $$| $$     |  $$$$$$$| $$_/ $$_/ $$
| $$    $$| $$      \\$$    $$ \\$$   $$   $$
 \\$$$$$$$  \\$$       \\$$$$$$$  \\$$$$$\\$$$$ 
                                           
                                           
                                           
    """)




    