from math import sqrt

MESSAGE = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(MESSAGE)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Выводит результат."""
    if your_number <= 0:
        return
        calc = calculate_square_root(your_number)
        print(f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {calc}')


print(MESSAGE)
calc(25.5)
