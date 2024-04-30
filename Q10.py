def crypto(a):
    return a.replace("secret","******",-1)
f = input("Enter file name: ")
f = open(f,"r")
print(crypto(f.read()))


