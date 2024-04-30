def many(a):
    b=[]
    b+= a.split(" ")
    x = 0
    y = 0
    z = 0
    w = 0
    for i in b:
        if len(i)==1:
            x+=1
        elif len(i)==2:
            y+=1
        elif len(i)==3:
            z+=1
        elif len(i)==4:
            w+=1
    print("words of length 1=",x)
    print("words of length 2=", y)
    print("words of length 3=", z)
    print("words of length 4=", w)

f=open("sample.txt")
print(many(f.read()))

