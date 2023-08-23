from abc import ABC, ABCMeta, abstractmethod
from manager import AbstractManager, DefaultManager
from utils import get_executable_func_name
from loaders import JSONReader, JSONWriter


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

    def _get_data(self) -> list[dict]:
        """Возвращает прочитанные из файла данные в виде списка словарей"""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')

    @abstractmethod
    def save_into_file(self, file_name_to_write: str):
        """Сохраняет данные в файл"""
        raise NotImplementedError(
            f'{get_executable_func_name()} in class: {self.__class__}')


class Model(AbstractModel):
    def __init__(self, model: type, file_name_to_read: str = None,
                 manager: type = None):
        self.model = model
        if not manager and not file_name_to_read:
            self._manager = DefaultManager(model)
            return

        self.file_name_to_read = file_name_to_read
        self._data = self._get_data()
        if not manager:
            self._manager = DefaultManager(model, self._data)
        elif AbstractManager in manager.mro():
            self._manager = manager(model, self._data)
        else:
            raise AssertionError(
                "Параметр 'manager' должен быть либо пустым, "
                "либо дочерним классом от AbstractManager!")

    @property
    def objects(self):
        return self._manager

    def save_into_file(self, file_name_to_write: str) -> None:
        file_writer = self._get_file_writer(file_name_to_write)
        data = [obj.model_dump() for obj in self.objects.all()]
        file_writer.write(data, file_name_to_write)

    def _get_data(self) -> list[dict]:
        self._file_reader = self._get_file_reader()
        try:
            data = self._file_reader.read(self.file_name_to_read)
        except IOError as e:
            print(e)
        except Exception as e:
            print('Something is wrong throughout reading file!')

        return data

    def _get_file_reader(self):
        """На основе формата файла выбирается загрузчик данных"""
        file_format = self.file_name_to_read.split('.')[-1]
        if file_format == 'json':
            return JSONReader
        else:
            raise NotImplementedError(
                f"Загрузчик формата '{file_format}'не реализован!"
            )

    def _get_file_writer(self, file_name_to_write):
        """На основе формата файла выбирается класс для выгрузки данных"""
        file_format = file_name_to_write.split('.')[-1]
        if file_format == 'json':
            return JSONWriter
        else:
            raise NotImplementedError(
                f"Класс для выгрузки данных формата '{file_format}'не реализован!"
            )
