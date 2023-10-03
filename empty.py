from math import sqrt
import inspect


message = '''Добро пожаловать в самую лучшую программу для вычисления
          квадратного корня из заданного числа'''


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверка вводимого числа и вычисление квадратного корня."""
    root = 0
    if your_number <= 0:
        return root
    num = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {num}')


print(inspect.cleandoc(message))
calc(25.5)
