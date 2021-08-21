from app.prog.algos import pre_in_post_docs, sorting_docs


def get_prog_docs():
    data = []
    data += pre_in_post_docs()
    data += sorting_docs()

    return data
