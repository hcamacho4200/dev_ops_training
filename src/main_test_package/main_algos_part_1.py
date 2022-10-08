_data = [
    ('this', 9),
    ('that', 2),
    ('then', 3),
    ('this', 1),
    ('that', 1),
    ('that', 6)
]


def main():
    pass
    # iter_1()
    # iter_2()
    # iter_3()
    iter_4()


def iter_1():
    for _k, _v in _data:
        print(_k, _v)


def iter_2():
    d = {}
    for _k, _v in _data:
        if _k not in d:
            d[_k] = []
        d[_k].append(_v)
    print(d)


def iter_3():
    d = {}
    for _k, _v in _data:
        d[_k] = _v
    print(d)


def iter_4():
    d = {}
    for _k, _v in _data:
        if _k not in d:
            d[_k] = []
        d[_k].append(_v)

    for _k, _list in d.items():
        print(f'processing {_k}')
        for _item in _list:
            print(f'  executing item {_item}')

    print()

    for _k, _list in d.items():
        print("processing _k")
        for _item in sorted(_list):
            print(f'  executing item {_item}')


if __name__ == '__main__':
    main()
