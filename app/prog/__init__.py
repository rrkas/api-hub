from app.prog.algos import (
    pre_in_post_docs,
    sorting_docs,
    searching_docs,
    basic_docs,
    advanced_docs,
)


def get_prog_docs():
    data = []
    data += basic_docs()
    data += sorting_docs()
    data += searching_docs()
    data += pre_in_post_docs()
    data += advanced_docs()

    return data
