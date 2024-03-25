"""Задание 2 (НЕ ДОДЕЛАЛ!!!)

Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и
меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя.

"""


#Создаём класс и инициализируем атрибуты класса
class Dog:
    def __init__(self, dog_cls_attr_name, dog_cls_attr_height, dog_cls_attr_weight, dog_cls_attr_age):
        self.dog_cls_attr_name = dog_cls_attr_name
        self.dog_cls_attr_height = dog_cls_attr_height
        self.dog_cls_attr_weight = dog_cls_attr_weight
        self.dog_cls_attr_age = dog_cls_attr_age
        

#Добавляем методы класса
    def jump():
        print("Doggy jumps.")
    
    
    def run():
        print("Doggy runs.") 
    
    
    def bark():
        print("Doggy barks.")
        

#Добавляем объект 
doggy_1 = Dog("Fluffy", 15, 20, 5)


#Выводим атрибуты и методы
print(
    f"Name of the dog is {doggy_1.dog_cls_attr_name}, he is {doggy_1.dog_cls_attr_height} cm tall, his weight is {doggy_1.dog_cls_attr_weight} and he is {doggy_1.dog_cls_attr_age} years old."
    )


Dog.bark()
Dog.jump()
Dog.run()


"""Вывод

Name of the dog is Fluffy, he is 15 cm tall, his weight is 20 and he is 5 years old.
Doggy barks.
Doggy jumps.
Doggy runs.

"""
