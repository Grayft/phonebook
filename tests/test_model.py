import pytest
from model import Model
from person_model import Person


class TestModel:
    """Тестирование класса Model"""

    person_data = {'last_name': 'Петров',
            'first_name': 'Владимир',
            'middle_name': 'Олегович',
            'organization_name': '1',
            'work_phone_number': '9091234565',
            'mobile_phone_number': '9091234565'
                   }

    def test_init_null(self):
        """Тест создания пустой модели"""
        model = Model(Person)
        assert len(model.objects.all()) == 0

    def test_create(self):
        """Тест функции create"""
        model = Model(Person)
        p1 = Person(**self.person_data)
        p2 = model.objects.create(self.person_data)
        assert p1 == p2
        for f1, f2 in zip(p1.model_fields, p2.model_fields):
            assert f1 == f2

    def test_delete(self):
        """Тест функции delete"""
        model = Model(Person)
        p1 = model.objects.create(self.person_data)
        model.objects.delete(p1)
        assert len(model.objects.all()) == 0

    def test_filter(self):
        """Тестирование функции filter"""
        model = Model(Person)
        p1 = model.objects.create(self.person_data)
        assert p1 in model.objects.all()
        p2 = model.objects.filter(mobile_phone_number='9091234565')[0]
        assert p1 == p2

    def test_filter_null(self):
        """Тестирование функции filter при отсутствии результата"""
        model = Model(Person)
        p1 = model.objects.create(self.person_data)
        assert p1 in model.objects.all()
        p2 = model.objects.filter(last_name='Unknown')
        assert len(p2) == 0