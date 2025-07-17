from django.db.models import IntegerChoices


class Levels(IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


class UserTypes(IntegerChoices):
    INSTRUCTOR = 1, 'Instructor'
    STUDENT = 2, 'Student'