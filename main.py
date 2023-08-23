"""Описание возможностей программы

Создание модели данных телефонного справочника:
#создает объекты Person по данным из файла 'my_data.json'
model_1 = Model(Person, 'my_data.json')

#Можно создать новую модель, которая работает отдельно от model_1
model_2 = Model(Person, 'my_data.json')

Работа с данными происходит через метод objects
#Выводит все объекты
model_1.objects.all()
#Создает объект в моделе по значениям из словаря.
model_1.objects.create({'field': value})

#Удаляет объект из модели
some_object = model_1.objects.all()[0]
model_1.objects.delete(some_object)

#Поля объекта можно обновлять, но если измененные поля могут повлиять
#на расположение объекта в справочнике, то нужно вызвать метод update_obj_place
updated_person = model_1.objects.all()[0]
updated_person.last_name = 'Петров'
model_1.objects.update_obj_place(updated_object)
"""

from model import Model
from person_model import Person


if __name__ == '__main__':
    person_model = Model(Person, 'my_data.json')
    # person_model.objects.all().
    pass
