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

