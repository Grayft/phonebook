import pytest
from pydantic import ValidationError
from person_model import Person
from itertools import zip_longest


class TestPerson:
    """Тестирование класса Person"""
    person_data_1 = {'last_name': 'Петров',
                     'first_name': 'Владимир',
                     'middle_name': 'Олегович',
                     'organization_name': 'None',
                     'work_phone_number': '89433452323',
                     'mobile_phone_number': '89433452323'
                     }
    person_data_2 = {'last_name': 'Петров',
                     'first_name': 'Владимир',
                     'middle_name': 'Олегович',
                     'organization_name': '1',
                     'work_phone_number': '9091234565',
                     'mobile_phone_number': '9091234565'
                     }
    person_data_3 = {'last_name': 'Петров',
                     'first_name': 'Владимир',
                     'middle_name': 'Андреевич',
                     'organization_name': '----',
                     'work_phone_number': '+72344561223',
                     'mobile_phone_number': '+72344561223'
                     }
    person_data_4 = {'last_name': 'Якубович',
                     'first_name': 'Владимир',
                     'middle_name': 'Андреевич',
                     'organization_name': '----',
                     'work_phone_number': '+72344561223',
                     'mobile_phone_number': '+72344561223'
                     }

    sorted_fields = ('last_name', 'first_name', 'middle_name')

    @pytest.mark.parametrize(
        "person_data", (
                person_data_1, person_data_2, person_data_3, person_data_4
        )
    )
    def test_init(self, person_data):
        """Тест на создание экземпляра с валидными данными"""
        assert isinstance(Person(**person_data), Person)

    @pytest.mark.parametrize(
        "person_data", (
                {'last_name': 'Петров',
                 'first_name': '',
                 'middle_name': '',
                 'organization_name': '',
                 'work_phone_number': '+72344561223',
                 'mobile_phone_number': '+72344561223'
                 },
                {'last_name': 'Петроооооооооооооооооооооооов',
                 'first_name': 'Дмитрий',
                 'middle_name': 'Викторович',
                 'organization_name': '',
                 'work_phone_number': '+72344561223',
                 'mobile_phone_number': '+72344561223'
                 }
        )
    )
    def test_validate_name(self, person_data):
        """Тест валидации имени"""
        with pytest.raises(ValidationError):
            Person(**person_data)

    @pytest.mark.parametrize(
        "person_data", (
                {'last_name': 'Петров',
                 'first_name': 'Владимир',
                 'middle_name': 'Олегович',
                 'organization_name': '',
                 'work_phone_number': '+ad',
                 'mobile_phone_number': '+72344561223'
                 },
                {'last_name': 'Петров',
                 'first_name': 'Владимир',
                 'middle_name': 'Олегович',
                 'organization_name': '',
                 'work_phone_number': '+72344561223',
                 'mobile_phone_number': 'ag'
                 },
                {'last_name': 'Петров',
                 'first_name': 'Владимир',
                 'middle_name': 'Олегович',
                 'organization_name': '',
                 'work_phone_number': '+72344561223',
                 'mobile_phone_number': ''
                 }
        )
    )
    def test_validate_phone(self, person_data):
        """Тест валидации номера телефона"""
        with pytest.raises(ValidationError):
            Person(**person_data)

    @pytest.mark.parametrize(
        "person_data, person_data_other, expected",
        (
                (person_data_1, person_data_1, True),
                (person_data_1, person_data_2, True),
                (person_data_1, person_data_3, False),
                (person_data_1, person_data_4, False),
        )
    )
    def test_eq(self, person_data, person_data_other, expected):
        """Тест на равенство двух объектов Person.
        Если ФИО равны, то - True"""
        assert (Person(**person_data) == Person(
            **person_data_other)) == expected

    def test_ne(self):
        """Тест на неравенство объектов"""
        assert Person(**self.person_data_1) != Person(**self.person_data_4)

    @pytest.mark.parametrize(
        "person_data, person_data_other",
        (
                (person_data_3, person_data_1),
                (person_data_1, person_data_4),
                (person_data_3, person_data_4),
        )
    )
    def test_lt(self, person_data, person_data_other):
        """Проверка оператора '<' """
        assert Person(**person_data) < Person(**person_data_other)

    @pytest.mark.parametrize(
        "person_data, person_data_other",
        (
                (person_data_1, person_data_1),
                (person_data_1, person_data_2),
                (person_data_3, person_data_1),
                (person_data_1, person_data_4),
                (person_data_3, person_data_4),
        )
    )
    def test_le(self, person_data, person_data_other):
        """Проверка оператора '<=' """
        assert Person(**person_data) <= Person(**person_data_other)

    @pytest.mark.parametrize(
        "person_data, person_data_other",
        (
                (person_data_4, person_data_1),
                (person_data_4, person_data_3),
                (person_data_1, person_data_3),
        )
    )
    def test_gt(self, person_data, person_data_other):
        """Проверка оператора '>' """
        assert Person(**person_data) > Person(**person_data_other)

    @pytest.mark.parametrize(
        "person_data, person_data_other",
        (
                (person_data_4, person_data_1),
                (person_data_4, person_data_3),
                (person_data_1, person_data_3),
                (person_data_1, person_data_1),
                (person_data_1, person_data_2),
        )
    )
    def test_ge(self, person_data, person_data_other):
        """Проверка оператора '>=' """
        assert Person(**person_data) >= Person(**person_data_other)

    def test_sorted_fields(self):
        """Проверка, что поля для сортировки не изменились"""
        person_sorted_fields = Person(**self.person_data_1)._sorted_fields
        for val_1, val_2 in zip_longest(self.sorted_fields,
                                        person_sorted_fields):
            assert val_1 == val_2
