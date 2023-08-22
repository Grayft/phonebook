from abc import ABC, abstractmethod
from utils import get_executable_func_name
import json

class AbstractReader(ABC):
    """Абстрактный класс для загрузки данных из файла."""
    @classmethod
    @abstractmethod
    def read(cls, file_name: str) -> list[dict]:
        """Читает данные из файла и возвращает список словарей,
        где ключ - это наименование поля, а значение - это значение"""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {cls.__class__}')


class AbstractWriter(ABC):
    """Абстрактный класс для записи данных в файл."""
    @classmethod
    @abstractmethod
    def write(cls, file_name: str) -> None:
        """В зависимости от конкретного класса
        записывает данные в необходимый формат файла."""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {cls.__class__}')


class JSONReader(AbstractReader):
    @classmethod
    def read(cls, file_name: str) -> list[dict]:
        with open(file_name) as file:
            return json.load(file)


class JSONWriter(AbstractWriter):
    @classmethod
    def write(cls, data, file_name: str) -> None:
        with open(file_name, 'w') as file:
            json.dump(data, file)
