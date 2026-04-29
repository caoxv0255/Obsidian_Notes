---
type: special
topic: STL底层原理
category: data_structures
difficulty: advanced
language: C++20
book: Introduction of Algorithms (CLRS)
created: 2026-02-21
status: learning
acm_relevant: true
---

# STL底层原理详解

## 概述

C++标准模板库（STL）是C++标准库的重要组成部分，提供了高效的容器、迭代器、算法和函数对象。理解STL的底层实现对于编写高效、正确的C++代码至关重要。

## 目录

1. [容器底层实现](#1-容器底层实现)
2. [迭代器](#2-迭代器)
3. [算法库](#3-算法库)
4. [内存分配器](#4-内存分配器)
5. [函数对象](#5-函数对象)

## 1. 容器底层实现

### 1.1 std::vector

**底层结构**：动态数组

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <initializer_list>
#include <utility>
#include <new>

template <typename T, typename Allocator = std::allocator<T>>
class Vector {
private:
    T* data_;           // 指向数据数组
    size_t size_;       // 当前元素数量
    size_t capacity_;   // 当前容量
    Allocator alloc_;   // 内存分配器

public:
    using iterator = T*;
    using const_iterator = const T*;
    // 构造函数
    Vector() noexcept : data_(nullptr), size_(0), capacity_(0) {}

    explicit Vector(size_t count, const T& value = T())
        : data_(nullptr), size_(count), capacity_(count) {
        data_ = alloc_.allocate(count);
        for (size_t i = 0; i < count; ++i) {
            std::construct_at(&data_[i], value);
        }
    }

    Vector(std::initializer_list<T> init) : Vector() {
        reserve(init.size());
        for (const auto& item : init) {
            push_back(item);
        }
    }

    // 析构函数
    ~Vector() {
        clear();
        if (data_) {
            alloc_.deallocate(data_, capacity_);
        }
    }

    // 拷贝构造
    Vector(const Vector& other) : data_(nullptr), size_(0), capacity_(0) {
        reserve(other.size_);
        for (size_t i = 0; i < other.size_; ++i) {
            push_back(other.data_[i]);
        }
    }

    // 移动构造
    Vector(Vector&& other) noexcept
        : data_(other.data_), size_(other.size_),
          capacity_(other.capacity_), alloc_(std::move(other.alloc_)) {
        other.data_ = nullptr;
        other.size_ = 0;
        other.capacity_ = 0;
    }

    //拷贝赋值
    Vector& operator=(const Vector& other){
            if(this != &other){
                    Vector temp(other);
                    swap(temp);
            }
            return *this;
    }

    //移动赋值
    Vector& operator=(Vector&& other)noexcept{
            if(this != &other){
                    clear();
                    if(data_){
                            alloc_.deallocate(data_,capacity_);
                    }
                    data_ = other.data_;
                    size_ = other.size_;
                    capacity_ = other.capacity_;
                    alloc_ = std::move(other.alloc_);
                    other.data_ = nullptr;
                    other.capacity_ = 0;
                    other.size_ = 0;
            }
            return *this;
    }

    //swap
    void swap(Vector& other)noexcept{
            std::swap(data_,other.data_);
            std::swap(size_,other.size_);
            std::swap(capacity_,other.capacity_);
            std::swap(alloc_,other.alloc_);
    }

    //shrink_to_fit
    void shrink_to_fit(){
            if(size_ < capacity_){
                    reserve(size_);
            }
    }

    //max_size
    size_t max_size() const noexcept {
    return alloc_.max_size();
    }

    // 元素访问
    T& operator[](size_t index) { return data_[index]; }
    const T& operator[](size_t index) const { return data_[index]; }

    T& at(size_t index) {
        if (index >= size_) {
            throw std::out_of_range("Vector index out of range");
        }
        return data_[index];
    }

    T& front() {
            if(empty()) {throw std::out_of_range("Vector is empty.");}
            return data_[0];
    }
    T& back() {
            if(empty()) {throw std::out_of_range("Vector is empty.");}
            return data_[size_ - 1];
    }
    T* data() noexcept { return data_; }

    // 迭代器
    T* begin() noexcept { return data_; }
    T* end() noexcept { return data_ + size_; }
    const T* begin() const noexcept { return data_; }
    const T* end() const noexcept { return data_ + size_; }
    const T* cbegin() const noexcept { return data_; }
    const T* cend() const noexcept { return data_ + size_; }

    // 容量
    bool empty() const noexcept { return size_ == 0; }
    size_t size() const noexcept { return size_; }
    size_t capacity() const noexcept { return capacity_; }

    void reserve(size_t new_capacity) {
    if (new_capacity <= capacity_) return;

    T* new_data = alloc_.allocate(new_capacity);

    try {
        std::uninitialized_move(data_, data_ + size_, new_data);
    } catch (...) {
        alloc_.deallocate(new_data, new_capacity);
        throw;
    }

    // 销毁并释放旧内存
    std::destroy(data_, data_ + size_);
    if (data_) {
        alloc_.deallocate(data_, capacity_);
    }

    data_ = new_data;
    capacity_ = new_capacity;
}

    //带默认值的resize
    void resize(size_t new_size, const T& value = T()) {
            if (new_size < size_) {
                    for (size_t i = new_size; i < size_; ++i) {
                            std::destroy_at(&data_[i]);
                    }
                    size_ = new_size;
            } else if (new_size > size_) {
                    reserve(new_size);
                    size_t old_size = size_;
                    size_t constructed = 0;
                    try {
                            for (; constructed < new_size - old_size; ++constructed) {
                                    std::construct_at(&data_[old_size + constructed], value);
                            }
                    } catch (...) {
                            for (size_t i = 0; i < constructed; ++i) {
                                    std::destroy_at(&data_[old_size + i]);
                            }
                            throw;
                    }
                    size_ = new_size;
            }
    }


    // 修改
    void push_back(const T& value) {
        if (size_ >= capacity_) {
            reserve(capacity_ == 0 ? 1 : capacity_ * 2);
        }
        std::construct_at(&data_[size_++], value);
    }

    void push_back(T&& value) {
        if (size_ >= capacity_) {
            reserve(capacity_ == 0 ? 1 : capacity_ * 2);
        }
        std::construct_at(&data_[size_++], std::move(value));
    }

    template <typename... Args>
    void emplace_back(Args&&... args) {
        if (size_ >= capacity_) {
            reserve(capacity_ == 0 ? 1 : capacity_ * 2);
        }
        std::construct_at(&data_[size_++], std::forward<Args>(args)...);
    }

    void pop_back() {
        if (size_ > 0) {
            std::destroy_at(&data_[--size_]);
        }
    }

    void clear() {
        for (size_t i = 0; i < size_; ++i) {
            std::destroy_at(&data_[i]);
        }
        size_ = 0;
    }
};

//类外swap
template <typename T, typename Alloc>
void swap(Vector<T, Alloc>& a, Vector<T, Alloc>& b) noexcept {
    a.swap(b);
}


// ============ 测试用例 ============

void test_vector() {
    std::cout << "=== Vector 测试 ===" << std::endl;

    // 测试1: 基本操作
    {
        Vector<int> vec;
        vec.push_back(1);
        vec.push_back(2);
        vec.push_back(3);

        std::cout << "基本操作: ";
        for (const auto& item : vec) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    }

    // 测试2: 初始化列表
    {
        Vector<int> vec = {1, 2, 3, 4, 5};
        std::cout << "初始化列表: ";
        for (const auto& item : vec) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    }

    // 测试3: 扩容
    {
        Vector<int> vec;
        std::cout << "容量测试: ";
        for (int i = 0; i < 10; ++i) {
            vec.push_back(i);
            std::cout << "size=" << vec.size()
                      << ", capacity=" << vec.capacity() << "; ";
        }
        std::cout << std::endl;
    }

    // 测试4: emplace_back
    {
        Vector<std::pair<int, int>> vec;
        vec.emplace_back(1, 2);
        vec.emplace_back(3, 4);

        std::cout << "emplace_back: ";
        for (const auto& [first, second] : vec) {
            std::cout << "(" << first << "," << second << ") ";
        }
        std::cout << std::endl;
    }
    // 测试5: 赋值运算符
    {
            Vector<int> vec1 = {1, 2, 3};
            Vector<int> vec2;
            vec2 = vec1;  // 拷贝赋值

            std::cout << "拷贝赋值: ";
            for (const auto& item : vec2) {
                    std::cout << item << " ";
            }
            std::cout << std::endl;
    }

// 测试6: 移动赋值
{
    Vector<int> vec1 = {1, 2, 3};
    Vector<int> vec2;
    vec2 = std::move(vec1);  // 移动赋值

    std::cout << "移动赋值: ";
    for (const auto& item : vec2) {
        std::cout << item << " ";
    }
    std::cout << ", vec1.size=" << vec1.size() << std::endl;
}

// 测试7: resize
{
    Vector<int> vec = {1, 2, 3, 4, 5};
    vec.resize(3);  // 缩小
    std::cout << "resize缩小: ";
    for (const auto& item : vec) {
        std::cout << item << " ";
    }

    vec.resize(5, 0);  // 扩大
    std::cout << ", resize扩大: ";
    for (const auto& item : vec) {
        std::cout << item << " ";
    }
    std::cout << std::endl;
}

// 测试8: front/back 异常
{
    Vector<int> vec;
    try {
        vec.front();
    } catch (const std::out_of_range& e) {
        std::cout << "front 异常捕获: " << e.what() << std::endl;
    }
}

// 测试9: at 异常
{
    Vector<int> vec = {1, 2, 3};
    try {
        vec.at(10);
    } catch (const std::out_of_range& e) {
        std::cout << "at 异常捕获: " << e.what() << std::endl;
    }
}

// 测试10: swap
{
    Vector<int> vec1 = {1, 2, 3};
    Vector<int> vec2 = {4, 5};
    swap(vec1, vec2);

    std::cout << "swap后 vec1: ";
    for (const auto& item : vec1) {
        std::cout << item << " ";
    }
    std::cout << ", vec2: ";
    for (const auto& item : vec2) {
        std::cout << item << " ";
    }
    std::cout << std::endl;
}
}

int main() {
    test_vector();
    return 0;
}
```



**关键特性**：
- **时间复杂度**：
  - 随机访问：O(1)
  - 尾部插入/删除：O(1) 平均
  - 中间插入/删除：O(n)
  - 扩容：O(n)（但分摊后为O(1)）
- **扩容策略**：通常按2倍扩容
- **内存连续性**：保证内存连续，适合缓存友好

### 1.2 std::list

**底层结构**：双向链表

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <utility>
#include <initializer_list>

template <typename T, typename Allocator = std::allocator<T>>
class List {
private:
    struct Node {
        T value;
        Node* prev;
        Node* next;

        Node(const T& val, Node* p, Node* n)
            : value(val), prev(p), next(n) {}
    };

    using NodeAllocator = typename std::allocator_traits<Allocator>::
        template rebind_alloc<Node>;

    Node* head_;
    Node* tail_;
    size_t size_;
    NodeAllocator alloc_;

public:
    // 迭代器
    class Iterator {
    private:
        Node* node_;
    public:
        using iterator_category = std::bidirectional_iterator_tag;
        using value_type = T;
        using difference_type = std::ptrdiff_t;
        using pointer = T*;
        using reference = T&;

        explicit Iterator(Node* node) : node_(node) {}

        reference operator*() const { return node_->value; }
        pointer operator->() const { return &node_->value; }

        Iterator& operator++() {
            node_ = node_->next;
            return *this;
        }

        Iterator operator++(int) {
            Iterator tmp = *this;
            ++(*this);
            return tmp;
        }

        Iterator& operator--() {
            node_ = node_->prev;
            return *this;
        }

        Iterator operator--(int) {
            Iterator tmp = *this;
            --(*this);
            return tmp;
        }

        bool operator==(const Iterator& other) const {
            return node_ == other.node_;
        }

        bool operator!=(const Iterator& other) const {
            return !(*this == other);
        }
    };

    //反向迭代器
	class ReverseIterator {
	private:
		Node* node_;
	public:
	    using iterator_category = std::bidirectional_iterator_tag;
	    using value_type = T;
	    using difference_type = std::ptrdiff_t;
	    using pointer = T*;
	    using reference = T&;

	    explicit ReverseIterator(Node* node) : node_(node) {}

	    reference operator*() const { return node_->value; }
	    pointer operator->() const { return &node_->value; }

	    ReverseIterator& operator++() {  // 反向迭代器的++是向前
	        node_ = node_->prev;
	        return *this;
	    }

	    ReverseIterator operator++(int) {
	        ReverseIterator tmp = *this;
	        ++(*this);
	        return tmp;
	    }

	    ReverseIterator& operator--() {
	        node_ = node_->next;
	        return *this;
	    }

	    ReverseIterator operator--(int) {
	        ReverseIterator tmp = *this;
	        --(*this);
	        return tmp;
	    }

	    bool operator==(const ReverseIterator& other) const {
	        return node_ == other.node_;
	    }

	    bool operator!=(const ReverseIterator& other) const {
	        return !(*this == other);
	    }
	};

	=using reverse_iterator = ReverseIterator;
	using const_reverse_iterator = const ReverseIterator;

	reverse_iterator rbegin() noexcept { return reverse_iterator(tail_); }
	reverse_iterator rend() noexcept { return reverse_iterator(nullptr); }
	const_reverse_iterator rbegin() const noexcept { 
		return const_reverse_iterator(tail_); 
	}
	const_reverse_iterator rend() const noexcept { 
		return const_reverse_iterator(nullptr); 
	}

    using iterator = Iterator;
    using const_iterator = const Iterator;

    List() : head_(nullptr), tail_(nullptr), size_(0) {}

    List(std::initializer_list<T> init):List(){
            for(const auto& item:init){
                    push_back(item);
            }
    }

    // 拷贝构造
    List(const List& other) : List() {
        for (const auto& item : other) {
            push_back(item);
        }
    }

    // 移动构造
    List(List&& other) noexcept
        : head_(other.head_), tail_(other.tail_), size_(other.size_),
          alloc_(std::move(other.alloc_)) {
        other.head_ = nullptr;
        other.tail_ = nullptr;
        other.size_ = 0;
    }

    ~List() {
        clear();
    }

    // 拷贝赋值
    List& operator=(const List& other) {
        if (this != &other) {
            List temp(other);
            swap(temp);
        }
        return *this;
    }

    // 移动赋值
    List& operator=(List&& other) noexcept {
        if (this != &other) {
            clear();
            head_ = other.head_;
            tail_ = other.tail_;
            size_ = other.size_;
            alloc_ = std::move(other.alloc_);
            other.head_ = nullptr;
            other.tail_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }

    void swap(List& other) noexcept {
        std::swap(head_, other.head_);
        std::swap(tail_, other.tail_);
        std::swap(size_, other.size_);
        std::swap(alloc_, other.alloc_);
    }

    void push_front(const T& value) {
        Node* new_node = alloc_.allocate(1);
        try {
            std::construct_at(new_node, value, nullptr, head_);
        } catch (...) {
            alloc_.deallocate(new_node, 1);
            throw;
        }

        if (head_) {
            head_->prev = new_node;
        }
        head_ = new_node;

        if (!tail_) {
            tail_ = new_node;
        }
        ++size_;
    }

    void push_back(const T& value) {
        Node* new_node = alloc_.allocate(1);
        try {
            std::construct_at(new_node, value, tail_, nullptr);
        } catch (...) {
            alloc_.deallocate(new_node, 1);
            throw;
        }

        if (tail_) {
            tail_->next = new_node;
        }
        tail_ = new_node;

        if (!head_) {
            head_ = new_node;
        }
        ++size_;
    }

    void pop_front() {
        if (head_) {
            Node* temp = head_;
            head_ = head_->next;
            if (head_) {
                head_->prev = nullptr;
            } else {
                tail_ = nullptr;
            }
            std::destroy_at(temp);
            alloc_.deallocate(temp, 1);
            --size_;
        }
    }

    void pop_back() {
        if (tail_) {
            Node* temp = tail_;
            tail_ = tail_->prev;
            if (tail_) {
                tail_->next = nullptr;
            } else {
                head_ = nullptr;
            }
            std::destroy_at(temp);
            alloc_.deallocate(temp, 1);
            --size_;
        }
    }

    T& front() {
        if (empty()) throw std::out_of_range("List is empty");
        return head_->value;
    }

    const T& front() const {
        if (empty()) throw std::out_of_range("List is empty");
        return head_->value;
    }

    T& back() {
        if (empty()) throw std::out_of_range("List is empty");
        return tail_->value;
    }

    const T& back() const {
        if (empty()) throw std::out_of_range("List is empty");
        return tail_->value;
    }

    iterator begin() noexcept { return iterator(head_); }
    iterator end() noexcept { return iterator(nullptr); }
    const_iterator begin() const noexcept { return const_iterator(head_); }
    const_iterator end() const noexcept { return const_iterator(nullptr); }
    const_iterator cbegin() const noexcept { return const_iterator(head_); }
    const_iterator cend() const noexcept { return const_iterator(nullptr); }

    size_t size() const noexcept { return size_; }
    bool empty() const noexcept { return size_ == 0; }

    void clear() {
        while (!empty()) {
            pop_front();
        }
    }
};

// 类外 swap
template <typename T, typename Alloc>
void swap(List<T, Alloc>& a, List<T, Alloc>& b) noexcept {
    a.swap(b);
}

// ============ 测试用例 ============

void print_list(const List<int>& list, const std::string& label) {
    std::cout << label << ": ";
    for (const auto& item : list) {
        std::cout << item << " ";
    }
    std::cout << "(size=" << list.size() << ")" << std::endl;
}

void test_basic_operations() {
    std::cout << "\n=== 测试1: 基本操作 ===" << std::endl;

    List<int> list;
    list.push_back(1);
    list.push_back(2);
    list.push_back(3);
    print_list(list, "push_back 后");

    list.push_front(0);
    print_list(list, "push_front 后");

    list.pop_front();
    print_list(list, "pop_front 后");

    list.pop_back();
    print_list(list, "pop_back 后");
}

void test_front_back() {
    std::cout << "\n=== 测试2: front/back 访问 ===" << std::endl;

    List<int> list;
    list.push_back(10);
    list.push_back(20);
    list.push_back(30);

    std::cout << "front: " << list.front() << std::endl;
    std::cout << "back: " << list.back() << std::endl;

    // 测试空列表异常
    List<int> empty_list;
    try {
        empty_list.front();
    } catch (const std::out_of_range& e) {
        std::cout << "front 异常捕获: " << e.what() << std::endl;
    }

    try {
        empty_list.back();
    } catch (const std::out_of_range& e) {
        std::cout << "back 异常捕获: " << e.what() << std::endl;
    }
}

void test_iterator() {
    std::cout << "\n=== 测试3: 迭代器 ===" << std::endl;

    List<int> list;
    list.push_back(1);
    list.push_back(2);
    list.push_back(3);
    list.push_back(4);
    list.push_back(5);

    // 正向遍历
    std::cout << "正向遍历: ";
    for (auto it = list.begin(); it != list.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // 反向遍历
    std::cout << "反向遍历: ";
    for (auto rit = list.rbegin(); rit != list.rend(); ++rit) {
        std::cout << *rit << " ";
    }
    std::cout << std::endl;

    // 使用范围 for
    std::cout << "范围 for: ";
    for (const auto& item : list) {
        std::cout << item << " ";
    }
    std::cout << std::endl;
}

void test_copy() {
    std::cout << "\n=== 测试4: 拷贝构造和赋值 ===" << std::endl;

    List<int> list1;
    list1.push_back(1);
    list1.push_back(2);
    list1.push_back(3);
    print_list(list1, "list1 原始");

    // 拷贝构造
    List<int> list2(list1);
    print_list(list2, "list2 拷贝构造");

    // 拷贝赋值
    List<int> list3;
    list3 = list1;
    print_list(list3, "list3 拷贝赋值");

    // 修改原列表，验证深拷贝
    list1.push_back(4);
    print_list(list1, "list1 修改后");
    print_list(list2, "list2 应不变");
}

void test_move() {
    std::cout << "\n=== 测试5: 移动构造和赋值 ===" << std::endl;

    List<int> list1;
    list1.push_back(1);
    list1.push_back(2);
    list1.push_back(3);
    print_list(list1, "list1 原始");

    // 移动构造
    List<int> list2(std::move(list1));
    print_list(list2, "list2 移动构造后");
    std::cout << "list1 移动后 size: " << list1.size() << std::endl;

    // 移动赋值
    List<int> list3;
    list3 = std::move(list2);
    print_list(list3, "list3 移动赋值后");
    std::cout << "list2 移动后 size: " << list2.size() << std::endl;
}

void test_swap() {
    std::cout << "\n=== 测试6: swap ===" << std::endl;

    List<int> list1;
    list1.push_back(1);
    list1.push_back(2);
    list1.push_back(3);

    List<int> list2;
    list2.push_back(10);
    list2.push_back(20);

    print_list(list1, "swap 前 list1");
    print_list(list2, "swap 前 list2");

    // 成员 swap
    list1.swap(list2);
    print_list(list1, "swap 后 list1");
    print_list(list2, "swap 后 list2");

    // 全局 swap
    swap(list1, list2);
    print_list(list1, "全局 swap 后 list1");
    print_list(list2, "全局 swap 后 list2");
}

void test_clear() {
    std::cout << "\n=== 测试7: clear 和 empty ===" << std::endl;

    List<int> list;
    list.push_back(1);
    list.push_back(2);
    list.push_back(3);

    std::cout << "clear 前 empty: " << list.empty() << std::endl;
    std::cout << "clear 前 size: " << list.size() << std::endl;

    list.clear();

    std::cout << "clear 后 empty: " << list.empty() << std::endl;
    std::cout << "clear 后 size: " << list.size() << std::endl;
}

void test_const_iterators() {
    std::cout << "\n=== 测试8: const 迭代器 ===" << std::endl;

    const List<int> list{1, 2, 3, 4, 5};

    std::cout << "cbegin/cend: ";
    for (auto it = list.cbegin(); it != list.cend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
}

void test_edge_cases() {
    std::cout << "\n=== 测试9: 边界情况 ===" << std::endl;

    // 空列表操作
    List<int> empty;
    empty.pop_front();  // 应无崩溃
    empty.pop_back();   // 应无崩溃
    std::cout << "空列表 pop 操作: 无崩溃 ✓" << std::endl;

    // 单元素列表
    List<int> single;
    single.push_back(42);
    single.pop_front();
    std::cout << "单元素 pop 后 empty: " << single.empty() << std::endl;

    // 大量元素
    List<int> large;
    for (int i = 0; i < 100; ++i) {
        large.push_back(i);
    }
    std::cout << "大量元素 size: " << large.size() << std::endl;

    // 反向遍历大量元素
    int count = 0;
    for (auto it = large.end(); ; ) {
        --it;
        ++count;
        if (it == large.begin()) break;
    }
    std::cout << "反向遍历计数: " << count << std::endl;
}

int main() {
    std::cout << "========================================" << std::endl;
    std::cout << "       双向链表 List 测试套件          " << std::endl;
    std::cout << "========================================" << std::endl;

    test_basic_operations();
    test_front_back();
    test_iterator();
    test_copy();
    test_move();
    test_swap();
    test_clear();
    test_const_iterators();
    test_edge_cases();

    std::cout << "\n========================================" << std::endl;
    std::cout << "           所有测试完成！              " << std::endl;
    std::cout << "========================================" << std::endl;

    return 0;

```

**关键特性**：
- **时间复杂度**：
  - 任意位置插入/删除：O(1)
  - 随机访问：O(n)
- **内存特性**：节点分散，不保证连续

### 1.3 std::deque

**底层结构**：分段连续数组（分段连续内存）

```cpp
template <typename T, size_t ChunkSize = 512>
class Deque {
private:
    using Chunk = std::unique_ptr<T[]>;
    std::vector<Chunk> chunks_;
    size_t start_idx_;  // 起始chunk索引
    size_t start_pos_;  // 起始位置
    size_t size_;
    
public:
    Deque() : start_idx_(0), start_pos_(0), size_(0) {}
    
    void push_back(const T& value) {
        if (chunks_.empty() || start_pos_ + size_ >= ChunkSize) {
            add_chunk_back();
        }
        
        size_t global_pos = start_pos_ + size_;
        size_t chunk_idx = start_idx_ + global_pos / ChunkSize;
        size_t pos_in_chunk = global_pos % ChunkSize;
        
        chunks_[chunk_idx - start_idx_][pos_in_chunk] = value;
        ++size_;
    }
    
    void push_front(const T& value) {
        if (start_pos_ == 0) {
            add_chunk_front();
            start_pos_ = ChunkSize;
        }
        
        --start_pos_;
        chunks_[0][start_pos_] = value;
        ++size_;
    }
    
private:
    void add_chunk_back() {
        chunks_.push_back(std::make_unique<T[]>(ChunkSize));
    }
    
    void add_chunk_front() {
        chunks_.insert(chunks_.begin(), std::make_unique<T[]>(ChunkSize));
        ++start_idx_;
    }
};
```

**关键特性**：
- **时间复杂度**：
  - 头尾插入/删除：O(1) 分摊
  - 随机访问：O(1)
- **内存特性**：分段连续，平衡了vector和list的优势

### 1.4 std::map 和 std::set

**底层结构**：红黑树（Red-Black Tree）

红黑树是一棵自平衡二叉搜索树，满足以下性质：
1. 每个节点是红色或黑色
2. 根节点是黑色
3. 所有叶子节点（NIL）是黑色
4. 红色节点的两个子节点都是黑色
5. 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点

```cpp
enum class Color { RED, BLACK };

template <typename Key, typename Value>
struct RBTreeNode {
    Key key;
    Value value;
    Color color;
    RBTreeNode* left;
    RBTreeNode* right;
    RBTreeNode* parent;
    
    RBTreeNode(const Key& k, const Value& v)
        : key(k), value(v), color(Color::RED),
          left(nullptr), right(nullptr), parent(nullptr) {}
};

template <typename Key, typename Value>
class RBTree {
private:
    RBTreeNode<Key, Value>* root_;
    RBTreeNode<Key, Value>* nil_;  // 哨兵节点
    
    void left_rotate(RBTreeNode<Key, Value>* x) {
        RBTreeNode<Key, Value>* y = x->right;
        x->right = y->left;
        
        if (y->left != nil_) {
            y->left->parent = x;
        }
        
        y->parent = x->parent;
        
        if (x->parent == nil_) {
            root_ = y;
        } else if (x == x->parent->left) {
            x->parent->left = y;
        } else {
            x->parent->right = y;
        }
        
        y->left = x;
        x->parent = y;
    }
    
    void right_rotate(RBTreeNode<Key, Value>* y) {
        RBTreeNode<Key, Value>* x = y->left;
        y->left = x->right;
        
        if (x->right != nil_) {
            x->right->parent = y;
        }
        
        x->parent = y->parent;
        
        if (y->parent == nil_) {
            root_ = x;
        } else if (y == y->parent->right) {
            y->parent->right = x;
        } else {
            y->parent->left = x;
        }
        
        x->right = y;
        y->parent = x;
    }
    
    void insert_fixup(RBTreeNode<Key, Value>* z) {
        while (z->parent->color == Color::RED) {
            if (z->parent == z->parent->parent->left) {
                RBTreeNode<Key, Value>* y = z->parent->parent->right;
                
                if (y->color == Color::RED) {
                    z->parent->color = Color::BLACK;
                    y->color = Color::BLACK;
                    z->parent->parent->color = Color::RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->right) {
                        z = z->parent;
                        left_rotate(z);
                    }
                    z->parent->color = Color::BLACK;
                    z->parent->parent->color = Color::RED;
                    right_rotate(z->parent->parent);
                }
            } else {
                // 对称情况
            }
        }
        root_->color = Color::BLACK;
    }
    
public:
    RBTree() {
        nil_ = new RBTreeNode<Key, Value>(Key{}, Value{});
        nil_->color = Color::BLACK;
        root_ = nil_;
    }
    
    void insert(const Key& key, const Value& value) {
        RBTreeNode<Key, Value>* z = new RBTreeNode<Key, Value>(key, value);
        z->left = nil_;
        z->right = nil_;
        
        RBTreeNode<Key, Value>* y = nil_;
        RBTreeNode<Key, Value>* x = root_;
        
        while (x != nil_) {
            y = x;
            if (z->key < x->key) {
                x = x->left;
            } else {
                x = x->right;
            }
        }
        
        z->parent = y;
        if (y == nil_) {
            root_ = z;
        } else if (z->key < y->key) {
            y->left = z;
        } else {
            y->right = z;
        }
        
        insert_fixup(z);
    }
};
```

**关键特性**：
- **时间复杂度**：
  - 插入、删除、查找：O(log n)
- **有序性**：元素按key排序
- **唯一性**：std::set/map保证key唯一，std::multiset/multimap允许重复

### 1.5 std::unordered_map 和 std::unordered_set

**底层结构**：哈希表

```cpp
#include <vector>
#include <list>
#include <functional>

template <typename Key, typename Value, typename Hash = std::hash<Key>>
class HashMap {
private:
    struct Bucket {
        Key key;
        Value value;
    };
    
    using BucketList = std::list<Bucket>;
    std::vector<BucketList> buckets_;
    size_t size_;
    Hash hash_func_;
    
    size_t get_bucket_index(const Key& key) const {
        return hash_func_(key) % buckets_.size();
    }
    
    void rehash(size_t new_bucket_count) {
        std::vector<BucketList> new_buckets(new_bucket_count);
        
        for (auto& bucket_list : buckets_) {
            for (auto& bucket : bucket_list) {
                size_t new_index = hash_func_(bucket.key) % new_bucket_count;
                new_buckets[new_index].push_back(std::move(bucket));
            }
        }
        
        buckets_ = std::move(new_buckets);
    }
    
public:
    HashMap(size_t bucket_count = 16) 
        : buckets_(bucket_count), size_(0) {}
    
    void insert(const Key& key, const Value& value) {
        // 检查负载因子
        if (size_ >= buckets_.size() * 0.75) {
            rehash(buckets_.size() * 2);
        }
        
        size_t index = get_bucket_index(key);
        
        // 检查是否已存在
        for (auto& bucket : buckets_[index]) {
            if (bucket.key == key) {
                bucket.value = value;
                return;
            }
        }
        
        buckets_[index].push_back({key, value});
        ++size_;
    }
    
    std::optional<Value> find(const Key& key) const {
        size_t index = get_bucket_index(key);
        
        for (const auto& bucket : buckets_[index]) {
            if (bucket.key == key) {
                return bucket.value;
            }
        }
        
        return std::nullopt;
    }
    
    bool erase(const Key& key) {
        size_t index = get_bucket_index(key);
        
        for (auto it = buckets_[index].begin(); 
             it != buckets_[index].end(); ++it) {
            if (it->key == key) {
                buckets_[index].erase(it);
                --size_;
                return true;
            }
        }
        
        return false;
    }
};
```

**关键特性**：
- **时间复杂度**：
  - 平均情况：O(1)
  - 最坏情况：O(n)（哈希冲突严重时）
- **负载因子**：通常控制在0.75左右
- **哈希函数**：影响性能的关键

## 2. 迭代器

### 2.1 迭代器类别

C++迭代器分为5个类别，形成继承层次：

```cpp
#include <iterator>
#include <type_traits>

// 输入迭代器：只能读取，只能向前移动
// 示例：std::istream_iterator

// 输出迭代器：只能写入，只能向前移动
// 示例：std::ostream_iterator

// 前向迭代器：可以读写，可以多次读取同一位置
// 示例：std::forward_list迭代器

// 双向迭代器：可以向前和向后移动
// 示例：std::list, std::map迭代器

// 随机访问迭代器：可以常数时间跳到任意位置
// 示例：std::vector, std::array迭代器

// 使用concepts检查迭代器类型（C++20）
template <std::input_iterator It>
void process_input(It begin, It end);

template <std::random_access_iterator It>
void process_random_access(It begin, It end);
```

### 2.2 自定义迭代器

```cpp
#include <iterator>

template <typename T>
class MyContainer {
private:
    std::vector<T> data_;
    
public:
    // 迭代器类
    class Iterator {
    private:
        typename std::vector<T>::iterator it_;
        
    public:
        using iterator_category = std::random_access_iterator_tag;
        using value_type = T;
        using difference_type = std::ptrdiff_t;
        using pointer = T*;
        using reference = T&;
        
        Iterator(typename std::vector<T>::iterator it) : it_(it) {}
        
        reference operator*() const { return *it_; }
        pointer operator->() const { return &(*it_); }
        
        Iterator& operator++() {
            ++it_;
            return *this;
        }
        
        Iterator operator++(int) {
            Iterator temp = *this;
            ++it_;
            return temp;
        }
        
        Iterator& operator--() {
            --it_;
            return *this;
        }
        
        Iterator operator--(int) {
            Iterator temp = *this;
            --it_;
            return temp;
        }
        
        Iterator& operator+=(difference_type n) {
            it_ += n;
            return *this;
        }
        
        Iterator operator+(difference_type n) const {
            return Iterator(it_ + n);
        }
        
        difference_type operator-(const Iterator& other) const {
            return it_ - other.it_;
        }
        
        reference operator[](difference_type n) const {
            return it_[n];
        }
        
        bool operator==(const Iterator& other) const {
            return it_ == other.it_;
        }
        
        bool operator!=(const Iterator& other) const {
            return it_ != other.it_;
        }
        
        bool operator<(const Iterator& other) const {
            return it_ < other.it_;
        }
    };
    
    Iterator begin() { return Iterator(data_.begin()); }
    Iterator end() { return Iterator(data_.end()); }
    
    // const迭代器
    class ConstIterator {
        // 类似实现，但只读
    };
    
    ConstIterator begin() const { return ConstIterator(data_.begin()); }
    ConstIterator end() const { return ConstIterator(data_.end()); }
    
    ConstIterator cbegin() const { return ConstIterator(data_.cbegin()); }
    ConstIterator cend() const { return ConstIterator(data_.cend()); }
};
```

## 3. 算法库

### 3.1 常用算法的时间复杂度

| 算法 | 时间复杂度 | 说明 |
|------|------------|------|
| std::sort | O(n log n) | 内省排序 |
| std::stable_sort | O(n log n) | 归并排序 |
| std::find | O(n) | 线性搜索 |
| std::binary_search | O(log n) | 二分搜索（需已排序） |
| std::lower_bound | O(log n) | 第一个不小于目标的位置 |
| std::upper_bound | O(log n) | 第一个大于目标的位置 |
| std::accumulate | O(n) | 累积 |
| std::transform | O(n) | 转换 |
| std::for_each | O(n) | 遍历 |
| std::copy | O(n) | 复制 |
| std::min/max_element | O(n) | 查找最值 |

### 3.2 自定义算法

```cpp
#include <algorithm>
#include <functional>
#include <ranges>

// 泛型算法示例
template <std::forward_iterator It, typename UnaryPredicate>
bool all_of(It first, It last, UnaryPredicate pred) {
    for (; first != last; ++first) {
        if (!pred(*first)) {
            return false;
        }
    }
    return true;
}

// 使用ranges（C++20）
namespace views = std::views;

void example_ranges() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // 过滤偶数并平方
    auto result = numbers 
        | views::filter([](int x) { return x % 2 == 0; })
        | views::transform([](int x) { return x * x; });
    
    for (auto x : result) {
        std::cout << x << " ";
    }
    // 输出: 4 16 36 64 100
}
```

## 4. 内存分配器

### 4.1 自定义分配器

```cpp
template <typename T>
class MyAllocator {
public:
    using value_type = T;
    
    MyAllocator() noexcept = default;
    
    template <typename U>
    MyAllocator(const MyAllocator<U>&) noexcept {}
    
    T* allocate(size_t n) {
        if (n > std::numeric_limits<size_t>::max() / sizeof(T)) {
            throw std::bad_alloc();
        }
        
        if (auto p = static_cast<T*>(::operator new(n * sizeof(T)))) {
            std::cout << "Allocated " << n << " objects\n";
            return p;
        }
        
        throw std::bad_alloc();
    }
    
    void deallocate(T* p, size_t n) noexcept {
        std::cout << "Deallocated " << n << " objects\n";
        ::operator delete(p);
    }
};

// 使用自定义分配器
std::vector<int, MyAllocator<int>> vec;
vec.push_back(42);
```

### 4.2 内存池分配器

```cpp
template <typename T, size_t PoolSize = 1024>
class PoolAllocator {
private:
    struct Block {
        Block* next;
    };
    
    Block* free_list_;
    char* pool_;
    size_t pool_used_;
    
public:
    using value_type = T;
    
    PoolAllocator() {
        pool_ = static_cast<char*>(::operator new(PoolSize));
        free_list_ = nullptr;
        pool_used_ = 0;
    }
    
    ~PoolAllocator() {
        ::operator delete(pool_);
    }
    
    T* allocate(size_t n = 1) {
        if (free_list_) {
            Block* block = free_list_;
            free_list_ = free_list_->next;
            return reinterpret_cast<T*>(block);
        }
        
        if (pool_used_ + sizeof(T) * n > PoolSize) {
            throw std::bad_alloc();
        }
        
        T* result = reinterpret_cast<T*>(pool_ + pool_used_);
        pool_used_ += sizeof(T) * n;
        return result;
    }
    
    void deallocate(T* p, size_t n = 1) noexcept {
        Block* block = reinterpret_cast<Block*>(p);
        block->next = free_list_;
        free_list_ = block;
    }
};
```

## 5. 函数对象

### 5.1 lambda表达式

```cpp
#include <functional>

// lambda捕获方式
void lambda_examples() {
    int x = 10;
    
    // 值捕获
    auto f1 = [x](int y) { return x + y; };
    
    // 引用捕获
    auto f2 = [&x](int y) { x += y; return x; };
    
    // 混合捕获
    auto f3 = [x, &y](int z) { return x + y + z; };
    
    // 初始化捕获（C++14）
    auto f4 = [ptr = std::make_unique<int>(42)]() { return *ptr; };
    
    // 泛型lambda（C++14）
    auto f5 = [](auto&& x) { return x * 2; };
    
    // constexpr lambda（C++17）
    constexpr auto f6 = [](int x) { return x * x; };
    static_assert(f6(5) == 25);
}
```

### 5.2 std::function

```cpp
#include <functional>

void function_examples() {
    // 存储函数指针
    std::function<int(int, int)> add = [](int a, int b) { 
        return a + b; 
    };
    
    // 存储成员函数
    struct Calculator {
        int multiply(int a, int b) const { return a * b; }
    };
    
    Calculator calc;
    std::function<int(int, int)> mul = 
        std::bind(&Calculator::multiply, &calc, 
                  std::placeholders::_1, std::placeholders::_2);
    
    // 存储函数对象
    struct Adder {
        int operator()(int a, int b) const { return a + b; }
    };
    
    std::function<int(int, int)> adder = Adder{};
}
```

## 6. 性能优化建议

### 6.1 选择合适的容器

| 场景 | 推荐容器 | 原因 |
|------|----------|------|
| 随机访问 | std::vector | O(1)访问，缓存友好 |
| 频繁头尾插入 | std::deque | O(1)头尾操作 |
| 中间插入删除 | std::list | O(1)插入删除 |
| 有序存储 | std::map/set | 自动排序，O(log n)操作 |
| 快速查找 | std::unordered_map/set | O(1)平均查找 |

### 6.2 避免不必要的拷贝

```cpp
// 使用const引用
void process(const std::vector<int>& vec);

// 使用移动语义
std::vector<int> create_large_vector() {
    std::vector<int> result(1000000);
    // ... 填充数据
    return result;  // RVO或移动语义
}

// 使用std::move
std::vector<int> vec1 = /* ... */;
std::vector<int> vec2 = std::move(vec1);  // 无拷贝

// 使用std::forward（完美转发）
template <typename T>
void wrapper(T&& arg) {
    process(std::forward<T>(arg));
}
```

### 6.3 预分配内存

```cpp
// 预分配vector大小
std::vector<int> vec;
vec.reserve(1000000);  // 避免多次扩容

// 预分配unordered_map桶数
std::unordered_map<int, int> map;
map.reserve(1000000);
```

## 7. 调试和性能分析

### 7.1 使用地址清理器

```bash
# 编译时启用
g++ -fsanitize=address -g your_code.cpp

# 运行
./a.out
```

### 7.2 使用性能分析工具

```bash
# 使用gprof
g++ -pg your_code.cpp -o your_program
./your_program
gprof your_program gmon.out > analysis.txt

# 使用perf（Linux）
perf record ./your_program
perf report
```

## 8. 本章小结

- STL容器各有特点，需要根据场景选择
- 理解迭代器类别对编写泛型代码很重要
- 算法库提供了高效的实现，优先使用STL算法
- 自定义分配器可以优化内存管理
- 函数对象提供了灵活的回调机制
- 注意性能优化，避免不必要的拷贝和内存分配

## 9. 参考资源

- C++参考文档: https://en.cppreference.com/w/
- 《Effective STL》by Scott Meyers
- 《C++ STL中文版》by Nicolai M. Josuttis
- STL源码剖析: https://github.com/gcc-mirror/gcc