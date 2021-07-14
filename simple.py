def sample(cc):
    def inner(x):
        auto(x)
        cc(x)
    return inner


def auto(dd):
    print("hello World", dd)

# ddd = sample(auto)

@sample
def other(y):
    print("this function is called", str(y))

debut = sample(other)
# debut
other("mn")


def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The H.C.F. of", num1, "and", num2, "is", hcf(num1, num2))