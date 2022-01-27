
_HELLO_WORLD = 'Hello World'


def package_code_1():
    """

    :return:
    """
    return 42


def count_odd():
    """

    :return:
    """
    _count = 1
    while True:
        yield _count
        _count += 2


def test_yield(data):
    """

    :return:
    """
    for _data in data:
        yield _data
