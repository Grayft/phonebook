from abc import ABC, abstractmethod
from utils import get_executable_func_name
from pydantic import BaseModel


class AbstractManager(ABC):
    @abstractmethod
    def __init__(self, model: type, data: list[dict]):
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
    def delete(self, obj) -> None:
        """Удаляет обьект из структуры данных"""
        pass

    @abstractmethod
    def filter(self):
        pass

    def update_obj_place(self):
        """Обновляет положение объекта в структуре данных
        Метод необходимо вызвать, если данные объекта были обновлены"""
        pass


class DefaultManager(AbstractManager):
    """Менеджер данных по умолчанию хранит данные в списке"""

    def __init__(self, model: BaseModel, data: list[dict]) -> None:
        self.model = model
        self.structure = SortedList()
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

    def filter(self, **kwargs) -> list[BaseModel]:
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    def update_obj_place(self, obj: BaseModel) -> None:
        self.structure.update_obj_place(obj)


class BinaryTreeManager(DefaultManager):
    pass


class AbstractSortedDataStructure(ABC):
    """Абстрактный класс сортированной структуры данных"""
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


class SortedList(AbstractSortedDataStructure):
    def __init__(self):
        self.sorted_list = []

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

