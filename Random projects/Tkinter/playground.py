# SUM OF ALL UNLIMITED ARGUMENTS
def add(*args):
    a = []
    for n in args:
        a.append(n)
    print(sum(a))


add(5, 6, 7, 8, 9)


# ANOTHER WAY

def add(*args):
    a = 0
    for n in args:
        a += n
    return a


print(add(5, 6, 7, 8, 9))


# KEYWORD ARGUMENTS
def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.made = kw["made"]


my_car = Car(make="Nissan", made="GT-R")
print(my_car.make)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)