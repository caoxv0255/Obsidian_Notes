---
type: snippets
topic: geometry_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/计算几何, 叉积, 凸包, Snippets]
---

# 计算几何模板

> 先掌握点、向量、叉积，再往后就是线段相交和凸包。

## 1) 基础几何工具

```cpp
#include <algorithm>
#include <cmath>
using namespace std;

struct Point {
    long long x;
    long long y;
};

Point operator-(const Point& left, const Point& right) {
    return {left.x - right.x, left.y - right.y};
}

long long cross(const Point& left, const Point& right) {
    return left.x * right.y - left.y * right.x;
}

long long cross(const Point& a, const Point& b, const Point& c) {
    return cross(b - a, c - a);
}

long long dot(const Point& left, const Point& right) {
    return left.x * right.x + left.y * right.y;
}

int sign(long long value) {
    if (value > 0) return 1;
    if (value < 0) return -1;
    return 0;
}

bool onSegment(const Point& a, const Point& b, const Point& p) {
    if (sign(cross(a, b, p)) != 0) return false;
    return min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x) &&
           min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y);
}

bool segmentsIntersect(const Point& a, const Point& b, const Point& c, const Point& d) {
    int ab_c = sign(cross(a, b, c));
    int ab_d = sign(cross(a, b, d));
    int cd_a = sign(cross(c, d, a));
    int cd_b = sign(cross(c, d, b));

    if (ab_c == 0 && onSegment(a, b, c)) return true;
    if (ab_d == 0 && onSegment(a, b, d)) return true;
    if (cd_a == 0 && onSegment(c, d, a)) return true;
    if (cd_b == 0 && onSegment(c, d, b)) return true;

    return ab_c * ab_d < 0 && cd_a * cd_b < 0;
}
```

## 2) 凸包（Monotonic Chain）

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct Point {
    long long x;
    long long y;

    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
};

Point operator-(const Point& left, const Point& right) {
    return {left.x - right.x, left.y - right.y};
}

long long cross(const Point& left, const Point& right) {
    return left.x * right.y - left.y * right.x;
}

long long cross(const Point& a, const Point& b, const Point& c) {
    return cross(b - a, c - a);
}

vector<Point> convexHull(vector<Point> points) {
    sort(points.begin(), points.end());
    points.erase(unique(points.begin(), points.end(), [](const Point& left, const Point& right) {
        return left.x == right.x && left.y == right.y;
    }), points.end());

    if (points.size() <= 1) return points;

    vector<Point> hull;
    for (const auto& point : points) {
        while (hull.size() >= 2 && cross(hull[hull.size() - 2], hull.back(), point) <= 0) {
            hull.pop_back();
        }
        hull.push_back(point);
    }

    size_t lowerSize = hull.size();
    for (int index = static_cast<int>(points.size()) - 2; index >= 0; --index) {
        const auto& point = points[index];
        while (hull.size() > lowerSize && cross(hull[hull.size() - 2], hull.back(), point) <= 0) {
            hull.pop_back();
        }
        hull.push_back(point);
    }

    if (!hull.empty()) {
        hull.pop_back();
    }

    return hull;
}
```

## 3) 多边形面积

```cpp
#include <vector>
using namespace std;

struct Point {
    long long x;
    long long y;
};

long long polygonArea2(const vector<Point>& polygon) {
    long long area2 = 0;
    int n = static_cast<int>(polygon.size());
    for (int index = 0; index < n; ++index) {
        const Point& current = polygon[index];
        const Point& next = polygon[(index + 1) % n];
        area2 += current.x * next.y - current.y * next.x;
    }
    return area2;
}
```

## 使用建议

- 判断方向 / 旋转关系：叉积
- 判断线段相交：先判跨立，再判端点共线
- 求凸包：Monotonic Chain 最通用
- 多边形面积：直接用鞋带公式
