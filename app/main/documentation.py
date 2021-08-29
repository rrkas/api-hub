from collections import OrderedDict
from typing import List

from app.models import Documentation

docs: List[Documentation] = []


def load_docs():
    from app.prog import get_prog_docs

    docs.extend(get_prog_docs())


load_docs()


def find_doc_with_id(id):
    t = [d for d in docs if d.doc_html_id == id]
    return t[0] if len(t) > 0 else None


def get_docs():
    subjects = OrderedDict()
    for doc in docs:
        if doc.subject not in subjects.keys():
            subjects[doc.subject] = OrderedDict()
            subjects[doc.subject][doc.category] = [doc]
        elif doc.category not in subjects[doc.subject].keys():
            subjects[doc.subject][doc.category] = [doc]
        else:
            subjects[doc.subject][doc.category].append(doc)
    for subject, categories in subjects.items():
        for category, doc_list in categories.items():
            doc_list.sort(key=lambda x: x.name)
    return subjects
