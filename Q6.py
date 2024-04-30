lists = list(input("Enter numbers to add in the list: "))
print(lists)
for i in lists:
    if int(i)%3==0:
        print(i,end=" ")

