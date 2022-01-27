from typing import (
    List
)
def main():
    """Entry point for data structures demo

    :return:
    """
    print("Data Structures")
    # demo_lists()
    # demo_stack()
    # demo_tuple()
    # demo_set()
    demo_dictionary()

def demo_lists():
    """
    A list of very much like an Array that contains various types of data
    - can be int, strings, class objects, really anything, even lists

    :return:
    """
    a_list = []
    b_list = list()

    print(a_list)
    print(b_list)

    a_list = [1, 2, 3, 4, 5]
    # b_list = list('a', 'b')  # invalid
    b_list = list(a_list)

    print(id(a_list), a_list)
    print(id(b_list), b_list)

    class ListClassObjA:
        def __init__(self, number):
            self._number = number

        def __repr__(self):
            return f'ListClassObjA: {self._number}'

    class ListClassObjB:
        def __init__(self, string):
            self._string = string

        def __repr__(self):
            return f'ListClassObjB: {self._string}'

    c_list = [
        ListClassObjA(1),
        ListClassObjA(2),
        ListClassObjA(3),
        ListClassObjA(4),
        ListClassObjA(5),
    ]

    print(id(c_list), c_list)

    c_list.append(ListClassObjB("Test1"))
    c_list.append(ListClassObjB("Test2"))

    print(id(c_list), c_list)

    d_list = [
        a_list,
        b_list
    ]


    print(id(d_list), d_list)

    # iterating a list
    for _list_element in c_list:
        print(_list_element)

    # list comprehension
    # create a new list using an algo.
    list_comprehension_a = [ _list_element for _list_element in a_list if int(_list_element) > 3]
    print(list_comprehension_a)

    # slices
    print(a_list[::])       # all the elements
    print(a_list[::-1])     # all the elements reversed
    print(a_list[3:4])      # start at 3rd and stop at 4th
    print(a_list[3:5])
    print(a_list[4])




def demo_stack():
    """
    Last in First Out

    :return:
    """
    try:
        stack = []
        stack.append(1)
        stack.append(2)
        stack.append(3)
        stack.append(4)
        stack.append(5)
        print(stack)
        print(stack.pop())
        print(stack.pop())
        stack.append('a')
        stack.append('b')
        print(stack)
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())
    except IndexError:
        print("Ha... no more elements to extract")

def demo_tuple():
    """
    A touple is a list like structure, but is immutable
    - use commas
    - nested tuples must use ()
    :return:
    """

    a_tuple = 1, 2, 3, 4, 5
    print(a_tuple)
    print(a_tuple[3:4])
    print(a_tuple[3])
    # a_tuple[3] = 5  # this will not work, compile time error

    print()
    for _tuple_value in a_tuple:
        print(_tuple_value)

    single_tuple = 'I am single',
    print(single_tuple)

def demo_set():
    """
    Unordered and Unique structure
    - Like a dictionary but with no values, only keys

    :return:
    """
    a_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    a_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}

    print(a_list)
    print(a_set)

    a_set.add(5)
    print(a_set)

    a_set.add(6)
    print(a_set)

    a_set = {1, 2, 3, 4, 5}
    b_set = {5, 6, 7, 8, 9}

    print(b_set - a_set)  # in b but not in a
    print(a_set - b_set)  # in a but not in b
    print(a_set | b_set)  # in a OR b
    print(a_set & b_set)  # in a AND b
    print(a_set ^ b_set)  # in a AND b but not in both

    # iterate
    for _set_value in a_set ^ b_set:
        print(_set_value)

    # set comprehension
    set_comprehension = { _set_value for _set_value in b_set ^ a_set }
    print(set_comprehension)

def demo_dictionary():
    """
    A dictionary is a set of keys,value pairs.
    - unique key
    - key insert order is not maintained
    :return:
    """

    a_dict = dict()
    b_dict = {}

    print(a_dict)
    print(b_dict)

    a_dict = {
        1: 'a_test1',
        2: 'a_test2',
        3: 'a_test3',
        4: 'a_test4',
        5: 'a_test5'
    }
    print(a_dict)

    b_dict = {
        5: 'b_test5',
        6: 'b_test6',
        7: 'b_test7',
        8: 'b_test8',
        9: 'b_test9'
    }

    print(a_dict | b_dict)

    # iterator
    for _key, _value in (a_dict | b_dict).items():
        print(f'{_key} {_value}')

    # dictionary comprehension
    _dict_comprehension = {_key: _value for _key, _value in (a_dict | b_dict).items() if _key > 3 and _key < 8}
    print(_dict_comprehension)

    # attempting to get a key that does not exist throws an exception
    try:
        print(_dict_comprehension[100])
    except KeyError as e:
        print("Ha, key error missing key was", e)

    # test if key is present:
    if 100 not in _dict_comprehension:
        print("key is missing, adding")
        _dict_comprehension[100] = 'New Value'

    print(_dict_comprehension)


if __name__ == '__main__':
    main()