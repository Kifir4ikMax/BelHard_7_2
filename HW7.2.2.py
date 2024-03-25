"""Задание 2 (ДОДЕЛАЛ!!!)

Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и
меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя.

"""


# Создаём класс и инициализируем атрибуты класса
class Dog:
    def __init__(self, name: str, height: int, weight: int, age: int):
        self.dog_attr_name = name
        self.dog_attr_height = height
        self.dog_attr_weight = weight
        self.dog_attr_age = age

    # Добавляем методы класса
    def jump(self):
        print(f"Doggy jumps.")

    def run(self):
        print("Doggy runs.")

    def bark(self):
        print("Doggy barks.")

    # Добавляем метод замены имени
    def change_name(self, name):
        self.dog_attr_name = name


# Добавляем объект
doggy_1 = Dog("Fluffy", 15, 20, 5)


# Выводим атрибуты и методы
print(
    f"Name of the dog is {doggy_1.dog_attr_name}, he is {doggy_1.dog_attr_height} cm tall, his weight is {doggy_1.dog_attr_weight} and he is {doggy_1.dog_attr_age} years old."
)
doggy_1.bark()
doggy_1.jump()
doggy_1.run()
print(doggy_1.dog_attr_name)


# Меняем имя
doggy_1.change_name("Whitey")
print(doggy_1.dog_attr_name)


"""Вывод

Name of the dog is Fluffy, he is 15 cm tall, his weight is 20 and he is 5 years old.
Doggy barks.
Doggy jumps.
Doggy runs.
Fluffy
Whitey

"""
