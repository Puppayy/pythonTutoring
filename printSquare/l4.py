def printSquare(size):
    printRect(size,size)

def printRect(length, width):
    for i in range(0, length + 2):
        for j in range(0, width + 2):
            if (j == 0 or j == width + 1) and (i == 0 or i == length + 1):
                print(" ", sep = '', end = '')
            elif (i == 0 or i == length + 1):
                print("-", sep = '', end = '')
            elif (j == 0 or j == width + 1):
                print("|", sep = '', end = '')
            else:
                print(" ", sep = '', end = '')
        print()

def main():
    # testing
    # printRect(5,3)
    # printSquare(4,4)
    print("Welcome to the shape printer!")
    print("r) Rectangle")
    print("s) Square")
    shape = input("Enter the shape you want to print: ")
    if shape in "r":
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        printRect(length, width)
    elif shape in "s":
        size = int(input("Enter the size: "))
        printSquare(size)
    else:
        print("That shape is not supported.")
main()