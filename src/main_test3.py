import logging

from hfcdatastructures.hfcdict import HFCDictionary


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.propogate = True
logger.setLevel(logging.INFO)


def main():
    """

    :return:
    """
    logger.info('startup')
    test_dict = HFCDictionary()
    test_dict['HFC'] = 'Andover'
    test_dict['AB'] = 'Eden Prairie'

    print(test_dict._array)
    print(test_dict.keys())
    print(test_dict.values())

    test_dict = HFCDictionary()
    for _count in range(100):
        test_dict[f'testing{_count}'] = _count
        if _count == 50:
            print(test_dict._array)
    print(test_dict._array)


if __name__ == '__main__':
    main()
