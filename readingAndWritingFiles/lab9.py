import csv


def readFile(user_genre, filename):
    showList = []
    with open(filename, newline = '') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar='|')
        for row in reader:
            if (user_genre in row[1]):
                showList.append(row[0])
    return showList

def writeFile(genre, show_list):
    with open(genre + ".txt", 'a') as file:
        for show in show_list:
            file.write(show + "\n")
    print("The file \'" + genre + ".txt\' has the following shows: ")
    print(show_list)
    return

def main():
    print("TV Shows")
    print("Possible genres are action & adventure, animation, comedy, documentary, drama, mystery & suspense, science fiction & fantasy")
    genres = ["action", "adventure", "animation", "comedy", "documentary", "drama", "mystery", "suspense", "science fiction", "fantasy", "science fiction & fantasy", "mystery & suspense", "action & adventure"]
    genre = "N"
    while (not (genre in genres)):
        genre = input("Enter a genre: ")
    showList = readFile(genre,"shows.csv")
    writeFile(genre, showList)
    return

main()
