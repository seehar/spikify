### LoggerBuilder

#### 简介

`LoggerBuilder` 是一个用于配置和构建日志记录器的工具类，基于 `loguru`
库。它提供了链式调用的方法来添加不同的日志输出目标（如标准输出、文件等），并最终获取一个配置好的日志记录器实例。

#### 安装依赖

确保你已经安装了 `loguru` 库，可以通过以下命令安装：

```bash
pip install loguru
```

#### 使用示例

以下是一个简单的使用示例，展示了如何配置并获取一个日志记录器实例：

```python
from spikify.builder.logger_builder import LoggerBuilder

logger = (
    LoggerBuilder()
    .add_sys_stdout(level="DEBUG")
    .add_file(
        file_path="app.log",
        level="INFO",
        rotation="10 MB",  # 日志文件大小超过 10MB 时轮转
        retention="7 days",  # 保留最近 7 天的日志文件
        compression="zip",  # 压缩旧的日志文件
    )
    .get_logger()
)

# 使用日志记录器记录日志
logger.debug("这是一个调试信息")
logger.info("这是一个普通信息")
logger.warning("这是一个警告信息")
logger.error("这是一个错误信息")
```

#### 方法说明

##### `__init__()`

- **描述**: 初始化 `LoggerBuilder` 实例，并移除默认的日志处理器。
- **返回值**: 无

##### `add_sys_stdout`

- **描述**: 添加系统标准输出作为日志输出目标。
- **参数**:

| 参数名          | 类型                 | 默认值              | 描述   |
|--------------|--------------------|------------------|------|
| `level`      | `str` 或 `int`      | `"DEBUG"`        | 日志级别 |
| `log_format` | `str` 或 `callable` | `DEFAULT_FORMAT` | 日志格式 |

- **返回值**: 当前 `LoggerBuilder` 实例，支持链式调用。

##### `add_file`

- **描述**: 添加文件作为日志输出目标。
- **参数**:

| 参数名           | 类型                                            | 默认值              | 描述          |
|---------------|-----------------------------------------------|------------------|-------------|
| `file_path`   | `str` 或 `os.PathLike`                         | 必填               | 文件路径        |
| `level`       | `str` 或 `int`                                 | `"DEBUG"`        | 日志级别        |
| `log_format`  | `str` 或 `callable`                            | `DEFAULT_FORMAT` | 日志格式        |
| `log_filter`  | `str` 或 `callable`                            | `None`           | 日志过滤器       |
| `colorize`    | `bool`                                        | `False`          | 是否对输出进行颜色化  |
| `serialize`   | `bool`                                        | `False`          | 是否序列化日志记录   |
| `backtrace`   | `bool`                                        | `True`           | 是否包含完整的回溯信息 |
| `diagnose`    | `bool`                                        | `True`           | 是否包含诊断信息    |
| `enqueue`     | `bool`                                        | `True`           | 是否将日志记录放入队列 |
| `context`     | `str` 或 `multiprocessing.context.BaseContext` | `None`           | 多进程上下文      |
| `catch`       | `bool`                                        | `True`           | 是否捕获异常      |
| `rotation`    | `str`, `int`, `timedelta`, 或 `callable`       | `None`           | 日志文件轮转策略    |
| `retention`   | `str`, `int`, `timedelta`, 或 `callable`       | `None`           | 日志文件保留策略    |
| `compression` | `str` 或 `callable`                            | `None`           | 日志文件压缩策略    |
| `delay`       | `bool`                                        | `False`          | 是否延迟打开文件    |
| `watch`       | `bool`                                        | `False`          | 是否监视文件变化    |
| `mode`        | `str`                                         | `"a"`            | 文件打开模式      |
| `buffering`   | `int`                                         | `1`              | 缓冲大小        |
| `encoding`    | `str`                                         | `"utf-8"`        | 文件编码        |
| `errors`      | `str`                                         | `None`           | 编码错误处理方式    |
| `newline`     | `str`                                         | `None`           | 行结束符        |
| `closefd`     | `bool`                                        | `True`           | 是否关闭文件描述符   |
| `opener`      | `callable`                                    | `None`           | 自定义打开文件的函数  |

- **返回值**: 当前 `LoggerBuilder` 实例，支持链式调用。

##### `get_logger()`

- **描述**: 获取配置好的日志记录器。
- **返回值**: 配置好的日志记录器实例。

#### 日志格式

默认的日志格式如下：

```plaintext
<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | {process.name} | {thread.name}
| <cyan>{module}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan>
| <level>{level}</level>: <level>{message}</level>
```

你可以根据需要自定义日志格式，传递给 `log_format` 参数。

#### 注意事项

- `loguru` 的日志记录器是全局唯一的，因此 `LoggerBuilder` 实际上是对 `loguru.logger` 的封装。
- 如果你需要在多进程中使用日志记录器，请确保正确配置 `enqueue` 和 `context` 参数。
- 日志文件的轮转和保留策略可以帮助你管理日志文件的大小和生命周期，避免日志文件过大或过多。

希望这份文档能帮助你更好地理解和使用 `LoggerBuilder`。如果有任何问题或建议，请随时联系开发团队。