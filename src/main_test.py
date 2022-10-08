
import main_test_package as mtp

from main_test_package.package_code import test_yield


def main_hank():
    """

    :return:
    """
    # print(main_test_package.pc1())
    print(mtp.pc1())
    print(mtp._HELLO_WORLD)

    _data = [
        'Testing1',
        'Testing2',
        'Testing3',
        'Testing4',
        'Testing5',
        'Testing6',
    ]

    _generator = mtp.test_yield(_data)
    print("get an element from yield")
    print(next(_generator))
    print(next(_generator))

    print("get all the elements from the list")
    for _d in test_yield(_data):
        print(_d)

    print("get an element from yield")
    print(next(_generator))

    _g1 = test_yield(_data)
    _g2 = test_yield(_data)

    print(id(_g1))
    print(id(_g2))


if __name__ == '__main__':
    main_hank()
