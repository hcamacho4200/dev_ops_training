import copy
import sys

from typing import (
    Tuple
)

MODE_DELIMITER = 2 ** 0
MODE_FLAG = 2 ** 1
MODE_WIDTH = 2 ** 2
MODE_PRECISION_DOT = 2 ** 3
MODE_PRECISION = 2 ** 4
MODE_LENGTH = 2 ** 5
MODE_SPECIFIER = 2 ** 6

FLAG_VALUE = 0
FLAG_CHAR = 1
FLAG_LEFT_JUSTIFY = 2 ** 7, '-'
FLAG_PRINT_POSITIVE = 2 ** 8, '+'
FLAG_SPACE = 2 ** 9, ' '
FLAG_PRECEDE_ZERO = 2 ** 10, '#'
FLAG_LEFT_PAD = 2 ** 11, '0'

WIDTH_IN_ARGS = 2 ** 12, '*'

PRECISION_DOT = 2 ** 13, '.'
PRECISION_IN_ARGS = 2 ** 14, '*'

RESERVED_CHARS = 'diuoxXeEgGaAcsphlL.'


def printf(*args):
    """

    :return:
    """
    sys.stdout.write(__printf(args))


def __printf(args: Tuple) -> str:
    """Implementation of printf for C in python
    - need a format string that handles the % syntax and normal characters
    - need variable number of arguments to satisify formatting arguments
    - need to parse the format sting, and figure out a lot of things, likely needs to be pluggable somehow
    - %[flags][width][.precision][length]specifier
        - flags
            - left-justify, right justify is default
            + preceed the result with a + or -, default only only negative numbers are preceeded by a -
            [space] no sign is outputed
            # used with o, x or X preceeds values with 0, with e, E or F forces a decimal point with g or G result is the same with e, E with trailing zeros not removed.  # noqa: E501
            0 left pads the number with zeros instead of spaces
        - width
            [number] minimum number of characters to print, will be padded with spaces
            * specified in the argument preceeding the argument to be formatted
        - precision
            .number d, i, o, u, x, X specifies the number of digitals to be written.
                e, E, f specifies the number of digits after the decimal point
                g, G specifies the maximum number of siginificant digits to print
                s, the maximum number of characters to print
                c no effect
                default of 1
                if specified with no number, assumed to be zero.
            .* the specification is in the argument preceding the formated argument
        - length
            h i, d, o, u, x, X interpreted as short int or unsigned short int
            l i, d, u, x, X as a long int, or unsigned long int, for c and s handled as a double wide character
            L e, E, f, g, G used as long double
        - specifier d, i int
                    u unsigned int
                    o octal
                    x, X unsigned hex
                    e, E Floating point
                    g, G shortest representitation
                    a, A hexadecimal Floating point
                    c character
                    s string
                    P Pointer Address



    :param format:
    :param args:
    :return:
    """
    if type(args[0]) != str:
        raise ValueError('1st argument must be a string')

    _output = ''
    _format_string = copy.copy(args[0])
    _format_pos = 0
    _argument_pos = 1
    while _format_pos < len(_format_string):
        _pos_ch = _format_string[_format_pos]
        if _pos_ch == '%':
            print("special char found parse")
            _parse_format(_format_string[_format_pos:], args[_argument_pos:])
        else:
            _output += _pos_ch

        print(_format_string[_format_pos])
        _format_pos += 1

    return _output


def _parse_format(format_string, args):
    """Parse the incoming format_string along with the args and return the flags and offsets

    :param format_string:
    :param args:
    :return:
    """
    MODE_DELIMITER = 2**0
    MODE_FLAG = 2**1
    MODE_WIDTH = 2**2
    MODE_PRECISION_DOT = 2**3
    MODE_PRECISION = 2**4
    MODE_LENGTH = 2**5

    FLAG_VALUE = 0
    FLAG_CHAR = 1
    FLAG_LEFT_JUSTIFY = 2**7, '-'
    FLAG_PRINT_POSITIVE = 2**8, '+'
    FLAG_SPACE = 2**9, ' '
    FLAG_PRECEDE_ZERO = 2**10, '#'
    FLAG_LEFT_PAD = 2**11, '0'

    WIDTH_IN_ARGS = 2**12, '*'

    PRECISION_DOT = 2**13, '.'
    PRECISION_IN_ARGS = 2**14, '*'

    RESERVED_CHARS = 'diuoxXeEgGaAcsphlL.'

    _mode = MODE_DELIMITER
    _flags = 0
    _width = None
    _width_string = ''
    _precision = None
    _precision_string = ''

    _format_pos = 0
    _argument_pos = 0
    while _format_pos < len(format_string):
        _pos_ch = format_string[_format_pos]

        if _mode == MODE_DELIMITER:
            if _pos_ch != '%':
                raise ValueError(f'problem with format string {format_string} missing %')
            else:
                _mode = MODE_FLAG
        elif _mode == MODE_FLAG:
            if _pos_ch == FLAG_LEFT_JUSTIFY[FLAG_CHAR]:
                _flags |= FLAG_LEFT_JUSTIFY[FLAG_VALUE]
            elif _pos_ch == FLAG_PRINT_POSITIVE[FLAG_CHAR]:
                _flags |= FLAG_PRINT_POSITIVE[FLAG_VALUE]
            elif _pos_ch == FLAG_SPACE[FLAG_CHAR]:
                _flags |= FLAG_SPACE[FLAG_VALUE]
            elif _pos_ch == FLAG_PRECEDE_ZERO[FLAG_CHAR]:
                _flags |= FLAG_PRECEDE_ZERO[FLAG_VALUE]
            elif _pos_ch == FLAG_LEFT_PAD[FLAG_CHAR]:
                _flags |= FLAG_LEFT_PAD[FLAG_VALUE]
            else:
                _mode = MODE_WIDTH
                continue
        elif _mode == MODE_WIDTH:
            if _pos_ch == WIDTH_IN_ARGS[FLAG_CHAR]:
                _width = int(args[_argument_pos])
                _argument_pos += 1
                _mode = MODE_PRECISION
            else:
                if _pos_ch not in RESERVED_CHARS:
                    _width_string += _pos_ch
                else:
                    if len(_width_string) > 0:
                        _width = int(_width_string)
                    _mode = MODE_PRECISION_DOT
                    continue
        elif _mode == MODE_PRECISION_DOT:
            if _pos_ch != PRECISION_DOT[FLAG_CHAR]:
                _mode = MODE_LENGTH
            else:
                _mode = MODE_PRECISION
        elif _mode == MODE_PRECISION:
            if _pos_ch == PRECISION_IN_ARGS[FLAG_CHAR]:
                _precision = int(args[_argument_pos])
                _argument_pos += 1
                _mode = MODE_LENGTH
            else:
                if _pos_ch not in RESERVED_CHARS:
                    _precision_string += _pos_ch
                else:
                    if len(_precision_string) > 0:
                        _precision = int(_precision_string)
                        _mode = MODE_LENGTH
                        continue

        _format_pos += 1

    return _format_pos, _argument_pos, _flags, _width, _precision
