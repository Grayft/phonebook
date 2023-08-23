from abc import ABC, abstractmethod
from utils import get_executable_func_name
from pydantic import BaseModel


class AbstractManager(ABC):
    @abstractmethod
    def __init__(self, model: type, data: list[dict] = None):
        pass

    @abstractmethod
    def all(self) -> list:
        """Возвращает все обьекты модели"""
        pass

    @abstractmethod
    def create(self, obj: dict):
        """Создает обьект класса model и помещает в сортированную стрпуктуру данных"""
        pass

    @abstractmethod
    def delete(self, obj: BaseModel) -> None:
        """Удаляет обьект из структуры данных"""
        pass

    @abstractmethod
    def filter(self, **kwargs) -> list:
        pass

    def update_obj_place(self, obj: BaseModel) -> None:
        """Обновляет положение объекта в структуре данных
        Метод необходимо вызвать, если данные объекта были обновлены"""
        pass


class DefaultManager(AbstractManager):
    """Менеджер данных по умолчанию хранит данные в списке"""

    def __init__(self, model: BaseModel, data: list[dict] = None):
        self.model = model
        self.structure = SortedList(self.model._sorted_fields.default)
        if data:
            for obj in data:
                self.create(obj)

    def all(self) -> list:
        return self.structure.structure_in_list()

    def create(self, obj: dict) -> BaseModel:
        new_obj = self.model(**obj)
        self.structure.add(new_obj)
        return new_obj

    def delete(self, obj: BaseModel) -> None:
        self.structure.delete(obj)

    def update_obj_place(self, obj: BaseModel) -> None:
        self.structure.update_obj_place(obj)

    def filter(self, **kwargs) -> list[BaseModel]:
        find_keys = set(kwargs.keys())
        model_fields = set(self.model.model_fields.keys())
        invalid_keys = find_keys.difference(model_fields)
        if invalid_keys:
            raise KeyError(
                f'В объекте {self.model} нет таких полей: {invalid_keys}')

        return self.structure.filter(**kwargs)


class AbstractSortedDataStructure(ABC):
    """Абстрактный класс сортированной структуры данных"""

    def __init__(self, order_by: list):
        self.order_by = order_by

    @abstractmethod
    def add(self, obj: BaseModel) -> None:
        """Добавляет новый элемент в структуру данных"""
        pass

    @abstractmethod
    def delete(self, obj: BaseModel) -> None:
        """Удаляет объект из структуры данных"""
        pass

    @abstractmethod
    def structure_in_list(self) -> list:
        """Возвращает структуру данных в виде списка"""
        pass

    @abstractmethod
    def filter(self, **kwargs) -> list:
        """Фильтрует объекты с учетом сортировки."""
        pass


class SortedList(AbstractSortedDataStructure):
    def __init__(self, order_by: list):
        self.sorted_list = []
        self.order_by = order_by

    def structure_in_list(self):
        return self.sorted_list

    def add(self, obj: BaseModel) -> None:
        j = 0
        for i, v_obj in enumerate(self.sorted_list):
            if obj > v_obj:
                j = i
                break
        self.sorted_list.insert(j, obj)

    def delete(self, obj: BaseModel) -> None:
        self.sorted_list.remove(obj)

    def update_obj_place(self, obj: BaseModel) -> None:
        self.delete(obj)
        self.add(obj)

    def filter(self, **kwargs):
        result = []
        for obj in self.sorted_list:
            filter_flag = True
            for key, val in kwargs.items():
                if getattr(obj, key) != val:
                    filter_flag = False
                    break
                if key == self.order_by[0] and val > getattr(obj, key):
                    return result
            if filter_flag:
                result.append(obj)
        return result
