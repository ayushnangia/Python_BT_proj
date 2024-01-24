import random


def asciiart(turn):
    match turn:
        case 6:
            return """ 
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
    ====="""
        case 5:
            return """ 
 +----+
 |    |
 O    |
/|\   |
/     |
      |
    ====="""
        case 4:
            return """ 
 +----+
 |    |
 O    |
/|\   |
      |
      |
    ====="""
        case 3:
            return """ 
 +----+
 |    |
 O    |
/|    |
      |
      |
    ====="""
        case 2:
            return """ 
 +----+
 |    |
 O    |
 |    |
      |
      |
    ====="""
        case 1:
            return """ 
 +----+
 |    |
 O    |
      |
      |
      |
    ====="""
        case 0:
            return """ 
 +----+
 |    |
      |       
      |
      |
      |
    =====
YOU LOSE"""


wordlist = ["apple", "dog", "cat", "moon", "happy", "tree", "house", "book", "sun", "river",
            "bird", "fish", "green", "cloud", "jump", "smile", "pen", "flower", "song", "friend",
            "ocean", "star", "play", "red", "run"]


def hangman():
    randindex = random.randint(0, len(wordlist)-1)
    word = wordlist[randindex].lower()
    length = len(word)
    turn = 6
    gamestr = ""
    for i in range(length):
        gamestr += '_'

    def checker(inputchar):
        updatedgamestr = ""
        for j in range(0, length):
            if gamestr[j] == '_' and inputchar == word[j]:
                updatedgamestr += inputchar
            else:
                updatedgamestr += gamestr[j]
        return updatedgamestr
    gameover = False
    while gameover == False:
        if gamestr == word:
            print("You Win. The word was %s" % word)
            gameover = True
            continue
        print(asciiart(turn))
        if turn != 0:
            print(gamestr)
            print("(%d letter word)" % length)
        else:
            print("The word was %s" % word)
            gameover = True
            continue
        while True:
            guesstype = input("Do you want to guess letter or word?")
            if guesstype.lower() in "letter" or guesstype.lower() in "word":
                break
            else:
                print("Invalid input.")
        if guesstype.lower() in "letter":
            while True:
                letter = input("Guess letter: ")
                if len(letter) == 1:
                    break
                else:
                    print("Enter a letter only.")
            if checker(letter.lower()) == gamestr:
                turn -= 1
            else:
                gamestr = checker(letter.lower())
        elif guesstype.lower() in "word":
            while True:
                guessword = input("Guess the word: ")
                if len(guessword) == length:
                    break
                else:
                    print("Length does not match.")
            if guessword.lower() == word:
                gameover = True
                print("You Win. The word was %s" % word)
                continue
            else:
                print(asciiart(0))
                print("The word was %s" % word)
                gameover = True
                continue


while True:
    hangman()
    while True:
        choice = input("Do you want to play again?(y/n): ")
        if choice.lower() == 'y' or choice.lower() == 'n':
            break
        else:
            print("invalid input")
    if choice.lower() == 'y':
        pass
    else:
        break
