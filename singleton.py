from threading import Lock, Thread


class SingletonMeta(type):
    _instance = None
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)

        return cls._instance


class MultiThreadsSingleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'MultiThreadsSingleton: {self.value}'


def test_multi_threads_singleton(value):
    singleton = MultiThreadsSingleton(value)
    print(singleton)


class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls._instance = object.__new__(cls)

        return cls.__instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    process1 = Thread(target=test_multi_threads_singleton, args=("FOO",))
    process2 = Thread(target=test_multi_threads_singleton, args=("BAR",))
    process1.start()
    process2.start()
