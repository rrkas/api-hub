from app.implementation import *
from app.models import *
from .basic import *


def get_math_docs():
    data = []
    data += basic_docs()
    return data