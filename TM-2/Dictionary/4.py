d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Existing dictionary :",d)
print("\n")
print("The keys are:")
for i in d.keys():
    print(i,end=" ")
print("\n")
print("The values are:")
for i in d.values():
    print(i,end=" ")
print("\n")
print("The keys and values are:")
for k,v in d.items():
    print(k,":",v)
