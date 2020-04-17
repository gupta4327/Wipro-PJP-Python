num = input("Enter a number: ")
list1 = [x for x in num]
rev= "".join(list1[::-1])
if num==rev:
    print(num,"is a Palindrome")
else:
    print(num,"is not a Palindrome")
