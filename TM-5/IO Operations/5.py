def longestWord(string):

    length = 0
    for word in string.split():
        if(len(word) > length):
            length = len(word)
            bigWord = word

    return bigWord

name = input("enter file name: ")
try:
    f1 = open(name)
except:
    print("file does not exist")
print(longestWord(f1.read()))
f1.close()
