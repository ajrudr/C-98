def countWordsFromFile():
    fileName=input("enterthefilename: ")

    numberofWords=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberofWords=numberofWords+len(words)
    print("Number of Words: ")
    print(numberofWords)

countWordsFromFile()   