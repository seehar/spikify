from concurrent.futures import Future
from concurrent.futures import ProcessPoolExecutor

from spikify.manager.process_manager import ProcessManager


class TestProcessManager:
    def test_init(self):
        manager = ProcessManager(max_workers=3)
        assert isinstance(manager._executor, ProcessPoolExecutor)
        assert manager._max_workers == 3
        assert isinstance(manager._futures, list)

    def test_submit(self):
        def task():
            return 42

        manager = ProcessManager()
        future = manager.submit(task)
        assert isinstance(future, Future)
        assert manager.pending_count == 1

    def test_shutdown(self):
        manager = ProcessManager()
        manager.shutdown()
        # 这里可以添加更多的断言来验证关闭操作是否成功

    def test_all_done(self):
        manager = ProcessManager()
        assert manager.all_done()

        def task():
            return 42

        future = manager.submit(task)
        assert not manager.all_done()
        future.cancel()
        # 等待回调函数执行
        import time

        time.sleep(0.1)
        assert manager.all_done()

    def test_remove_future(self):
        manager = ProcessManager()

        def task():
            return 42

        future = manager.submit(task)
        assert manager.pending_count == 1
        manager._remove_future(future)
        assert manager.pending_count == 0

    def test_pending_count(self):
        manager = ProcessManager()
        assert manager.pending_count == 0

        def task():
            return 42

        manager.submit(task)
        assert manager.pending_count == 1
