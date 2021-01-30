from os import system, name

c4 = [['o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o']]
gameEnd = False
letterNumber = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
player = 1

def printC4():
    
    for a in zip(*c4):
        print(*a)
    print("A B C D E F G")

def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

while gameEnd == False:
    clear()
    printC4()
    rowLetter = input("What row do you want your piece in? :").upper()
    rowNumber = letterNumber[rowLetter]

    if 'o' in c4[rowNumber]:
        if player == 1:
            c4[rowNumber][listRightIndex(c4[rowNumber], 'o')] = '1'
            player = 2
        elif player == 2:
            c4[rowNumber][listRightIndex(c4[rowNumber], 'o')] = '2'
            player = 1