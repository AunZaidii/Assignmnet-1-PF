def water():
    input("Putting water. To continue press enter.")
def sugar():
    input("Adding sugar. To continue press enter.")
def mix1():
    input("Mixing well. To continue press enter.")
def coffee():
    input("Adding coffee. To continue press enter.")
def milk():
    input("Adding milk. To continue press enter.")
def mix2():
    input("Mixing well again. To continue press enter.")
def timing(c, t, d):
    if c.lower() == "w" and d.lower() == "d":
        t =76* 1.5
    elif c.lower() == "b" and d.lower() == "d":
        t = 105* 1.5
    elif c.lower() == "b" and d.lower()== "n":
        t = 105
    elif c.lower() =="w" and d.lower() == "n":
        t = 76
    print(f"Your coffee will be ready in {t} mins.")
def manual_b(c):
    if c.lower() == "w":
        water(), sugar(), mix1(), coffee(), milk(), mix2()
    elif c.lower() == "b":
        water(), sugar(), mix1(), coffee(), mix2()
def auto():
    print("Your coffee is being prepared...")
coffee_type = input("What type of coffee would you like? (W) for White or (B) for Black. ")
size = input("What size would you like? (N) for Normal or (D) for Double.")
manual = input("Would you like to have manual brew? (Y) for Yes or (N). ")
timer = 0
if manual == "Y" or manual == "y":
    manual_b(coffee_type)
    timing(coffee_type, timer, size)
elif manual == "N" or manual == "n":
    auto()
    timing (coffee_type, timer, size)