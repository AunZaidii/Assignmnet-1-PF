def month(a):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return months[a-1]

m = int(input("Enter the number of the month: "))
print(month(m))


