import os

from hfcdatastructures.hfcdict import (
    HFCDictionary,
    HDS_DICT_INITIAL_KEYS,
    _create_empty_array,
    _get_hash_bucket_value
)


def test_hfcdict_get():
    """

    :return:
    """

    # setup
    test_dict = HFCDictionary()
    assert len(test_dict._array) == HDS_DICT_INITIAL_KEYS
    actual = test_dict['test'] = 42

    actual = test_dict['test']

    assert actual == 42


def test_hfcdict_set():
    """

    :return:
    """

    test_dict = HFCDictionary()
    assert len(test_dict._array) == HDS_DICT_INITIAL_KEYS
    test_dict['test'] = 42
    assert 'test', 42 in test_dict._array


def test_hfc_dict__create_empty_array():
    """

    :return:
    """

    actual = _create_empty_array(10)
    print(len(actual))
    assert len(actual) == 10

    actual = _create_empty_array(0)
    print(len(actual))
    print(actual)
    assert len(actual) == 0


def test_hfc_dict__get_hash_bucket_value():
    """

    :return:
    """
    os.environ['PYTHONHASHSEED'] = "0"

    assert _get_hash_bucket_value("TESTING", 100) == 13
    assert _get_hash_bucket_value("TESTING1", 100) == 6
    assert _get_hash_bucket_value("TESTING2", 100) == 67


def test_hfcdict_init():
    """

    :return:
    """
    print("hello")
    test_dict = HFCDictionary()
    print(type(test_dict))

    assert type(test_dict) == HFCDictionary
