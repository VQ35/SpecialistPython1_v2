def my_abs(...):
    ...
    return ...


print(my_abs(-5))
print(my_abs(5))
print(my_abs(0))

def my_abs(a):
    if a>0:
        return a
    else:
        return a*(-1)
rez=my_abs(-5)
print(rez)

def my_abs(a):
    if a>=0:
        return a
    else:
        return a*(-1)
rez=my_abs(0)
print(rez)
