from abc import ABC, ABCMeta, abstractmethod
from pydantic import BaseModel
from manager import AbstractManager, DefaultManager
from utils import get_executable_func_name


class AbstractModel(ABC):
    """Абстрактный класс модели данных."""
    @property
    @abstractmethod
    def objects(self):
        """Работа с данными происходит через это свойство"""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @objects.setter
    def objects(self):
        """Предполагается, что структура данных,
        в которой будут храниться данные, выбирается перед их загрузкой
        и далее не подлежит изменению."""
        raise AssertionError(
            "Аттрибут 'objects' нельзя изменить для уже созданного экземпляра класса"
            "Для этого действия создайте новый обьект класса!")

    @abstractmethod
    def _get_file_reader(self):
        """В зависимости от формата файла с данными выбирается класс,
        который будет парсить файл."""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @abstractmethod
    def _get_file_writer(self):
        """В зависимости от формата файла, в который необходимо сохранить данные,
        выбирается класс для записи."""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    def _get_data(self) -> list(dict):
        """Возвращает прочитанные из файла данные в виде списка словарей"""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @abstractmethod
    def save_into_file(self, file_name_to_write: str):
        """Сохраняет данные в файл"""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')


class Model(AbstractModel):
    def __init__(self, model: type, file_name_to_read: str,
                 manager: type = None):
        self.model = model
        self.file_name_to_read = file_name_to_read

        self._data = self._get_data()
        if manager is None:
            self._manager = DefaultManager(model, self._data)
        elif isinstance(manager, type):
            if AbstractManager in manager.mro():
                self._manager = manager(model, self._data)
        else:
            raise AssertionError(
                "Параметр 'manager' должен быть либо пустым, "
                "либо дочерним классом от AbstractManager!")

    @property
    def objects(self):
        return self._manager

