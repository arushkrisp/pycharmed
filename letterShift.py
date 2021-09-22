import string
inpWord = input("Your word (No spaces or special characters please): ")
inpShift = input("How much you want your letters to shift by: ")
inpWord = str(inpWord)
inpShift = int(inpShift)

def letterShift(word, shift):
    indexNum = []
    shiftedLetters = []
    alphabetStr = string.ascii_lowercase
    alphabetList = list(alphabetStr)
    for letter in word:
        indexNum.append(alphabetList.index(letter.lower()))
    for num in indexNum:
        shiftedLetters.append(alphabetList[(num + shift) % (len(alphabetList))])
    newWord = "".join(shiftedLetters)
    print(newWord)
letterShift(inpWord, inpShift)