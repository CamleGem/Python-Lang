def name(first, second = 100):
    print(first + " " + str(second))


name('name')

try:
    print(5/0)
except ZeroDivisionError:
    print("wrong param!\n")

check = lambda x: x > 5

def check_value(value):
    return value > 5

def compare(list):
    return [value for value in list if check_value(value)]



print(compare([1, 2, 3, 4, 6, 7, 8]))