import pytest
from pydantic import ValidationError
from person_model import Person


class TestPerson:
    p1 = Person(**{'last_name': 'Петров',
                   'first_name': 'Владимир',
                   'middle_name': 'Олегович',
                   'organization_name': 'None',
                   'work_phone_number': '89433452323',
                   'mobile_phone_number': '89433452323'
                   })
    p2 = Person(**{'last_name': 'Петров',
                   'first_name': 'Владимир',
                   'middle_name': 'Олегович',
                   'organization_name': '1',
                   'work_phone_number': '9091234565',
                   'mobile_phone_number': '9091234565'
                   })
    p3 = Person(**{'last_name': 'Петров',
                   'first_name': 'Владимир',
                   'middle_name': 'Андреевич',
                   'organization_name': '----',
                   'work_phone_number': '+72344561223',
                   'mobile_phone_number': '+72344561223'
                   })

    p4 = Person(**{'last_name': 'Якубович',
                   'first_name': 'Владимир',
                   'middle_name': 'Андреевич',
                   'organization_name': '----',
                   'work_phone_number': '+72344561223',
                   'mobile_phone_number': '+72344561223'
                   })

    def test_eq(self):
        assert self.p1 == self.p2, 'Person != Person'

    def test_ne(self):
        assert self.p1 != self.p3, 'Ne_test'

    def test_lt(self):
        assert self.p3 < self.p1, 'middle_name'

    def test_le(self):
        assert self.p1 <= self.p1, 'p1 <= p1'
        assert self.p1 <= self.p4, 'p1 <= p1'

    def test_gt(self):
        assert self.p4 > self.p1, 'p4 > p1'
        assert self.p4 > self.p2, 'p4 > p2'
        assert self.p4 > self.p3, 'p4 > p3'

    def test_ge(self):
        assert self.p4 >= self.p4, 'p4 >= p4'
        assert self.p4 >= self.p1, 'p4 >= p1'
        assert self.p4 >= self.p3, 'p4 >= p3'

    def test_name_validation(self):
        with pytest.raises(ValidationError):
            p = Person(**{'last_name': 'Петров',
                          'first_name': '',
                          'middle_name': '',
                          'organization_name': '',
                          'work_phone_number': '+72344561223',
                          'mobile_phone_number': '+72344561223'
                          })
            p = Person(**{'last_name': 'Петроооооооооооооооооооооооов',
                          'first_name': 'Дмитрий',
                          'middle_name': 'Викторович',
                          'organization_name': '',
                          'work_phone_number': '+72344561223',
                          'mobile_phone_number': '+72344561223'
                          })

    def test_phone_validation(self):
        with pytest.raises(ValidationError):
            p = Person(**{'last_name': 'Петров',
                   'first_name': 'Владимир',
                   'middle_name': 'Олегович',
                   'organization_name': '',
                   'work_phone_number': '+ad',
                   'mobile_phone_number': '+72344ada5s223'
                   })