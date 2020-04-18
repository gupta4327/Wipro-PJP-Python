def print2largest(arr,arr_size):
    if (arr_size < 2):
        print(" Invalid Input ")
        return
    first = second = -2147483648
    for i in range(arr_size):
        if (arr[i] > first):
            second = first
            first = arr[i]
        elif (arr[i] > second and arr[i] != first):
            second = arr[i]

    if (second == -2147483648):
        print("There is no runner up")
    else:
        print("The runner up is", second)

arr = list(map(int,input("Enter the numbers").split()))
n =len(arr)
print2largest(arr, n)
