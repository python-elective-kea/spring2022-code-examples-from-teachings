from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()
