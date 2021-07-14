# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# Collect input from the user
kilometers = float(input('How many kilometers?: '))
# conversion factor
conv_fac = 0.621371
# calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' % (kilometers, miles))