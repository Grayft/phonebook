from abc import ABC, abstractmethod
from utils import get_executable_func_name
from pydantic import BaseModel


class AbstractManager(ABC):
    @abstractmethod
    def __init__(self, model: type, data: list[dict]):
        raise NotImplementedError('')

    @abstractmethod
    def all(self):
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @abstractmethod
    def save(self):
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @abstractmethod
    def create(self):
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @abstractmethod
    def update(self):
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @abstractmethod
    def delete(self):
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @abstractmethod
    def filter(self):
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    def _form_data_structure(self):
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')


class DefaultManager(AbstractManager):
    """Менеджер данных по умолчанию хранит данные в списке"""

    def __init__(self, model: BaseModel, data: list[dict]) -> None:
        self.model = model
        self._sorted_data_structure = []
        for obj in data:
            self.create(**obj)

    def all(self) -> list:
        return self._sorted_data_structure

    def create(self, obj: dict) -> BaseModel:
        new_obj = self.model(obj)
        self._sorted_data_structure.append(new_obj)

    def filter(self, **kwargs):
        pass


class BinaryTreeManager(DefaultManager):
    pass
