def indexes(a,b):
    list=[]
    for j in range(len(a)):
        if b==a[j]:
            list.append(j)
    return list

w = input("Enter your word/sentence: ")
s = input("Enter the alphabet of which the index is required: ")
print("The index of",s,"is",indexes(w.casefold(),s.casefold()))
