list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("Existing list of tuples :", list1)
print("Replaced list of tuples :")
print([t[:-1]+(100,) for t in list1])
