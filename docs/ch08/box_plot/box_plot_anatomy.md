# Box Plot Anatomy

Understanding the visual components of a box plot is essential for proper interpretation of distributional data.

## Visual Components

A box plot consists of five primary visual elements that summarize the distribution.

### 1. The Box

The rectangular box spans from the first quartile (Q1, 25th percentile) to the third quartile (Q3, 75th percentile). This range is called the Interquartile Range (IQR).

```python
IQR = Q3 - Q1
```

### 2. The Median Line

The horizontal line inside the box represents the median (Q2, 50th percentile). Its position within the box indicates skewness.

### 3. The Whiskers

Vertical lines extend from the box to show the range of non-outlier data. By default, whiskers extend to 1.5 × IQR from the box edges.

```python
lower_whisker = Q1 - 1.5 * IQR
upper_whisker = Q3 + 1.5 * IQR
```

### 4. The Fliers (Outliers)

Points beyond the whiskers are plotted individually as outliers (fliers). These represent extreme values in the distribution.

### 5. The Caps

Short horizontal lines at whisker ends mark the extent of non-outlier data.

## Statistical Interpretation

The box plot encodes the five-number summary plus outlier detection.

### 1. Five-Number Summary

```python
import numpy as np

data = np.random.normal(100, 15, 200)

minimum = np.min(data)
q1 = np.percentile(data, 25)
median = np.percentile(data, 50)
q3 = np.percentile(data, 75)
maximum = np.max(data)
```

### 2. Spread Indicators

The box width (IQR) shows the middle 50% of data. Tall boxes indicate high variability; short boxes indicate consistency.

### 3. Skewness Detection

When the median line is not centered in the box, the distribution is skewed. Median closer to Q1 indicates right skew; closer to Q3 indicates left skew.

## Comparison with Histogram

Box plots and histograms both show distributions but emphasize different aspects.

### 1. Box Plot Strengths

Box plots excel at comparing multiple distributions side-by-side, identifying outliers, and showing quartile information compactly.

### 2. Histogram Strengths

Histograms reveal the shape of the distribution, multimodality, and density patterns that box plots cannot show.

### 3. Combined View

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.normal(100, 15, 200)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.hist(data, bins=20, edgecolor='black', alpha=0.7)
ax1.set_title('Histogram')

ax2.boxplot(data)
ax2.set_title('Box Plot')

plt.tight_layout()
plt.show()
```
