import sys


def hfc_grep():
    """Main entrypoint for hfc_grep
    - need to work like grep
    - search string that look in each line, when matched prints.
    - input_filename a file to search


    :return:
    """

    if '--version' in sys.argv:
        version = True
    else:
        version = False

    if version:
        print("HFCGrep by hcamacho")
        print("version .001beta")
        exit(0)

    if len(sys.argv) < 2:
        raise ValueError('Not enough arguments')

    try:
        input_filename = sys.argv[2]
    except IndexError:
        input_filename = None

    search_string = sys.argv[1]
    if not search_string:
        raise ValueError('Required search_string')

    input_stream = None

    if not sys.stdin.isatty():
        input_stream = sys.stdin
        if input_filename:
            raise ValueError('Choose input PIPE or input filename, not both')
    else:
        try:
            if not input_filename:
                raise ValueError('Requires input_filename')

            input_stream = open(input_filename, 'r')
        except FileNotFoundError:
            raise FileNotFoundError(f'Unable to open file {input_filename}')

    for _line in input_stream:
        if search_string in _line:
            print(_line.strip())


if __name__ == '__main__':
    try:
        hfc_grep()
    except ValueError as e:
        print(e)
    except Exception:
        import traceback
        print(traceback.format_exc())
