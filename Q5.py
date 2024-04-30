
def interest(a):
    from math import log
    b = log(2)/log(1+a)
    return b

interest_rate = float(input("Enter the interest rate per year: "))
print("the time in which the principle amount will be doubled is",interest(interest_rate),"years.")


