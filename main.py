from icecream import ic

def myf(value):
    if value % 2 == 0:
        ic()
        return True
    else:
        ic()
        return False

print(myf(10))
print(myf(11))
print(myf(12))

ic.disable()

print(myf(10))
print(myf(11))
print(myf(12))

ic.enable()

print(myf(10))
print(myf(11))
print(myf(12))