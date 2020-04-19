def ispalindrome(name):
    if name==name[::-1]:
        return True
    else:
        return False

def count_the_vowels(name):
    count=0
    vowels=set("aeiouAEIOU")
    for i in name:
        if i in vowels:
            count+=1
    return count

def frequency_of_letters(name):
    dict={}
    for i in name:
        dict[i]=dict.get(i,0)+1
    return dict
