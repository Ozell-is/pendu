import random

HANGMAN_PICS: ['''
    +++---+++
            |
            |
            |
           ===''', '''
    +++---+++
     0      |
            |
            |
           ===''', '''
    +++---+++
     0      |
     |      |
            |
           === ''', '''
    +++---+++
     0      |
    /|      |
            |
           === ''', '''
    +++---+++
     0      |
    /|\     |
            |
           ===       ''', '''
    +++---+++
     0      |
    /|\     |
    /       |
           ===        ''', '''
    +++---+++
     0      |
    /|\     |
    / \     |
           ===        ''']

words = ('aigle babouin baleine belette blaireau bouc canard'
         ' canari castor cerf chameau chat cheval chien chouette '
         ' cigogne cobra cochon corbeau corneille couleuvre'
         ' coyote crapaud crotale cygne dauphin dindon dromadaire'
         ' faucon fourmi furet gorille grenouille hibou'
         ' hippopotame lama lapin lion loup mouton mule mygale'
         ' oie otarie ours palourde panda paresseux perroquet'
         ' phoque pigeon poisson puma putois python rat renard '
         ' renne requin salamandre saumon singe souris taupe'
         ' tigre tortue truite').split()

def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist)-1)
    return wordlist[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('mauvaise lettres: ', ' ')
    for letter in missedLetters:
        print(letter, ' ')
    print()

    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, ' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Propose une lettre')
        guess=input()
        guess=guess.lower()
        if len(guess) != 1:
            print('une seule lettre accepté')
        elif guess in alreadyGuessed:
            print('deja faite')

        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('ceci n\'est pas une lettre')
        else:
            return guess

def playAgain():
    print('veux tu rejouer')
    return input().lower().startswith('o')

print ('P E N D U')
missedLetters =''
correctLetters=''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters,correctLetters,secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters+guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Oui! Le mot secret est"' +secretWord +'"! Tu as gagné!')
                gameIsDone = True
            else:
                missedLetters=missedLetters+guess
                if len(missedLetters) == len(HANGMAN_PICS) -1:
                    displayBoard(missedLetters, correctLetters, secretWord)
                    print('Tu as perdu! \n Après' +str(len(missedLetters))+ ' mauvaise lettres et '+str(len(correctLetters))+ ' lettres exacte, le mot etait ' +secretWord+'.')

        if gameIsDone:
            if playAgain():
                missedLetters =''
                correctLetters=''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
