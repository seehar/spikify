import sys
from datetime import timedelta
from typing import TYPE_CHECKING
from typing import Optional
from typing import Union

from loguru import logger as loguru_logger


if TYPE_CHECKING:
    import multiprocessing.context
    import os


DEFAULT_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | {process.name} | {thread.name}"
    " | <cyan>{module}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan>"
    " | <level>{level}</level>: <level>{message}</level>"
)


class LoggerBuilder:
    """
    Logger 构建工具类

    使用方式：
    logger = LoggerBuilder().add_sys_stdout(level="DEBUG").add_file("log.log").get_logger()
    """

    def __init__(self):
        self._logger = loguru_logger
        self._logger.remove()

    def add_sys_stdout(
        self,
        level: Union[str, int] = "DEBUG",
        log_format: Union[str, callable] = DEFAULT_FORMAT,
    ) -> "LoggerBuilder":
        """
        添加系统标准输出作为日志输出目标。

        :param level: 日志级别，可以是字符串或整数。
        :param log_format: 日志格式，可以是字符串或格式化函数。
        :return: 当前 LoggerBuilder 实例，支持链式调用。
        """
        self._logger.add(sys.stdout, level=level, format=log_format)
        return self

    def add_file(
        self,
        file_path: Union[str, "os.PathLike"],
        level: Union[str, int] = "DEBUG",
        log_format: Union[str, callable] = DEFAULT_FORMAT,
        log_filter: Optional[Union[str, callable]] = None,
        colorize: Optional[bool] = False,
        serialize: bool = False,
        backtrace: bool = True,
        diagnose: bool = True,
        enqueue: bool = True,
        context: Optional[Union[str, "multiprocessing.context.BaseContext"]] = None,
        catch: bool = True,
        rotation: Optional[Union[str, int, timedelta, callable]] = None,
        retention: Optional[Union[str, int, timedelta, callable]] = None,
        compression: Optional[Union[str, callable]] = None,
        delay: bool = False,
        watch: bool = False,
        mode: str = "a",
        buffering: int = 1,
        encoding: str = "utf-8",
        errors: Optional[str] = None,
        newline: Optional[str] = None,
        closefd: bool = True,
        opener: Optional[callable] = None,
    ) -> "LoggerBuilder":
        """
        添加文件作为日志输出目标。

        :param file_path: 文件路径，可以是字符串或 PathLike 对象。
        :param level: 日志级别，可以是字符串或整数。
        :param log_format: 日志格式，可以是字符串或格式化函数。
        :param log_filter: 日志过滤器，可以是字符串、过滤函数或过滤字典。
        :param colorize: 是否对输出进行颜色化。
        :param serialize: 是否序列化日志记录。
        :param backtrace: 是否包含完整的回溯信息。
        :param diagnose: 是否包含诊断信息。
        :param enqueue: 是否将日志记录放入队列。
        :param context: 多进程上下文。
        :param catch: 是否捕获异常。
        :param rotation: 日志文件轮转策略。
        :param retention: 日志文件保留策略。
        :param compression: 日志文件压缩策略。
        :param delay: 是否延迟打开文件。
        :param watch: 是否监视文件变化。
        :param mode: 文件打开模式。
        :param buffering: 缓冲大小。
        :param encoding: 文件编码。
        :param errors: 编码错误处理方式。
        :param newline: 行结束符。
        :param closefd: 是否关闭文件描述符。
        :param opener: 自定义打开文件的函数。
        :return: 当前 LoggerBuilder 实例，支持链式调用。
        """
        self._logger.add(
            file_path,
            level=level,
            format=log_format,
            filter=log_filter,
            colorize=colorize,
            serialize=serialize,
            backtrace=backtrace,
            diagnose=diagnose,
            enqueue=enqueue,
            context=context,
            catch=catch,
            rotation=rotation,
            retention=retention,
            compression=compression,
            delay=delay,
            watch=watch,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            newline=newline,
            closefd=closefd,
            opener=opener,
        )
        return self

    def get_logger(self):
        """
        获取配置好的日志记录器。

        :return: 配置好的日志记录器实例。
        """
        return self._logger
