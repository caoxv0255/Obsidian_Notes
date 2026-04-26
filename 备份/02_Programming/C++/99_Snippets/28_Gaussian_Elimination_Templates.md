---
type: snippets
topic: gaussian_elimination_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/线性代数, 高斯消元, 方程组, Snippets]
---

# 高斯消元模板

> 用于解线性方程组、判无解/多解、求唯一解。

## 1) 实数高斯消元

```cpp
#include <cmath>
#include <vector>
using namespace std;

struct GaussianElimination {
    static constexpr double EPS = 1e-9;

    int equations;
    int variables;
    vector<vector<double>> matrix;
    vector<double> solution;
    vector<int> where;

    GaussianElimination(int equations, int variables)
        : equations(equations), variables(variables),
          matrix(equations, vector<double>(variables + 1, 0.0)),
          solution(variables, 0.0), where(variables, -1) {}

    void setEquation(int row, const vector<double>& coefficients, double constant) {
        for (int col = 0; col < variables; ++col) {
            matrix[row][col] = coefficients[col];
        }
        matrix[row][variables] = constant;
    }

    int solve() {
        fill(where.begin(), where.end(), -1);

        int row = 0;
        int rank = 0;
        for (int col = 0; col < variables && row < equations; ++col) {
            int pivot = row;
            for (int candidate = row; candidate < equations; ++candidate) {
                if (fabs(matrix[candidate][col]) > fabs(matrix[pivot][col])) {
                    pivot = candidate;
                }
            }

            if (fabs(matrix[pivot][col]) < EPS) {
                continue;
            }

            swap(matrix[pivot], matrix[row]);
            where[col] = row;

            double divisor = matrix[row][col];
            for (int currentCol = col; currentCol <= variables; ++currentCol) {
                matrix[row][currentCol] /= divisor;
            }

            for (int other = 0; other < equations; ++other) {
                if (other == row) continue;
                double factor = matrix[other][col];
                if (fabs(factor) < EPS) continue;
                for (int currentCol = col; currentCol <= variables; ++currentCol) {
                    matrix[other][currentCol] -= factor * matrix[row][currentCol];
                }
            }

            ++row;
            ++rank;
        }

        for (int currentRow = row; currentRow < equations; ++currentRow) {
            if (fabs(matrix[currentRow][variables]) > EPS) {
                return 0;
            }
        }

        fill(solution.begin(), solution.end(), 0.0);
        for (int col = 0; col < variables; ++col) {
            if (where[col] != -1) {
                solution[col] = matrix[where[col]][variables];
            }
        }

        return rank < variables ? 2 : 1;
    }
};
```

## 使用建议

- `0` 表示无解，`1` 表示唯一解，`2` 表示多解
- 如果是 XOR 方程组，把浮点运算改成模 2 即可
- 题目要的是“存在性”还是“具体解”，先确认清楚再写模板
