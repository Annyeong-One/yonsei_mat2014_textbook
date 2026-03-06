# Introduction to Panel Data

**Panel data** (also called **longitudinal data**) combines cross-sectional and time-series dimensions. Each observation is identified by two keys: an entity (individual, firm, country) and a time point.

## What is Panel Data?

Panel data has two dimensions:
- **Cross-sectional**: Different entities (stocks, companies, individuals)
- **Time-series**: Repeated observations over time

```
┌─────────────────────────────────────────────────┐
│                  Panel Data                      │
├─────────────────────────────────────────────────┤
│    Entity (i)     Time (t)        Value         │
│    ──────────     ────────        ─────         │
│    AAPL           2024-01-01      \$150.00       │
│    AAPL           2024-01-02      \$151.50       │
│    AAPL           2024-01-03      \$149.80       │
│    MSFT           2024-01-01      \$300.00       │
│    MSFT           2024-01-02      \$302.00       │
│    MSFT           2024-01-03      \$301.50       │
│    GOOGL          2024-01-01      \$140.00       │
│    GOOGL          2024-01-02      \$141.20       │
│    GOOGL          2024-01-03      \$142.00       │
└─────────────────────────────────────────────────┘
```

## Panel Data vs Other Data Types

| Data Type | Entities | Time Points | Example |
|-----------|----------|-------------|---------|
| Cross-sectional | Multiple | Single | Survey at one point |
| Time-series | Single | Multiple | One stock's history |
| **Panel** | **Multiple** | **Multiple** | Multiple stocks over time |

## Why Use Panel Data?

### 1. More Information

Panel data contains more observations than cross-sectional or time-series alone:

```
Cross-sectional: 100 stocks × 1 day = 100 observations
Time-series: 1 stock × 252 days = 252 observations
Panel: 100 stocks × 252 days = 25,200 observations
```

### 2. Control for Unobserved Heterogeneity

Panel data allows fixed effects models that control for entity-specific factors:
- Stock-specific characteristics (management quality, brand value)
- Time-specific effects (market conditions, regulations)

### 3. Study Dynamics

Track how entities change over time.

## Examples of Panel Data

| Domain | Entities | Time | Variables |
|--------|----------|------|-----------|
| Finance | Stocks | Days | Returns, Volume |
| Economics | Countries | Years | GDP, Inflation |
| Healthcare | Patients | Visits | Vitals, Tests |
| Education | Students | Grades | Scores, Attendance |

## Balanced vs Unbalanced Panels

### Balanced Panel
Every entity has observations for every time period.

### Unbalanced Panel
Some entity-time combinations are missing (common in real data).

## Long vs Wide Format

### Long Format (Standard)
```
ticker  date        return
AAPL    2024-01-01  0.01
AAPL    2024-01-02  0.02
MSFT    2024-01-01  0.015
```

### Wide Format
```
date        AAPL   MSFT
2024-01-01  0.01   0.015
2024-01-02  0.02   0.018
```

## Panel Data in Pandas

Pandas handles panel data using **MultiIndex**:

```python
import pandas as pd
import numpy as np

tickers = ['AAPL', 'MSFT', 'GOOGL']
dates = pd.date_range('2024-01-01', periods=5)

index = pd.MultiIndex.from_product(
    [tickers, dates], 
    names=['ticker', 'date']
)

returns = pd.Series(np.random.randn(15) * 0.02, index=index, name='return')
print(returns)
```
