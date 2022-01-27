import logging

from typing import (
    Any,
    List
)

from .exceptions import (
    HDSKeyCollisionError,
    HDSKeyError
)


HDS_DICT_INITIAL_KEYS = 100
HDS_DICT_INCREMENT_KEYS = 100
HDS_DICT_COLLISION_MULTIPLIER = 50
HDS_FREE_LIMIT = .5


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class HFCDictionary:
    """
    - hash table
    - key lookup, quick.

    sorted list (key_hash, value)
    array[n items] = value
    l = [1, 2, 3, 4]
    l[3]

    l[pos] = 1
    key => hash % len(list)
    20 elements -> 40 buckets




    """

    def __init__(self, initial_keys=HDS_DICT_INITIAL_KEYS, increment_keys=HDS_DICT_INCREMENT_KEYS, free_limit=HDS_FREE_LIMIT):
        """

        """
        logger.warning("init HFCDictionary")
        self._array = _create_empty_array(initial_keys)
        self._buckets_used = 0
        self._initial_keys = initial_keys
        self._increment_keys = increment_keys
        self._free_limit = free_limit


    def __getitem__(self, key):
        """

        :param item:
        :return:
        """
        print(f"__getitem__ {key}")
        _array = self._array

        _bucket = _get_hash_bucket_value(key, len(_array))
        _data = _array[_bucket]

        if not _data:
            raise HDSKeyError(f'KeyError while retrieving {key}')

        if key != _data[0]:
            raise HDSKeyCollisionError(f'key {key} collided with {_data[0]}')

        return _data[1]


    def __setitem__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        _array = self._array

        _bucket = _get_hash_bucket_value(key, len(_array))
        _data = _array[_bucket]
        if not _data:
            _data = key, value
            self._buckets_used += 1

            if self._buckets_used / len(_array) > self._free_limit:
                print("breeched buckets free, resize")
                self._array = self._resize(_array, len(_array) + self._increment_keys)
                _array = self._array
                _bucket = _get_hash_bucket_value(key, len(self._array))
        else:
            # check for key collision
            if _data[0] != key:
                new_array = self._resize(_array, len(_array) + self._increment_keys * HDS_DICT_COLLISION_MULTIPLIER)
                _bucket = _get_hash_bucket_value(key, len(new_array))
                _test_data = new_array[_bucket]
                if _test_data:
                    raise HDSKeyCollisionError(f'key {key} collided with {_data[0]} even after resize')
                else:
                    self._array = new_array
                    self._array[_bucket] = key, value
                    return
            _data = key, value
        _array[_bucket] = _data

    def _resize(self, existing_array, new_size):
        new_array = _create_empty_array(new_size)
        for _data in existing_array:
            if _data:
                _bucket = _get_hash_bucket_value(_data[0], len(new_array))
                new_array[_bucket] = _data[0], _data[1]
        return new_array

    def keys(self):
        """
        Dump the keys currently in the dictionary

        :return:
        """
        return [_data[0] for _data in self._array if _data]

    def values(self):
        """
        Dump the values currently in the dictionary

        :return:
        """
        return [_data[1] for _data in self._array if _data]


def _create_empty_array(size: int) -> List:
    """
    Create an empty array of size

    :param size:
    :return:
    """

    return [None] * size


def _get_hash_bucket_value(key: Any, array_len: int):
    """

    :param key:
    :param array_len:
    :return:
    """
    return hash(key) % array_len

