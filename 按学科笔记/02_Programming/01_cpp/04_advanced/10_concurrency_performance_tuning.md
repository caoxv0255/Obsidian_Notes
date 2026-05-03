---
type: advanced
topic: concurrency_performance_tuning
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 并发, 性能优化, 线程池]
---

# Linux C++ 并发与性能调优

> 这一页把线程池、锁、原子、false sharing、以及性能优化的基本路径串起来。

## 1) 并发编程的基本原则

- 共享数据越少越好。
- 锁粒度越小越好，但不要把系统复杂度炸掉。
- 能批处理就不要单条处理。
- 热路径上尽量避免动态分配和额外拷贝。

## 2) 一个最小可用的线程池骨架

```cpp
#include <condition_variable>
#include <functional>
#include <future>
#include <memory>
#include <mutex>
#include <queue>
#include <thread>
#include <type_traits>
#include <utility>
#include <vector>

class ThreadPool {
public:
    explicit ThreadPool(std::size_t threadCount) {
        start(threadCount);
    }

    ~ThreadPool() {
        stop();
    }

    template <class Function, class... Args>
    auto submit(Function&& function, Args&&... args)
        -> std::future<typename std::invoke_result_t<Function, Args...>> {
        using ReturnType = typename std::invoke_result_t<Function, Args...>;

        auto task = std::make_shared<std::packaged_task<ReturnType()>>(
            std::bind(std::forward<Function>(function), std::forward<Args>(args)...));

        std::future<ReturnType> result = task->get_future();

        {
            std::lock_guard<std::mutex> lock(mutex_);
            tasks.emplace([task]() { (*task)(); });
        }

        cv.notify_one();
        return result;
    }

private:
    std::vector<std::thread> workers;
    std::queue<std::function<void()>> tasks;
    std::mutex mutex_;
    std::condition_variable cv;
    bool stopping = false;

    void start(std::size_t threadCount) {
        for (std::size_t index = 0; index < threadCount; ++index) {
            workers.emplace_back([this]() {
                while (true) {
                    std::function<void()> task;
                    {
                        std::unique_lock<std::mutex> lock(mutex_);
                        cv.wait(lock, [this]() { return stopping || !tasks.empty(); });
                        if (stopping && tasks.empty()) {
                            return;
                        }
                        task = std::move(tasks.front());
                        tasks.pop();
                    }
                    task();
                }
            });
        }
    }

    void stop() {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            stopping = true;
        }
        cv.notify_all();
        for (auto& worker : workers) {
            if (worker.joinable()) {
                worker.join();
            }
        }
    }
};
```

## 3) 常见性能问题

- false sharing：不同线程写相邻变量，缓存行抖动严重。
- 频繁锁竞争：把吞吐量直接压扁。
- 小对象大量分配：分配器开销会变成热点。
- 容器不预留容量：`reserve()` 很多时候比事后优化更有效。

## 4) 适合工程里的优化顺序

1. 先测：基准测试、压测、火焰图。
2. 再定位：锁、分配、拷贝、I/O。
3. 最后修改：批处理、预分配、减少共享、减少日志开销。

## 5) 一个缓存行对齐的例子

```cpp
#include <atomic>

struct alignas(64) PaddedCounter {
    std::atomic<long long> value {0};
};
```

## 6) 工具建议

- `perf`：看 CPU 热点。
- `valgrind`：看内存和缓存问题。
- `asan/ubsan/tsan`：看越界、未定义行为、数据竞争。
