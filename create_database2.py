from faker import Faker

from models2.database import create_db, Session
from models2.hospital import Hospital


def create_database2(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):

    faker = Faker('ru_RU')
    session.commit()

    group_list = ['Областная больница', 'Больница имени Лазарева', 'Больница имени Бушева', 'Детская больница']

    for _ in range(10):
        country = faker.country()
        town = faker.city()
        name = faker.random.choice(group_list)
        number = faker.phone_number()
        number_hospital = faker.random.randint(1, 25)
        hospital = Hospital(country, town, name, number, number_hospital)
        session.add(hospital)

    session.commit()
    session.close()
