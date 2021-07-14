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

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)

# Output: <function Person.greet>
print(Person.greet)

# Output: "This is a person class"
print(Person.__doc__)