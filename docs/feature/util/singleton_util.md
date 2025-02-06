# SingletonUtil 单例工具类

## 简介
`SingletonUtil` 模块提供了两种单例模式的实现方式：线程安全的单例模式和异步安全的单例模式。这两种模式分别适用于多线程环境和异步编程环境，确保类的实例在整个应用程序中唯一。

## 单例模式实现

### 1. 线程安全的单例模式 (`SingletonType`)
`SingletonType` 是一个元类，用于创建线程安全的单例类。它使用 `threading.RLock` 来确保在多线程环境下只有一个实例被创建。

#### 使用方法
要使某个类成为线程安全的单例类，只需将 `SingletonType` 作为该类的元类即可。

```python
from spikify import SingletonType

class MySingletonClass(metaclass=SingletonType):
    def __init__(self, value=None):
        self.value = value

# 创建实例
instance1 = MySingletonClass("first")
instance2 = MySingletonClass("second")

print(instance1 is instance2)  # 输出: True
print(instance1.value)         # 输出: first
```


### 2. 异步安全的单例模式 (`AsyncSingletonType`)
`AsyncSingletonType` 是一个元类，用于创建异步安全的单例类。它使用 `asyncio.Lock` 来确保在异步编程环境中只有一个实例被创建。

#### 使用方法
要使某个类成为异步安全的单例类，只需将 `AsyncSingletonType` 作为该类的元类即可。

```python
from spikify import AsyncSingletonType
import asyncio

class MyAsyncSingletonClass(metaclass=AsyncSingletonType):
    def __init__(self, value=None):
        self.value = value

async def create_instance(value):
    instance = MyAsyncSingletonClass(value)
    print(f"Instance created with value: {value}")
    return instance

async def main():
    task1 = asyncio.create_task(create_instance("first"))
    task2 = asyncio.create_task(create_instance("second"))

    instance1 = await task1
    instance2 = await task2

    print(instance1 is instance2)  # 输出: True
    print(instance1.value)         # 输出: first

asyncio.run(main())
```


## 注意事项
- `SingletonType` 适用于多线程环境，确保线程安全。
- `AsyncSingletonType` 适用于异步编程环境，确保异步安全。
- 在使用 `AsyncSingletonType` 时，请确保正确处理异步上下文，并使用 `await` 关键字来调用构造函数。

## 示例代码
### 线程安全的单例模式示例
```python
from spikify import SingletonType

class MySingletonClass(metaclass=SingletonType):
    def __init__(self, value=None):
        self.value = value

# 创建实例
instance1 = MySingletonClass("first")
instance2 = MySingletonClass("second")

print(instance1 is instance2)  # 输出: True
print(instance1.value)         # 输出: first
```


### 异步安全的单例模式示例
```python
from spikify import AsyncSingletonType
import asyncio

class MyAsyncSingletonClass(metaclass=AsyncSingletonType):
    def __init__(self, value=None):
        self.value = value

async def create_instance(value):
    instance = MyAsyncSingletonClass(value)
    print(f"Instance created with value: {value}")
    return instance

async def main():
    task1 = asyncio.create_task(create_instance("first"))
    task2 = asyncio.create_task(create_instance("second"))

    instance1 = await task1
    instance2 = await task2

    print(instance1 is instance2)  # 输出: True
    print(instance1.value)         # 输出: first

asyncio.run(main())
```
