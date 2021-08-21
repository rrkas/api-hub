from collections import OrderedDict
from typing import List

from app.models import Documentation

docs: List[Documentation] = []


def load_docs():
    from app.prog import get_prog_docs

    docs.extend(get_prog_docs())


load_docs()


def get_docs():
    categories = OrderedDict()
    for doc in docs:
        if doc.category not in categories.keys():
            categories[doc.category] = [doc]
        else:
            categories[doc.category].append(doc)
    return categories
