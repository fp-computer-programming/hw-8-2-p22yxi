def display():
    letter = str(input('enter a letter: '))
    word = str(input('enter a word: '))
    print(countNum(word,letter))

def countNum(letter, word):
    count = 0
    index = 0
    for letter in word:
        if str(word[index]) == letter :  
           print(count)
           count = count + 1
