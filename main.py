import requests
import random
from os import system, name

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
word = ""
correct = False
wrongLetters = []
underscores = ""
error = ""
guesses = 0
difficulty = ""
wrongGuesses = 0
noGuesses = False
art = [
    """
  +---+
      |
      |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
      |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
    """
]

def getWord(minLen, maxLen):
    response = requests.get(word_site)
    words = response.content.splitlines()
    word = random.choice(words).decode("utf-8")
    while len(word) < minLen or len(word) > maxLen:
        word = random.choice(words).decode("utf-8")
    return word

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos


clear()


print("""
After 7 wrong guesses, the game ends. Good luck!

If you do not type 1, 2 or 3, the game defaults to easy mode

Select a difficulty:
[1]: Easy - words are between 17 and 22 letters
[2]: Medium - words are between 8 and 16 letters
[3]: Hard - words are shorter than 8 letters

""")

difficulty = input(":")


if difficulty == "3":
    word = getWord(0, 8)
elif difficulty == "2":
    word = getWord(7, 17)
elif difficulty == "1":
    word = getWord(16, 23)
else:
    word = getWord(16, 23)

clear()

# print(word)

for letter in word: 
# print("_", end=' ') 
    underscores += "-"

while not correct:
    print(art[wrongGuesses])
    print(error + "\n\n")
    print(underscores + "\n") 

    print("Wrong guesses: ", end=' ')
    for i in wrongLetters:
        print(i + " ", end=' ') 
    print("\n")

    guess = input("Enter your guess: ")
    
    if guess.isalpha():
        if len(guess) < 2:
            if guess in wrongLetters or guess in underscores:
                error = str(guess) + " has already been guessed"
            elif guess not in word:
                # print("in word")
                wrongLetters.append(guess)
                error = str(guess) + " is not in the word"
                wrongGuesses += 1
                # print(art[wrongGuesses])
                if wrongGuesses == 7:
                    correct = True
                    noGuesses = True
            else:
                # print("letter is in word")
                for n in charposition(word, guess):
                    underscores = underscores[:n] + guess + underscores[n+1:]
        else:
            error = "Please enter 1 letter only"
    else:
        error = "Please enter 1 letter"
    # print(wrongLetters)
    guesses += 1
    if underscores == word:
        correct = True
    clear()

if noGuesses:
    print(art[wrongGuesses])
    print("uh oh! you ran out of attempts... You couldn't get " + word)
else:   
    print("Well done! You guessed " + word + " in " + str(guesses) + " tries")

