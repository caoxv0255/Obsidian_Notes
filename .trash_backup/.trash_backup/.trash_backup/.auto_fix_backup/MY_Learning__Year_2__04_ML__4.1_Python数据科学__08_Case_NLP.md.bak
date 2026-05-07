---
type: case_study
topic: nlp
category: case_studies
difficulty: advanced
prerequisites: [[temp_data_cleaning, temp_ml_pipeline]]
acm_relevant: true
created: 2026-02-20
status: complete
---

# 自然语言处理案例

> 端到端 NLP 应用：文本预处理、词向量化、情感分析、文本分类和命名实体识别

## 案例目标

构建一个完整的 NLP 应用系统，包括文本预处理、词向量化、情感分析、文本分类和命名实体识别。

## 环境准备

```python
import nltk
import spacy
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

# 下载必要的 NLTK 数据
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# 加载 SpaCy 模型
nlp = spacy.load('en_core_web_sm')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

## 文本预处理

```python
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

def preprocess_text(text, lowercase=True, remove_stopwords=True, 
                   remove_punctuation=True, lemmatize=True):
    """文本预处理"""
    
    # 1. 转小写
    if lowercase:
        text = text.lower()
    
    # 2. 移除 URL
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # 3. 移除 HTML 标签
    text = re.sub(r'<.*?>', '', text)
    
    # 4. 移除标点符号
    if remove_punctuation:
        text = re.sub(r'[^\w\s]', '', text)
    
    # 5. 移除数字
    text = re.sub(r'\d+', '', text)
    
    # 6. 移除特殊字符
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # 7. 分词
    tokens = word_tokenize(text)
    
    # 8. 移除停用词
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]
    
    # 9. 词干提取（可选）
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    # 10. 词形还原（推荐）
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # 11. 移除空词
    tokens = [token for token in tokens if len(token) > 1]
    
    return tokens, stemmed_tokens

def preprocess_text_list(texts):
    """批量预处理文本"""
    processed_texts = []
    for text in texts:
        tokens, _ = preprocess_text(text)
        processed_texts.append(' '.join(tokens))
    return processed_texts

# 示例
sample_text = "The quick brown fox jumps over the lazy dog! Visit https://example.com"
tokens, stemmed = preprocess_text(sample_text)
print("原始文本:", sample_text)
print("处理后词列表:", tokens)
print("处理后文本:", ' '.join(tokens))
```

## 词向量化

```python
def vectorize_text(texts, method='tfidf'):
    """文本向量化"""
    
    if method == 'count':
        # 词袋模型
        vectorizer = CountVectorizer(max_features=5000, ngram_range=(1, 2))
    elif method == 'tfidf':
        # TF-IDF
        vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    elif method == 'binary':
        # 二值化
        vectorizer = CountVectorizer(max_features=5000, binary=True)
    else:
        raise ValueError(f"Unknown method: {method}")
    
    # 训练并转换
    X = vectorizer.fit_transform(texts)
    
    return X, vectorizer

def get_feature_importance(vectorizer, top_n=20):
    """获取最重要的特征词"""
    feature_names = vectorizer.get_feature_names_out()
    importance = vectorizer.idf_ if hasattr(vectorizer, 'idf_') else None
    
    if importance is not None:
        importance_df = pd.DataFrame({
            'word': feature_names,
            'idf': importance
        }).sort_values('idf', ascending=False)
    else:
        importance_df = pd.DataFrame({'word': feature_names})
    
    return importance_df.head(top_n)
```

## 词云可视化

```python
def generate_wordcloud(texts, max_words=100):
    """生成词云"""
    
    # 合并所有文本
    all_text = ' '.join(texts)
    
    # 生成词云
    wordcloud = WordCloud(width=800, height=400, 
                         background_color='white',
                         max_words=max_words).generate(all_text)
    
    # 绘制词云
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('词云')
    plt.show()
    
    return wordcloud
```

## 情感分析

```python
from textblob import TextBlob

def analyze_sentiment_textblob(text):
    """使用 TextBlob 进行情感分析"""
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        'polarity': sentiment.polarity,  # -1 到 1，负数表示负面，正数表示正面
        'subjectivity': sentiment.subjectivity  # 0 到 1，0 表示客观，1 表示主观
    }

def analyze_sentiment_vader(text):
    """使用 VADER 进行情感分析"""
    from nltk.sentiment import SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    return scores

def classify_sentiment(polarity):
    """分类情感"""
    if polarity > 0.05:
        return 'positive'
    elif polarity < -0.05:
        return 'negative'
    else:
        return 'neutral'

def batch_sentiment_analysis(texts, method='textblob'):
    """批量情感分析"""
    sentiments = []
    for text in texts:
        if method == 'textblob':
            sentiment = analyze_sentiment_textblob(text)
            sentiments.append({
                'text': text,
                'polarity': sentiment['polarity'],
                'subjectivity': sentiment['subjectivity'],
                'sentiment': classify_sentiment(sentiment['polarity'])
            })
        elif method == 'vader':
            sentiment = analyze_sentiment_vader(text)
            sentiments.append({
                'text': text,
                'compound': sentiment['compound'],
                'sentiment': classify_sentiment(sentiment['compound'])
            })
    return pd.DataFrame(sentiments)
```

## 文本分类

```python
def train_text_classifier(X, y, model_type='logistic'):
    """训练文本分类器"""
    
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 选择模型
    if model_type == 'logistic':
        model = LogisticRegression(max_iter=1000, random_state=42)
    elif model_type == 'svm':
        model = SVC(kernel='linear', random_state=42)
    elif model_type == 'naive_bayes':
        model = MultinomialNB()
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    
    # 训练模型
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    
    # 评估
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    return model, report, cm

def plot_confusion_matrix(cm, class_names):
    """绘制混淆矩阵"""
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names)
    plt.title('混淆矩阵')
    plt.ylabel('真实标签')
    plt.xlabel('预测标签')
    plt.show()
```

## 命名实体识别

```python
def extract_entities_spacy(text):
    """使用 SpaCy 提取命名实体"""
    doc = nlp(text)
    
    entities = []
    for ent in doc.ents:
        entities.append({
            'text': ent.text,
            'label': ent.label_,
            'description': spacy.explain(ent.label_),
            'start': ent.start_char,
            'end': ent.end_char
        })
    
    return entities

def visualize_entities_spacy(text):
    """可视化命名实体"""
    doc = nlp(text)
    
    # 使用 displacy 可视化
    from spacy import displacy
    displacy.render(doc, style='ent', jupyter=True)
    
    return doc.ents

def extract_entities_nltk(text):
    """使用 NLTK 提取命名实体"""
    tokens = word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.ne_chunk(tagged, binary=False)
    
    entity_list = []
    for entity in entities:
        if hasattr(entity, 'label'):
            entity_name = ' '.join(c[0] for c in entity.leaves())
            entity_type = entity.label()
            entity_list.append({'name': entity_name, 'type': entity_type})
    
    return entity_list
```

## 主题建模

```python
from sklearn.decomposition import LatentDirichletAllocation

def perform_topic_modeling(texts, n_topics=5, n_top_words=10):
    """LDA 主题建模"""
    
    # 创建词频矩阵
    vectorizer = CountVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(texts)
    
    # LDA 模型
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)
    
    # 提取主题
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    
    for topic_idx, topic in enumerate(lda.components_):
        top_words_idx = topic.argsort()[:-n_top_words - 1:-1]
        top_words = [feature_names[i] for i in top_words_idx]
        topics.append({
            'topic_id': topic_idx,
            'words': top_words,
            'weights': topic[top_words_idx]
        })
    
    return lda, topics

def print_topics(topics):
    """打印主题"""
    for topic in topics:
        print(f"\n主题 {topic['topic_id']}:")
        for word, weight in zip(topic['words'], topic['weights']):
            print(f"  {word}: {weight:.4f}")
```

## 文本相似度

```python
from sklearn.metrics.pairwise import cosine_similarity

def calculate_text_similarity(texts, method='cosine'):
    """计算文本相似度"""
    
    # 向量化
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(texts)
    
    # 计算相似度矩阵
    if method == 'cosine':
        similarity_matrix = cosine_similarity(X)
    
    return similarity_matrix

def plot_similarity_matrix(similarity_matrix, labels=None):
    """绘制相似度矩阵"""
    plt.figure(figsize=(10, 8))
    sns.heatmap(similarity_matrix, annot=True, cmap='coolwarm', 
                xticklabels=labels, yticklabels=labels)
    plt.title('文本相似度矩阵')
    plt.show()
```

## 完整 NLP 流程

```python
def full_nlp_pipeline(texts, labels=None, task='classification'):
    """完整 NLP 流程"""
    
    # 1. 文本预处理
    print("=== 文本预处理 ===")
    processed_texts = preprocess_text_list(texts)
    
    # 2. 生成词云
    print("\n=== 词云 ===")
    wordcloud = generate_wordcloud(processed_texts)
    
    # 3. 文本向量化
    print("\n=== 文本向量化 ===")
    X, vectorizer = vectorize_text(processed_texts, method='tfidf')
    
    # 4. 特征重要性
    print("\n=== 重要特征词 ===")
    importance_df = get_feature_importance(vectorizer)
    print(importance_df)
    
    # 5. 情感分析
    print("\n=== 情感分析 ===")
    sentiments = batch_sentiment_analysis(texts, method='textblob')
    print(sentiments.head())
    
    # 6. 命名实体识别
    print("\n=== 命名实体识别 ===")
    for i, text in enumerate(texts[:3]):
        print(f"\n文本 {i+1}: {text}")
        entities = extract_entities_spacy(text)
        for ent in entities[:5]:
            print(f"  {ent['text']} -> {ent['label']} ({ent['description']})")
    
    # 7. 文本分类（如果有标签）
    if labels is not None and task == 'classification':
        print("\n=== 文本分类 ===")
        model, report, cm = train_text_classifier(X, labels)
        print(report)
        plot_confusion_matrix(cm, class_names=list(set(labels)))
    
    # 8. 主题建模
    print("\n=== 主题建模 ===")
    lda, topics = perform_topic_modeling(processed_texts, n_topics=3)
    print_topics(topics)
    
    # 9. 文本相似度
    print("\n=== 文本相似度 ===")
    similarity_matrix = calculate_text_similarity(processed_texts[:10])
    plot_similarity_matrix(similarity_matrix)
    
    return {
        'processed_texts': processed_texts,
        'vectorizer': vectorizer,
        'sentiments': sentiments,
        'lda': lda,
        'topics': topics,
        'similarity_matrix': similarity_matrix
    }

# 示例数据
sample_texts = [
    "I love this product! It's amazing and works perfectly.",
    "This is the worst purchase I've ever made. Terrible quality.",
    "The product is okay, nothing special but not bad either.",
    "Great service and fast delivery. Highly recommended!",
    "Disappointed with the quality. Expected much better.",
    "Average product, meets basic requirements."
]

sample_labels = ['positive', 'negative', 'neutral', 'positive', 'negative', 'neutral']

# 运行完整流程
results = full_nlp_pipeline(sample_texts, sample_labels, task='classification')
```

## 最佳实践

| 实践 | 说明 |
|------|------|
| 预处理彻底 | 确保数据干净一致 |
| 选择合适向量化 | 根据任务选择 BoW、TF-IDF 或词嵌入 |
| 平衡数据集 | 处理类别不平衡问题 |
| 交叉验证 | 使用 k-fold 交叉验证评估模型 |
领域适应 | 使用领域特定的停用词和词典 |

## 常见问题

**Q: 如何处理中文文本？**
```python
import jieba
def preprocess_chinese(text):
    tokens = jieba.cut(text)
    tokens = [token for token in tokens if token.strip()]
    return tokens
```

**Q: 如何提高情感分析准确率？**
```python
# 使用预训练模型
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
result = sentiment_pipeline("I love this product!")
```

## 相关链接
- [[temp_data_cleaning|数据清洗]]
- [[temp_ml_pipeline|ML 全流程]]
- [[temp_pytorch_index|PyTorch]]