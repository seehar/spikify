from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor

import pytest

from spikify.manager.thread_manager import ThreadManager


class TestThreadManager:
    def test_init(self):
        tm = ThreadManager(max_workers=5, thread_name_prefix="TestThread")
        assert isinstance(tm._executor, ThreadPoolExecutor)
        assert tm._max_workers == 5
        assert tm._executor._thread_name_prefix == "TestThread"
        assert tm._futures == []

    def test_submit_task(self):
        def dummy_task(x, y):
            return x + y

        tm = ThreadManager(max_workers=2)
        future = tm.submit(dummy_task, 1, 2)
        assert isinstance(future, Future)
        assert future.result() == 3
        assert tm.all_done() == False
        tm.shutdown()
        assert tm.all_done() == True

    def test_shutdown(self):
        def dummy_task(x, y):
            return x + y

        tm = ThreadManager(max_workers=2)
        tm.submit(dummy_task, 1, 2)
        tm.shutdown(wait=True, cancel_futures=False)
        assert tm.all_done() == True
        assert tm._futures == []

    def test_all_done(self):
        def dummy_task(x, y):
            return x + y

        tm = ThreadManager(max_workers=2)
        future = tm.submit(dummy_task, 1, 2)
        assert tm.all_done() == False
        result = future.result()  # Wait for the task to complete
        assert result == 3
        tm.shutdown()
        assert tm.all_done() == True

    def test_set_max_workers(self):
        tm = ThreadManager(max_workers=2)
        assert tm._max_workers == 2
        tm.set_max_workers(5)
        assert tm._max_workers == 5
        assert tm._executor._max_workers == 5

        with pytest.raises(ValueError):
            tm.set_max_workers(0)
