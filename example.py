# example.py

import os, sys  # Несоответствие PEP8: импорты из одного модуля через запятую

def calculate_sum(a, b): # Аргументы не описаны
return a+b  # Отступы нарушают стандарт

class myClass:  # Название класса не соответствует стилю
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print("Имя:", self.name) # Строки "Имя" и "Возраст" не используют логирования
        print("Возраст:", self.age)

def main():
    user = myClass("Алиса", 30)
    user.display_info()
    result = calculate_sum(3, 4)
    print("Сумма:", result)

main()  # Нарушение: main() вызывается без стандартного шаблона __name__ == '__main__'

