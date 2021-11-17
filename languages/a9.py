import csv

def getLanguages(fileName):
    with open(fileName, newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            return row

def getTranslationLanguage(langList):
    print("Translate English words to one of the following languages: ", end = "")
    for l in langList:
        if not l == "English":
            print(l, end = " ")
    print()
    choice = input("Enter a language: ").title()

    while not choice in langList and not choice == "English":
        print("The program does not support " + choice)
        choice = input("Enter a language: ").title()
    print()
    return choice

def readFile(langList, langStr, fileName):
    words = []

    column = 0
    while (not langList[column] == langStr):
        column += 1

    with open(fileName, newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if not row[column] == langStr:
                words.append(row[column])
    return words

def createResultsFile(language):
    with open(language + ".txt", 'w') as file:
        file.write("Words translated from English to " + language + "\n")
        return

def translateWords(englishList, translationList, language):
     with open(language + ".txt", 'a') as file:
        c = "y"
        while c == "y":
            word = input("Enter a word to translate: ").lower()
            if not (word in englishList):
                print(word + " is not in the list")
                c = input("Another word (y or n)? ").lower()
                print()
                continue
            index = 0
            while not (englishList[index] == word):
                index += 1
            if (translationList[index] == "-"):
                print(word + "did not have a translation")
            else:
                print(word + " is translated to " + translationList[index])
                file.write(word + " = " + translationList[index] + "\n")
            c = input("Another word (y or n)? ").lower()
            print()
        print("Translated words have been saved to " + language + ".txt")

def main():
    langList = getLanguages("languages.csv")
    transLang = getTranslationLanguage(langList)
    words = readFile(langList, transLang, "languages.csv")
    eWords = readFile(langList, "English", "languages.csv")
    createResultsFile(transLang)
    translateWords(eWords, words, transLang)

main()

