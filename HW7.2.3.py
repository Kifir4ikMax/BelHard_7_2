"""Задание 3

Создать класс Phone, у которого будут следующие атрибуты:
Определить атрибуты
- brand - бренд
- model - модель
- issue_year - год выпуска
Определить методы:
- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит
{name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}

"""


#Создаём класс и определяем атрибуты
class Phone:
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        

    #Метод вывода на экран имени звонящего  
    def recieve_call(self, name):
        print(f"Calling {name}.")
        

    #Метод возвращающий кортеж с параметрами
    def get_info(self):
        return (self.brand, self.model, self.issue_year)
        

    #Метод который выводит на экран информацию об устройстве
    def __str__(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.issue_year}")
        

#Создание объекта и вызов всех методов
kifir = Phone("iPhone", "X", 2019)
kifir.recieve_call("Maxim")
print(kifir.get_info())
kifir.__str__()


"""Вывод

Calling Maxim.
('iPhone', 'X', 2019)
Brand: iPhone
Model: X
Year: 2019

"""

