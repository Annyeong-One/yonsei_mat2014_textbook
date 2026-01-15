# Chunked Processing

When files are too large to fit in memory, chunked processing allows you to work with data in smaller pieces. This is essential for handling datasets larger than available RAM.

## The Memory Problem

```python
import pandas as pd

# This will fail if the file is larger than RAM
# df = pd.read_csv('huge_file.csv')  # MemoryError!
```

## Solution: chunksize Parameter

The `chunksize` parameter returns an iterator that yields DataFrames of the specified size.

```python
# Process in chunks of 100,000 rows
chunk_iter = pd.read_csv('huge_file.csv', chunksize=100_000)

for chunk in chunk_iter:
    # Process each chunk
    process(chunk)
```

## Common Chunked Processing Patterns

### Pattern 1: Aggregation

Compute statistics that can be combined across chunks.

```python
# Calculate mean of a column
total_sum = 0
total_count = 0

for chunk in pd.read_csv('data.csv', chunksize=100_000):
    total_sum += chunk['value'].sum()
    total_count += len(chunk)

mean_value = total_sum / total_count
print(f"Mean: {mean_value}")
```

### Pattern 2: Filtering and Collecting

Filter rows and collect matching results.

```python
# Find all rows matching a condition
results = []

for chunk in pd.read_csv('data.csv', chunksize=100_000):
    filtered = chunk[chunk['category'] == 'target']
    results.append(filtered)

# Combine results
df_filtered = pd.concat(results, ignore_index=True)
print(f"Found {len(df_filtered)} matching rows")
```

### Pattern 3: GroupBy Aggregation

Compute grouped statistics across chunks.

```python
from collections import defaultdict

# Track sums and counts per group
group_sums = defaultdict(float)
group_counts = defaultdict(int)

for chunk in pd.read_csv('data.csv', chunksize=100_000):
    grouped = chunk.groupby('category')['value'].agg(['sum', 'count'])
    for category, row in grouped.iterrows():
        group_sums[category] += row['sum']
        group_counts[category] += row['count']

# Calculate final means
group_means = {k: group_sums[k] / group_counts[k] for k in group_sums}
print(group_means)
```

### Pattern 4: Transform and Write

Process each chunk and write to output.

```python
# Transform and write in chunks
first_chunk = True

for chunk in pd.read_csv('input.csv', chunksize=100_000):
    # Transform
    chunk['new_column'] = chunk['value'] * 2
    chunk['category'] = chunk['category'].str.upper()
    
    # Write (append mode after first chunk)
    if first_chunk:
        chunk.to_csv('output.csv', index=False)
        first_chunk = False
    else:
        chunk.to_csv('output.csv', mode='a', header=False, index=False)
```

### Pattern 5: Sample from Large File

Extract a random sample without loading entire file.

```python
import random

# Reservoir sampling
sample_size = 10000
sample = []
n_seen = 0

for chunk in pd.read_csv('huge_file.csv', chunksize=100_000):
    for idx, row in chunk.iterrows():
        n_seen += 1
        if len(sample) < sample_size:
            sample.append(row)
        else:
            # Randomly replace with decreasing probability
            j = random.randint(0, n_seen - 1)
            if j < sample_size:
                sample[j] = row

df_sample = pd.DataFrame(sample)
```

## Choosing Chunk Size

| Factor | Smaller Chunks | Larger Chunks |
|--------|---------------|---------------|
| Memory usage | Lower | Higher |
| Overhead | Higher | Lower |
| Processing speed | Slower | Faster |

**Guidelines:**
- Start with 100,000 rows
- Adjust based on column count and types
- Monitor memory during processing
- Larger chunks = fewer iterations = faster

```python
# Estimate chunk size based on available memory
import psutil

def estimate_chunk_size(filepath, memory_fraction=0.1):
    """Estimate optimal chunk size."""
    available_memory = psutil.virtual_memory().available
    target_memory = available_memory * memory_fraction
    
    # Read small sample to estimate row size
    sample = pd.read_csv(filepath, nrows=1000)
    row_memory = sample.memory_usage(deep=True).sum() / 1000
    
    chunk_size = int(target_memory / row_memory)
    return max(10000, min(chunk_size, 1000000))  # Between 10K and 1M
```

## Processing with Progress

Track progress through large files.

```python
from tqdm import tqdm
import os

def count_lines(filepath):
    """Count lines in file (fast)."""
    with open(filepath, 'rb') as f:
        return sum(1 for _ in f)

filepath = 'huge_file.csv'
total_lines = count_lines(filepath) - 1  # Exclude header
chunk_size = 100_000

# Process with progress bar
with tqdm(total=total_lines, desc="Processing") as pbar:
    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        # Process chunk
        process(chunk)
        pbar.update(len(chunk))
```

## Combining with dtype Optimization

Optimize memory within each chunk.

```python
# Specify dtypes to reduce memory per chunk
dtypes = {
    'id': 'int32',
    'value': 'float32',
    'category': 'category'
}

for chunk in pd.read_csv('data.csv', chunksize=100_000, dtype=dtypes):
    # Chunk is already memory-optimized
    process(chunk)
```

## Practical Example: Log File Analysis

```python
# Analyze large web server logs
from collections import Counter

# Track statistics
status_counts = Counter()
total_bytes = 0
request_count = 0

for chunk in pd.read_csv('access_log.csv', chunksize=100_000):
    # Update status code counts
    status_counts.update(chunk['status_code'].value_counts().to_dict())
    
    # Sum bytes transferred
    total_bytes += chunk['bytes'].sum()
    
    # Count requests
    request_count += len(chunk)

# Results
print(f"Total requests: {request_count:,}")
print(f"Total data transferred: {total_bytes / 1e9:.2f} GB")
print(f"Status code distribution:")
for status, count in status_counts.most_common(10):
    print(f"  {status}: {count:,} ({count/request_count*100:.1f}%)")
```

## Practical Example: Financial Data

```python
# Process large stock price dataset
import numpy as np

# Track statistics per ticker
ticker_stats = {}

for chunk in pd.read_csv('stock_prices.csv', 
                         chunksize=100_000,
                         parse_dates=['date']):
    
    for ticker, group in chunk.groupby('ticker'):
        if ticker not in ticker_stats:
            ticker_stats[ticker] = {
                'sum_close': 0,
                'count': 0,
                'max_volume': 0,
                'returns': []
            }
        
        stats = ticker_stats[ticker]
        stats['sum_close'] += group['close'].sum()
        stats['count'] += len(group)
        stats['max_volume'] = max(stats['max_volume'], group['volume'].max())
        stats['returns'].extend(group['close'].pct_change().dropna().tolist())

# Final calculations
results = []
for ticker, stats in ticker_stats.items():
    results.append({
        'ticker': ticker,
        'avg_close': stats['sum_close'] / stats['count'],
        'max_volume': stats['max_volume'],
        'volatility': np.std(stats['returns']) * np.sqrt(252)  # Annualized
    })

df_results = pd.DataFrame(results)
```

## Alternative: Memory-Mapped Files

For random access patterns, consider memory mapping.

```python
# This doesn't load entire file into RAM
df = pd.read_csv('huge_file.csv', memory_map=True)

# Works well for sequential reads
# Less effective for random access
```

## Summary

| Pattern | Use Case |
|---------|----------|
| Aggregation | Computing statistics (sum, mean, count) |
| Filter & Collect | Finding rows matching criteria |
| GroupBy | Grouped statistics |
| Transform & Write | ETL pipelines |
| Sampling | Getting representative subset |

**Best practices:**
1. Choose appropriate chunk size (100K is good default)
2. Specify dtypes to reduce per-chunk memory
3. Use appropriate aggregation pattern for your task
4. Track progress for long-running operations
5. Consider Dask for more complex chunked operations
