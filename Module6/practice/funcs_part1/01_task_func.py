# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4):
    # TODO: your code here
    pass


# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))


def max4(n1,n2,n3,n4):
    numbers = [n1,n2,n3,n4]
    max_i=n1
    for num in numbers:
            if max_i<num:
                max_i=num
    return max_i

z=max4(10,12,3,4)
print(z)
