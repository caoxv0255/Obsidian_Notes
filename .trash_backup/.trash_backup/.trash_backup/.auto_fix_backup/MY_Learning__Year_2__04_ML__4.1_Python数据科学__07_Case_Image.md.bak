---
type: case_study
topic: image_processing
category: case_studies
difficulty: advanced
prerequisites: [[temp_data_cleaning, temp_ml_pipeline]]
acm_relevant: true
created: 2026-02-20
status: complete
---

# 图像处理案例

> 端到端图像处理：图像增强、边缘检测、图像分割和特征提取

## 案例目标

构建一个完整的图像处理系统，包括图像读取与保存、图像增强、边缘检测、图像分割和特征提取。

## 环境准备

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters, segmentation, feature, exposure
from skimage.color import rgb2gray, label2rgb
from skimage.feature import hog
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

## 图像读取与保存

```python
def read_image(image_path, color_mode='rgb'):
    """读取图像"""
    if color_mode == 'rgb':
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif color_mode == 'gray':
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return image

def save_image(image, output_path):
    """保存图像"""
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, image)

# 示例
# image = read_image('input.jpg')
# save_image(image, 'output.jpg')
```

## 图像增强

```python
def enhance_image(image):
    """图像增强"""
    
    # 1. 亮度调整
    brightness = np.ones(image.shape, dtype='uint8') * 50
    brightened = cv2.add(image, brightness)
    
    # 2. 对比度调整
    contrast = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
    
    # 3. 直方图均衡化
    if len(image.shape) == 2:
        equalized = cv2.equalizeHist(image)
    else:
        # 对每个通道分别均衡化
        yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
        equalized = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB)
    
    # 4. 伽马校正
    gamma = 1.5
    gamma_corrected = np.power(image / 255.0, gamma) * 255.0
    gamma_corrected = np.uint8(gamma_corrected)
    
    # 5. 降噪
    denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    
    # 6. 锐化
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    
    return {
        'original': image,
        'brightened': brightened,
        'contrast': contrast,
        'equalized': equalized,
        'gamma_corrected': gamma_corrected,
        'denoised': denoised,
        'sharpened': sharpened
    }

# 可视化增强效果
def plot_enhanced_images(enhanced_dict):
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.ravel()
    
    titles = ['原始图像', '亮度增强', '对比度增强', '直方图均衡化',
              '伽马校正', '降噪', '锐化', '占位']
    
    for i, (title, img) in enumerate(enhanced_dict.items()):
        if len(img.shape) == 2:
            axes[i].imshow(img, cmap='gray')
        else:
            axes[i].imshow(img)
        axes[i].set_title(titles[i])
        axes[i].axis('off')
    
    axes[-1].axis('off')
    plt.tight_layout()
    plt.show()
```

## 边缘检测

```python
def detect_edges(image):
    """边缘检测"""
    
    # 转换为灰度图
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image.copy()
    
    # 1. Sobel 算子
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel = np.uint8(sobel / sobel.max() * 255)
    
    # 2. Laplacian 算子
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    
    # 3. Canny 边缘检测
    canny = cv2.Canny(gray, 50, 150)
    
    # 4. Prewitt 算子
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt_x = cv2.filter2D(gray, -1, kernelx)
    prewitt_y = cv2.filter2D(gray, -1, kernely)
    prewitt = np.sqrt(prewitt_x**2 + prewitt_y**2)
    prewitt = np.uint8(prewitt / prewitt.max() * 255)
    
    return {
        'original': gray,
        'sobel': sobel,
        'laplacian': laplacian,
        'canny': canny,
        'prewitt': prewitt
    }

def plot_edges(edges_dict):
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.ravel()
    
    titles = ['原始灰度图', 'Sobel', 'Laplacian', 'Canny', 'Prewitt', '占位']
    
    for i, (title, img) in enumerate(edges_dict.items()):
        axes[i].imshow(img, cmap='gray')
        axes[i].set_title(titles[i])
        axes[i].axis('off')
    
    axes[-1].axis('off')
    plt.tight_layout()
    plt.show()
```

## 图像分割

```python
def segment_image(image):
    """图像分割"""
    
    # 转换为灰度图
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image.copy()
    
    # 1. 阈值分割
    _, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 2. 自适应阈值
    binary_adaptive = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    
    # 3. K-means 聚类分割
    if len(image.shape) == 3:
        pixel_values = image.reshape((-1, 3))
    else:
        pixel_values = gray.reshape((-1, 1))
    
    pixel_values = np.float32(pixel_values)
    k = 3
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    centers = np.uint8(centers)
    segmented_kmeans = centers[labels.flatten()]
    segmented_kmeans = segmented_kmeans.reshape(image.shape)
    
    # 4. 分水岭算法
    _, markers = cv2.connectedComponents(binary_otsu)
    markers = markers + 1
    markers[gray == 0] = 0
    markers = cv2.watershed(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB), markers)
    watershed = image.copy()
    watershed[markers == -1] = [255, 0, 0]
    
    # 5. 区域生长（简化版）
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    opened = cv2.morphologyEx(binary_otsu, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opened, kernel, iterations=3)
    
    return {
        'original': gray,
        'binary_otsu': binary_otsu,
        'binary_adaptive': binary_adaptive,
        'segmented_kmeans': segmented_kmeans,
        'watershed': watershed
    }

def plot_segments(segments_dict):
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.ravel()
    
    titles = ['原始灰度图', 'Otsu阈值', '自适应阈值', 'K-means聚类', '分水岭', '占位']
    
    for i, (title, img) in enumerate(segments_dict.items()):
        if len(img.shape) == 2:
            axes[i].imshow(img, cmap='gray')
        else:
            axes[i].imshow(img)
        axes[i].set_title(titles[i])
        axes[i].axis('off')
    
    axes[-1].axis('off')
    plt.tight_layout()
    plt.show()
```

## 特征提取

```python
def extract_features(image):
    """特征提取"""
    
    # 转换为灰度图
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image.copy()
    
    # 1. HOG 特征
    features_hog, hog_image = hog(
        gray, orientations=9, pixels_per_cell=(8, 8),
        cells_per_block=(2, 2), visualize=True
    )
    
    # 2. LBP (Local Binary Pattern)
    from skimage.feature import local_binary_pattern
    lbp = local_binary_pattern(gray, P=8, R=1, method='uniform')
    
    # 3. 角点检测 (Harris)
    gray_float = np.float32(gray)
    corners = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)
    corners = cv2.dilate(corners, None)
    corners_img = image.copy()
    corners_img[corners > 0.01 * corners.max()] = [255, 0, 0]
    
    # 4. ORB 特征点
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(gray, None)
    orb_img = cv2.drawKeypoints(gray, keypoints, None, color=(0, 255, 0), flags=0)
    
    # 5. SIFT 特征点（如果可用）
    try:
        sift = cv2.SIFT_create()
        keypoints_sift, descriptors_sift = sift.detectAndCompute(gray, None)
        sift_img = cv2.drawKeypoints(gray, keypoints_sift, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    except:
        sift_img = gray.copy()
        print("SIFT not available")
    
    # 6. 边缘特征（Canny）
    edges = cv2.Canny(gray, 50, 150)
    
    return {
        'original': gray,
        'hog_image': hog_image,
        'lbp': lbp,
        'corners': corners_img,
        'orb': orb_img,
        'sift': sift_img,
        'edges': edges,
        'hog_features': features_hog
    }

def plot_features(features_dict):
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.ravel()
    
    titles = ['原始灰度图', 'HOG', 'LBP', 'Harris角点', 'ORB特征', 'SIFT特征', 'Canny边缘', '占位']
    
    for i, (title, img) in enumerate(features_dict.items()):
        if title == 'hog_features':
            continue
        if len(img.shape) == 2:
            axes[i].imshow(img, cmap='gray')
        else:
            axes[i].imshow(img)
        axes[i].set_title(titles[i])
        axes[i].axis('off')
    
    axes[-1].axis('off')
    plt.tight_layout()
    plt.show()
```

## 卷积操作

```python
def convolve_image(image, kernel):
    """卷积操作"""
    return cv2.filter2D(image, -1, kernel)

def demonstrate_convolution(image):
    """演示不同卷积核的效果"""
    
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image.copy()
    
    # 定义不同的卷积核
    kernels = {
        '原始': np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        '锐化': np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]),
        '边缘检测': np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
        '浮雕': np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
        '高斯模糊': (1/16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]),
        '垂直边缘': np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
        '水平边缘': np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    }
    
    results = {'original': gray}
    for name, kernel in kernels.items():
        if name != '原始':
            results[name] = convolve_image(gray, kernel)
    
    # 可视化
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.ravel()
    
    for i, (title, img) in enumerate(results.items()):
        axes[i].imshow(img, cmap='gray')
        axes[i].set_title(title)
        axes[i].axis('off')
    
    axes[-1].axis('off')
    plt.tight_layout()
    plt.show()
    
    return results
```

## 完整分析流程

```python
def full_image_analysis(image_path):
    """完整图像分析流程"""
    
    # 1. 读取图像
    image = read_image(image_path, color_mode='rgb')
    
    # 2. 图像增强
    enhanced = enhance_image(image)
    plot_enhanced_images(enhanced)
    
    # 3. 边缘检测
    edges = detect_edges(image)
    plot_edges(edges)
    
    # 4. 图像分割
    segments = segment_image(image)
    plot_segments(segments)
    
    # 5. 特征提取
    features = extract_features(image)
    plot_features(features)
    
    # 6. 卷积演示
    conv_results = demonstrate_convolution(image)
    
    print(f"HOG 特征维度: {features['hog_features'].shape}")
    
    return {
        'enhanced': enhanced,
        'edges': edges,
        'segments': segments,
        'features': features,
        'convolution': conv_results
    }

# 使用示例
# results = full_image_analysis('input.jpg')
```

## 最佳实践

| 实践 | 说明 |
|------|------|
| 数据预处理 | 统一图像尺寸和归一化 |
| 选择合适算法 | 根据任务选择最佳方法 |
| 参数调优 | 通过实验确定最优参数 |
| 计算效率 | 考虑算法的时间和空间复杂度 |
| 可视化验证 | 每一步都可视化检查结果 |

## 相关链接
- [[temp_data_cleaning|数据清洗]]
- [[temp_ml_pipeline|ML 全流程]]
- [[temp_pytorch_index|PyTorch]]