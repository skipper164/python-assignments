"""number = 13

def get_square():
    square = number ** 2
    return square

print(get_square())




def get_square(number):
    return number ** 2

print(get_square(5))
print(get_square(15))
print(get_square(20))


def display_name(age, name):
    for _ in range(age):
        print(name)

display_name(10, "tobi")"""



def get_product(*numbers):
    product = 1
    for number in numbers:
        print(number)
        product *= number
    return product
print(get_product(3, 6, 5, 6, 7))

print(get_product(4, 3, 7, 9, 10, 15, 17, 21, 12, 45))



