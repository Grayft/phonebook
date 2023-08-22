from abc import ABC, abstractmethod
from utils import get_executable_func_name


class AbstractReader(ABC):
    """Абстрактный класс для загрузки данных из файла."""
    @abstractmethod
    def read(self, file_name: str) -> list[dict]:
        """Читает данные из файла и возвращает список словарей,
        где ключ - это наименование поля, а значение - это значение"""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')


class AbstractWriter(ABC):
    """Абстрактный класс для записи данных в файл."""
    @abstractmethod
    def write(self, file_name: str) -> None:
        """В зависимости от конкретного класса
        записывает данные в необходимый формат файла."""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')


class JSONReader(AbstractReader):
    pass


class JSONWriter(AbstractWriter):
    pass