import pytest

from spikify.util.singleton_util import SingletonType, AsyncSingletonType


class TestSingletonType:
    def test_first_call_creates_new_instance(self):
        class MyClass(metaclass=SingletonType):
            pass

        instance = MyClass()
        assert isinstance(instance, MyClass)

    def test_second_call_returns_same_instance(self):
        class MyClass(metaclass=SingletonType):
            pass

        instance1 = MyClass()
        instance2 = MyClass()
        assert instance1 is instance2

    def test_different_classes_have_different_instances(self):
        class MyClass1(metaclass=SingletonType):
            pass

        class MyClass2(metaclass=SingletonType):
            pass

        instance1 = MyClass1()
        instance2 = MyClass2()
        assert instance1 is not instance2


class TestAsyncSingletonType:
    def test_first_call_creates_new_instance(self):
        class MyAsyncClass(metaclass=AsyncSingletonType):
            pass

        instance = MyAsyncClass()
        assert isinstance(instance, MyAsyncClass)

    def test_second_call_returns_same_instance(self):
        class MyAsyncClass(metaclass=AsyncSingletonType):
            pass

        instance1 = MyAsyncClass()
        instance2 = MyAsyncClass()
        assert instance1 is instance2

    def test_different_classes_have_different_instances(self):
        class MyAsyncClass1(metaclass=AsyncSingletonType):
            pass

        class MyAsyncClass2(metaclass=AsyncSingletonType):
            pass

        instance1 = MyAsyncClass1()
        instance2 = MyAsyncClass2()
        assert instance1 is not instance2

    @pytest.mark.asyncio
    async def test_async_thread_safety(self):
        class MyAsyncClass(metaclass=AsyncSingletonType):
            pass

        async def create_instance():
            return MyAsyncClass()

        instance1 = await create_instance()
        instance2 = await create_instance()
        assert instance1 is instance2
