cal = float(input("Enter number of calories: "))
fat = float(input("Enter number of fats: "))
x = fat*9
if cal<0 or fat<0 or x>cal:
    print("Either the calories or fat grams were incorrectly entered")
elif x<(30/100)*cal:
    print("The food is low in fat")
else:
    b=(x/cal)*100
    print("The percentage of calories from fat is ",b,"%")


