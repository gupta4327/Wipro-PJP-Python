def Remove(item,sets):
    sets.remove(item)
    print(sets)

# Driver Code
sets = set(["ram", "aakash", "kaushik", "anand", "prashant"])
print("Existing set : ",sets)
item = input("enter element to remove from set: ")
Remove(item,sets)
