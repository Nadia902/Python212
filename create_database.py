from faker import Faker

from models.database import create_db, Session
from models.lesson import Lesson
from models.student import Student
from models.group import Group


def _load_fake_data(session):
    lessons_names = ['Математика', 'Программирование', 'Философия', 'Алгоритмика', '']