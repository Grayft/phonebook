from abc import ABC, abstractmethod
from utils import get_executable_func_name


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
    pass


class BinaryTreeManager(DefaultManager):
    pass