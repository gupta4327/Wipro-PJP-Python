string = input("Enter hyphen separated sequence of colors\n")
list1 = string.split("-")
list1.sort()
print("Sorted dequence is :","-".join(list1))
