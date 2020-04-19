import module as m

string=input("Enter a string: ")

if m.ispalindrome(string):
    print("Yes it is a Palindrome")
else:
    print("No it is not a palindrome")
print("no. of vowels",m.count_the_vowels(string))
print("Frequency of letters:",m.frequency_of_letters(string))        
