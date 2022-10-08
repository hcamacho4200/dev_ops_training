import pytest

from src.printf import (
    __printf,
    _parse_format,
    MODE_DELIMITER,
    MODE_FLAG,
    MODE_WIDTH,
    MODE_PRECISION_DOT,
    MODE_PRECISION,
    MODE_LENGTH,
    MODE_SPECIFIER,
    FLAG_VALUE,
    FLAG_CHAR,
    FLAG_LEFT_JUSTIFY,
    FLAG_PRINT_POSITIVE,
    FLAG_SPACE,
    FLAG_PRECEDE_ZERO,
    FLAG_LEFT_PAD,
    WIDTH_IN_ARGS,
)


def test___printf_arguments():
    """
    - check to make sure a non string argument raises exception

    :return:
    """
    with pytest.raises(ValueError):
        __printf((1, 'testing 1 2 3 4'))


def test___parse_format():
    """

    :return:
    """

    print()

    #
    # test for various flags
    #

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%-10.*d\n', (1, 2))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 8
    assert _argument_pos == 1
    assert _flags == 0 | FLAG_LEFT_JUSTIFY[FLAG_VALUE]
    assert _width == 10
    assert _precision == 1

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%-+10.*d\n', (1, 2))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 9
    assert _argument_pos == 1
    assert _flags == 0 | FLAG_LEFT_JUSTIFY[FLAG_VALUE] | FLAG_PRINT_POSITIVE[FLAG_VALUE]
    assert _width == 10
    assert _precision == 1

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%-+ 10.*d\n', (1, 2))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 10
    assert _argument_pos == 1
    assert _flags == 0 | FLAG_LEFT_JUSTIFY[FLAG_VALUE] | FLAG_PRINT_POSITIVE[FLAG_VALUE] | FLAG_SPACE[FLAG_VALUE]
    assert _width == 10
    assert _precision == 1

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%-+ #10.*d\n', (1, 2))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 11
    assert _argument_pos == 1
    assert _flags == 0 | FLAG_LEFT_JUSTIFY[FLAG_VALUE] | FLAG_PRINT_POSITIVE[FLAG_VALUE] | FLAG_SPACE[FLAG_VALUE] | FLAG_PRECEDE_ZERO[FLAG_VALUE]
    assert _width == 10
    assert _precision == 1

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%-+ #010.*d\n', (1, 2))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 12
    assert _argument_pos == 1
    assert _flags == 0 | FLAG_LEFT_JUSTIFY[FLAG_VALUE] | FLAG_PRINT_POSITIVE[FLAG_VALUE] | FLAG_SPACE[FLAG_VALUE] | FLAG_PRECEDE_ZERO[FLAG_VALUE] | FLAG_LEFT_PAD[FLAG_VALUE]
    assert _width == 10
    assert _precision == 1

    #
    # Test Width
    #

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%10d\n', (1))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 5
    assert _argument_pos == 0
    assert _flags == 0
    assert _width == 10
    assert _precision == None

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%*d\n', (10, 1))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 4
    assert _argument_pos == 1
    assert _flags == 0
    assert _width == 10
    assert _precision == None

    #
    # Test Precision
    #

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%.5e\n', (1))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 5
    assert _argument_pos == 0
    assert _flags == 0
    assert _width is None
    assert _precision == 5

    _format_pos, _argument_pos, _flags, _width, _precision = _parse_format('%.*e\n', (5, 1))
    print(_format_pos, _argument_pos, _flags, _width, _precision)
    assert _format_pos == 5
    assert _argument_pos == 1
    assert _flags == 0
    assert _width is None
    assert _precision == 5
