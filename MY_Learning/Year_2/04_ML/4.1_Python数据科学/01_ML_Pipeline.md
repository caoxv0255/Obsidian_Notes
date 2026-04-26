---
type: workflow
topic: ml_pipeline
category: machine_learning
difficulty: intermediate
prerequisites: []
acm_relevant: true
created: 2026-02-20
status: complete
---

# 机器学习全流程参考

> 快速参考：从数据加载到模型部署的端到端流程

## 流程概览

```
数据加载 → 数据预处理 → 特征工程 → 模型训练 → 模型评估 → 模型部署
```

## 快速参考

### 1. 数据加载

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# 读取数据
df = pd.read_csv('data.csv')

# 分离特征和标签
X = df.drop('target', axis=1)
y = df['target']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)
```

### 2. 数据预处理

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 数值列处理
numeric_features = ['age', 'salary', 'score']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# 分类列处理
categorical_features = ['city', 'gender']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# 组合处理器
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# 应用预处理
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)
```

### 3. 特征工程

```python
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.decomposition import PCA

# 特征选择（单变量统计检验）
selector = SelectKBest(score_func=f_classif, k=10)
X_train_selected = selector.fit_transform(X_train_processed, y_train)
X_test_selected = selector.transform(X_test_processed)

# 递归特征消除
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rfe = RFE(estimator=rf, n_features_to_select=10)
X_train_rfe = rfe.fit_transform(X_train_processed, y_train)
X_test_rfe = rfe.transform(X_test_processed)

# 特征重要性
rf.fit(X_train_processed, y_train)
importances = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

# 降维（PCA）
pca = PCA(n_components=0.95)  # 保留95%方差
X_train_pca = pca.fit_transform(X_train_processed)
X_test_pca = pca.transform(X_test_processed)
```

### 4. 模型训练

```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

# 定义模型
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', probability=True)
}

# 训练和交叉验证
results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_train_processed, y_train, cv=5, scoring='accuracy')
    results[name] = {
        'mean_score': scores.mean(),
        'std_score': scores.std()
    }
    print(f"{name}: {scores.mean():.4f} (+/- {scores.std():.4f})")

# 选择最佳模型
best_model_name = max(results, key=lambda x: results[x]['mean_score'])
best_model = models[best_model_name]
best_model.fit(X_train_processed, y_train)
```

### 5. 超参数调优

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# 网格搜索
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train_processed, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳分数: {grid_search.best_score_:.4f}")
best_model = grid_search.best_estimator_

# 随机搜索
from scipy.stats import randint
param_dist = {
    'n_estimators': randint(50, 200),
    'max_depth': randint(10, 50),
    'min_samples_split': randint(2, 10)
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_dist,
    n_iter=50,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)
random_search.fit(X_train_processed, y_train)
best_model = random_search.best_estimator_
```

### 6. 模型评估

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)

# 预测
y_pred = best_model.predict(X_test_processed)
y_pred_proba = best_model.predict_proba(X_test_processed)[:, 1]

# 分类指标
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# 分类报告
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ROC-AUC
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
auc_score = roc_auc_score(y_test, y_pred_proba)
print(f"\nROC-AUC Score: {auc_score:.4f}")

# 绘制 ROC 曲线
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'ROC (AUC = {auc_score:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

### 7. 模型保存与加载

```python
import joblib
import pickle

# 保存模型（joblib - 推荐）
joblib.dump(best_model, 'model.pkl')
joblib.dump(preprocessor, 'preprocessor.pkl')

# 保存模型（pickle）
with open('model.pickle', 'wb') as f:
    pickle.dump(best_model, f)

# 加载模型
loaded_model = joblib.load('model.pkl')
loaded_preprocessor = joblib.load('preprocessor.pkl')

# 使用加载的模型预测
X_new_processed = loaded_preprocessor.transform(X_new)
prediction = loaded_model.predict(X_new_processed)
```

### 8. 模型部署示例

```python
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# 加载模型和预处理器
model = joblib.load('model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # 获取输入数据
    data = request.json
    
    # 转换为 DataFrame
    df = pd.DataFrame([data])
    
    # 预处理
    df_processed = preprocessor.transform(df)
    
    # 预测
    prediction = model.predict(df_processed)
    probability = model.predict_proba(df_processed)
    
    # 返回结果
    return jsonify({
        'prediction': int(prediction[0]),
        'probability': probability[0].tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### 9. 完整 Pipeline 示例

```python
from sklearn.pipeline import Pipeline

# 创建完整流程
full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('selector', SelectKBest(score_func=f_classif, k=10)),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# 训练
full_pipeline.fit(X_train, y_train)

# 预测
y_pred = full_pipeline.predict(X_test)

# 评估
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# 保存
joblib.dump(full_pipeline, 'full_pipeline.pkl')
```

## 最佳实践

| 实践 | 说明 |
|------|------|
| 数据划分 | 使用 stratify 保持类别分布 |
| 预处理 | 训练集 fit，测试集只 transform |
| 交叉验证 | 评估模型稳定性 |
| 超参数调优 | 先粗调后细调 |
| 模型保存 | 同时保存预处理器 |
| 版本控制 | 记录模型版本和参数 |

## 常见问题

**Q: 如何处理类别不平衡？**
```python
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_processed, y_train)
```

**Q: 如何处理时间序列？**
```python
# 按时间划分，不要随机打乱
train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]
```

## 相关链接
- [[temp_data_cleaning|数据清洗]]
- [[temp_data_analysis|数据分析]]
- [[temp_pytorch_index|PyTorch]]