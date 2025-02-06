# 快速上手

## 简介

`Spikify` 是一个旨在提升开发效率的工具包，提供了多种实用的功能模块，如日志记录、线程管理、字符串和哈希工具等。本文档将引导你快速上手 `Spikify`，并展示如何使用其核心功能。

## 使用示例

### 日志记录器（LoggerBuilder）

`LoggerBuilder` 提供了灵活的日志配置和链式调用接口，支持将日志输出到标准输出和文件中。


**使用示例：**
```python
from spikify.builder.logger_builder import LoggerBuilder

# 创建并配置日志记录器
logger = (
    LoggerBuilder()
    .add_sys_stdout(level="DEBUG")
    .add_file(
        file_path="app.log",
        level="INFO",
        rotation="10 MB",  # 日志文件大小超过 10MB 时轮转
        retention="7 days",  # 保留最近 7 天的日志文件
        compression="zip"  # 压缩旧的日志文件
    )
    .get_logger()
)

# 使用日志记录器记录日志
logger.debug("这是一个调试信息")
logger.info("这是一个普通信息")
logger.warning("这是一个警告信息")
logger.error("这是一个错误信息")
```


### 线程管理器（ThreadManager）
`ThreadManager` 提供了对线程池的简单封装，方便管理和调度多线程任务。

**使用示例：**
```python
from spikify.manager.thread_manager import ThreadManager

def task(n):
    return n * n

# 创建线程管理器实例
thread_manager = ThreadManager()

# 提交任务
future = thread_manager.submit(task, 5)

# 获取任务结果
result = future.result()
print(f"任务结果: {result}")
```


### 字符串工具类（StringUtil）
`StringUtil` 提供了生成随机字符串的功能，支持生成不同类型的随机字符串。

**使用示例：**
```python
from spikify.util.string_util import StringUtil

# 生成指定长度的随机字母数字字符串
random_alphanumeric = StringUtil.create_random_alphanumeric(10)
print(f"随机字母数字字符串: {random_alphanumeric}")

# 生成指定长度的随机字母字符串（仅包含大小写字母）
random_letters = StringUtil.create_random_letters(8)
print(f"随机字母字符串: {random_letters}")

# 生成指定长度的随机小写字母字符串
random_lowercase = StringUtil.create_random_lowercase_letters(6)
print(f"随机小写字母字符串: {random_lowercase}")

# 生成指定长度的随机大写字母字符串
random_uppercase = StringUtil.create_random_uppercase_letters(4)
print(f"随机大写字母字符串: {random_uppercase}")
```


### MD5 工具类（MD5Util）
`MD5Util` 提供了生成 MD5 哈希值的功能，支持从字符串和字典生成哈希值。

**使用示例：**
```python
from spikify.util.md5_util import MD5Util

# 从字符串生成 MD5 哈希值
string_hash = MD5Util.from_str("Hello, World!")
print(f"字符串 'Hello, World!' 的 MD5 哈希值: {string_hash}")

# 从字典生成 MD5 哈希值
dict_data = {"name": "Alice", "age": 30, "city": "New York"}
dict_hash = MD5Util.from_dict(dict_data)
print(f"字典 {dict_data} 的 MD5 哈希值: {dict_hash}")
```


### 单例工具类（SingletonType 和 AsyncSingletonType）
`SingletonType` 和 `AsyncSingletonType` 提供了单例模式的支持，适用于需要全局唯一实例的场景。

**使用示例：**
```python
from spikify.util.singleton_util import SingletonType

class MySingleton(metaclass=SingletonType):
    def __init__(self):
        self.value = "Singleton Instance"

# 创建单例实例
singleton1 = MySingleton()
singleton2 = MySingleton()

print(singleton1 is singleton2)  # 输出: True
```


## 文档与资源
- **官方文档**: [https://seehar.github.io/spokify/](https://seehar.github.io/spokify/)
- **GitHub 仓库**: [https://github.com/seehar/spokify](https://github.com/seehar/spokify)
