import sys
from concurrent.futures import Future
from concurrent.futures import ProcessPoolExecutor
from threading import RLock
from typing import Callable
from typing import List


class ProcessManager:
    def __init__(self, max_workers: int = 2):
        """
        初始化进程管理器。

        :param max_workers: 进程池中最大工作进程数。
        """
        self._executor = ProcessPoolExecutor(max_workers=max_workers)
        self._futures: List[Future] = []
        self._lock = RLock()
        self._max_workers = max_workers

    def submit(self, task: Callable, /, *args, **kwargs) -> Future:
        """
        提交一个任务到进程池执行。

        :param task: 要执行的可调用任务，需可序列化（Pickle 兼容）。
        :param args: 传递给任务的位置参数。
        :param kwargs: 传递给任务的关键字参数。
        :return: 表示任务的 Future 对象。
        """
        future = self._executor.submit(task, *args, **kwargs)

        def done_callback(fut: Future) -> None:
            self._remove_future(fut)

        future.add_done_callback(done_callback)
        with self._lock:
            self._futures.append(future)
        return future

    def shutdown(self, wait: bool = True, cancel_futures: bool = False) -> None:
        """
        关闭进程池并清理资源。

        :param wait: 是否等待所有任务完成后再关闭。
        :param cancel_futures: 是否尝试取消未完成的任务（Python <3.9 可能无法完全生效）。
        """
        if sys.version_info >= (3, 9):
            self._executor.shutdown(wait=wait, cancel_futures=cancel_futures)
        else:
            # 低版本无法通过 shutdown 直接取消任务，需手动尝试
            self._executor.shutdown(wait=wait)
            if cancel_futures:
                self.__cancel_all_future()

        with self._lock:
            self._futures.clear()

    def __cancel_all_future(self) -> None:
        """
        取消所有未完成的任务（仅在 Python <3.9 时由 shutdown 调用）。
        注意：已开始执行的任务可能无法被终止。
        """
        with self._lock:
            for future in self._futures:
                # 仅尝试取消未开始的任务
                if not future.running():
                    future.cancel()

    def all_done(self) -> bool:
        """
        检查所有提交的任务是否均已完成。

        :return: 全部完成返回 True，否则返回 False。
        """
        with self._lock:
            return not bool(self._futures)

    def _remove_future(self, future: Future) -> None:
        """
        内部方法：从跟踪列表中移除已完成的 Future。

        :param future: 要移除的 Future 对象。
        """
        with self._lock:
            try:
                self._futures.remove(future)
            except ValueError:
                pass  # 防止重复移除

    @property
    def pending_count(self) -> int:
        """
        获取当前未完成的任务数量。

        :return: 待完成任务数。
        """
        with self._lock:
            return len(self._futures)
