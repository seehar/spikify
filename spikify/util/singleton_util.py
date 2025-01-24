from asyncio import Lock
from threading import RLock


class SingletonType(type):
    """
    利用线程锁实现的单例类
    """

    single_lock = RLock()

    def __call__(cls, *args, **kwargs):
        with SingletonType.single_lock:
            if not hasattr(cls, "_instance"):
                cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)

        return cls._instance


class AsyncSingletonType(type):
    """
    利用协程锁实现的单例类
    """

    single_lock = Lock()

    def __call__(cls, *args, **kwargs):
        with SingletonType.single_lock:
            if not hasattr(cls, "_instance"):
                cls._instance = super(AsyncSingletonType, cls).__call__(*args, **kwargs)

        return cls._instance
