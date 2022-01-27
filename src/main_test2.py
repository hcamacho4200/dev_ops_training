import time

from memoization import cached

def main():
    """

    :return:
    """

    print(long_running_init_function('app1'))
    print(long_running_init_function('app2'))
    print(long_running_init_function('app3'))

    print('Things Are Initalized')
    print(long_running_init_function('app1'))
    print(long_running_init_function('app2'))
    print(long_running_init_function('app3'))

    print("init a new one")
    print(long_running_init_function('app4'))

    print('Things Are Initalized')
    print(long_running_init_function('app1'))
    print(long_running_init_function('app2'))
    print(long_running_init_function('app3'))
    print(long_running_init_function('app4'))


class MultiFabricMetrics():
    def __init__(self, app):
        """

        """
        self.app = app
        time.sleep(1)
        print('wait')



@cached(ttl=86400)
def long_running_init_function(app):
    """

    :param app:
    :return:
    """

    return MultiFabricMetrics(app)





if __name__ == '__main__':
    main()



