string = input("Enter a string:\n")
n = int(input("Enter n: "))
if len(string)<2:
    print("Invalid input string")
else:
    print(string[:2]*n)
