# example_flake8.py

import os, sys # Несоответствие PEP8: импорты через запятую и не в алфавитном порядке


def add_numbers(a, b):return a + b # Отсутствие отступов и длинная строка


def greet(name): 
 print(f"Привет, {name}!") # Отступ неправильного размера


class customClass:  # Имя класса не соответствует стилю
    def __init__(self, value):
        self.value=value # Нет пробелов вокруг "="
    def print_value(self): 
        print(self.value) # Отсутствие пустой строки между методами


def main():
    obj = customClass("Example")
    obj.print_value()
    add_numbers(5, 7)  # Функция вызывается, но результат не используется
    greet("User")


main()  # Нет проверки на __name__ == '__main__'
