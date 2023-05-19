import dataclasses
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Subjects(Enum):
    MATH = 'Maths'
    ART = 'Art'
    ACCOUNTING = 'Accounting'
    SOCIAL_STUDIES = 'Social Studies'


class Hobbies(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: list[Gender]
    user_number: int
    birthday: date
    subject: list[Subjects]
    hobby: list[Hobbies]
    image: str
    address: str
    state: str
    city: str


student = User(first_name='Meerim', last_name='Sabyt',
              email='skmeerim1999@gmail.com', gender = Gender.FEMALE,
              user_number ='0554803097', birthday=date(1999, 10,10),subject=[Subjects.MATH],hobby= Hobbies.READING,
              image='totoro.jpg', address='str Abd 123', state='NCR', city='Delhi')
