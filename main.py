from base_model import Model
from person_model import Person


class PersonModel(Model):
    pass


if __name__ == '__main__':
    person_model = Model(Person, 'my_data.json')
    # person_model.objects.all().
    pass
