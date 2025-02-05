# ThreadManager 线程管理器

## 简介
`ThreadManager` 是一个用于管理线程池的类，它基于 Python 的 `concurrent.futures.ThreadPoolExecutor`。该类提供了提交任务、关闭线程池、检查任务状态以及动态调整线程池大小的功能。

## 初始化
```python
from thread_manager import ThreadManager

# 创建一个 ThreadManager 实例，默认最大工作线程数为 2，线程名称前缀为 "ThreadManager"
thread_manager = ThreadManager(max_workers=2, thread_name_prefix="MyThread")
```


### 参数说明
- `max_workers`: 线程池中最大工作线程数，默认值为 2。
- `thread_name_prefix`: 线程名称的前缀，默认值为 "ThreadManager"。

## 提交任务
使用 `submit` 方法可以将任务提交到线程池中执行。该方法返回一个 `Future` 对象，可以通过该对象获取任务的执行结果或状态。

```python
def my_task(arg1, arg2):
    print(f"Task running with args: {arg1}, {arg2}")
    return arg1 + arg2

future = thread_manager.submit(my_task, 1, 2)

# 获取任务结果
result = future.result()
print(f"Task result: {result}")
```


### 参数说明
- `task`: 要执行的任务，必须是一个可调用对象。
- `*args`: 传递给任务的位置参数。
- `**kwargs`: 传递给任务的关键字参数。

## 关闭线程池
使用 `shutdown` 方法可以关闭线程池，并可以选择是否等待所有任务完成或取消未完成的任务。

```python
thread_manager.shutdown(wait=True, cancel_futures=False)
```


### 参数说明
- `wait`: 如果为 `True`，则等待所有任务完成后再关闭线程池；如果为 `False`，则立即关闭线程池。
- `cancel_futures`: 如果为 `True`，则取消所有未完成的任务。

## 检查任务状态
使用 `all_done` 方法可以检查所有任务是否已完成。

```python
if thread_manager.all_done():
    print("All tasks are done.")
else:
    print("Some tasks are still running.")
```


## 动态调整线程池大小
使用 `set_max_workers` 方法可以动态设置线程池的最大工作线程数。

```python
thread_manager.set_max_workers(5)
```


### 参数说明
- `max_workers`: 新的最大工作线程数。必须大于 0。

## 注意事项
- 在 Python 3.9 及以上版本中，`shutdown` 方法支持 `cancel_futures` 参数；在较低版本中，该参数会被忽略。
- `set_max_workers` 方法会直接修改线程池的最大工作线程数，并根据需要调整线程数量。

## 示例代码
```python
from thread_manager import ThreadManager
import time

def task(n):
    time.sleep(n)
    return f"Task {n} completed"

# 创建 ThreadManager 实例
tm = ThreadManager(max_workers=3)

# 提交多个任务
futures = []
for i in range(5):
    futures.append(tm.submit(task, i))

# 获取任务结果
for future in futures:
    print(future.result())

# 关闭线程池
tm.shutdown(wait=True)

# 检查所有任务是否完成
if tm.all_done():
    print("All tasks are done.")

# 动态调整线程池大小
tm.set_max_workers(5)
```
