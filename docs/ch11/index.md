# Chapter 10: Pandas

This chapter covers pandas, the essential data analysis library in Python, including Series and DataFrame objects, data loading, filtering, manipulation, merging, reshaping, groupby, time series, and performance optimization.

## 10.1 Overview

- [Arrays vs DataFrames](overview/arrays_vs_dataframes.md)

## 10.2 Core pandas Objects

- [Series](core/series.md)
- [DataFrame](core/dataframe.md)
- [Series vs DataFrame](core/series_vs_dataframe.md)
- [Index Objects](core/index_objects.md)
- [Hierarchical Indexing](core/hierarchical_indexing.md)
- [Indexing and Selection](core/indexing.md)

## 10.3 Creating DataFrames

- [DataFrame Creation](creation/dataframe_creation.md)
- [Series Creation](creation/series_creation.md)
- [Loading CSV Files](creation/read_csv.md)
- [Loading Excel and JSON](creation/read_excel_json.md)
- [Loading SQL and Parquet](creation/read_sql_parquet.md)
- [Saving DataFrames](creation/saving.md)

## 10.4 DataFrame Inspection

- [Attributes](inspection/attributes.md)
- [Basic Methods](inspection/basic_methods.md)
- [Statistical Methods](inspection/statistical_methods.md)
- [Value Counts and Unique](inspection/value_counts.md)
- [Memory Usage](inspection/memory_usage.md)

## 10.5 Filtering Data

- [Boolean Indexing](filtering/boolean_indexing.md)
- [query Method](filtering/query.md)
- [isin Method](filtering/isin.md)
- [between Method](filtering/between.md)
- [String Methods](filtering/string_methods.md)
- [eval Method](filtering/eval.md)
- [select_dtypes Method](filtering/select_dtypes.md)

## 10.6 Data Manipulation

- [Renaming Axes](manipulation/renaming.md)
- [Type Conversion with astype](manipulation/astype.md)
- [map Method](manipulation/map.md)
- [apply Method](manipulation/apply.md)
- [apply with axis](manipulation/apply_axis.md)
- [Sorting by Index and Values](manipulation/sorting.md)
- [assign Method](manipulation/assign.md)
- [drop Method](manipulation/drop.md)
- [drop_duplicates Method](manipulation/drop_duplicates.md)
- [clip Method](manipulation/clip.md)

## 10.7 Handling Missing Data

- [Detecting Missing Values](missing/detecting.md)
- [fillna Method](missing/fillna.md)
- [fillna Keywords](missing/fillna_keywords.md)
- [interpolate Method](missing/interpolate.md)
- [dropna Method](missing/dropna.md)
- [dropna Keywords](missing/dropna_keywords.md)
- [replace Method](missing/replace.md)

## 10.8 Aggregations

- [Basic Aggregations](aggregation/basic_aggregations.md)
- [agg Method](aggregation/agg_method.md)
- [agg with Multiple Functions](aggregation/agg_multiple.md)

## 10.9 Accessor Methods

- [String Accessor (str)](accessors/str_accessor.md)
- [String Methods Reference](accessors/str_methods.md)
- [Datetime Accessor (dt)](accessors/dt_accessor.md)
- [Datetime Methods Reference](accessors/dt_methods.md)
- [Categorical Accessor (cat)](accessors/cat_accessor.md)

## 10.10 Categorical Data

- [Introduction to Categoricals](categorical/introduction.md)
- [Creating Categoricals](categorical/creating.md)
- [Memory Efficiency](categorical/memory_efficiency.md)
- [Ordered Categoricals](categorical/ordered.md)
- [Categorical Operations](categorical/operations.md)
- [Binning (cut and qcut)](categorical/binning.md)
- [One-Hot Encoding (get_dummies)](categorical/encoding.md)

## 10.11 Merging DataFrames

- [merge vs join](merge/merge_vs_join.md)
- [merge Method](merge/merge_method.md)
- [Keyword - on](merge/keyword_on.md)
- [Keyword - left_on right_on](merge/keyword_left_right_on.md)
- [Keyword - how](merge/keyword_how.md)
- [Keyword - suffixes](merge/keyword_suffixes.md)
- [Keyword - indicator](merge/keyword_indicator.md)
- [Self Merge](merge/self_merge.md)
- [Cross Merge](merge/cross_merge.md)
- [merge_asof Method](merge/merge_asof.md)

## 10.12 Joining DataFrames

- [join Method](join/join_method.md)
- [Keyword - how](join/keyword_how.md)
- [Keyword - on and lsuffix/rsuffix](join/keyword_on_suffixes.md)
- [Multi-Index Joins](join/multiindex_joins.md)
- [join vs merge](join/join_vs_merge.md)

## 10.13 Concatenating DataFrames

- [concat Method](concat/concat_method.md)
- [Keyword - axis](concat/keyword_axis.md)
- [Keyword - ignore_index](concat/keyword_ignore_index.md)
- [Keyword - keys and names](concat/keyword_keys_names.md)
- [Keyword - join and verify_integrity](concat/keyword_join_verify.md)
- [concat vs append vs merge](concat/concat_vs_append_merge.md)

## 10.14 Reshaping Data

- [melt Method](reshape/melt.md)
- [pivot vs melt](reshape/pivot_vs_melt.md)
- [stack Method](reshape/stack.md)
- [unstack Method](reshape/unstack.md)
- [stack vs unstack](reshape/stack_vs_unstack.md)
- [explode Method](reshape/explode.md)

## 10.15 GroupBy

- [GroupBy Object](groupby/groupby_object.md)
- [Iteration with GroupBy](groupby/iteration.md)
- [get_group Method](groupby/get_group.md)
- [GroupBy Aggregations](groupby/aggregations.md)
- [transform Method](groupby/transform.md)
- [rank Method](groupby/rank.md)
- [filter Method](groupby/filter.md)
- [Multi-Level Grouping](groupby/multi_level.md)

## 10.16 Pivot Tables

- [pivot Method](pivot/pivot_method.md)
- [pivot_table Method](pivot/pivot_table_method.md)
- [pivot vs pivot_table](pivot/pivot_vs_pivot_table.md)

## 10.17 Time Series

- [DatetimeIndex](timeseries/datetimeindex.md)
- [Creating Date Ranges](timeseries/date_ranges.md)
- [Parsing Dates](timeseries/parsing_dates.md)
- [Time Indexing](timeseries/time_indexing.md)
- [Resampling](timeseries/resampling.md)
- [shift and diff](timeseries/shift_diff.md)
- [pct_change Method](timeseries/pct_change.md)

## 10.18 Window Functions

- [Window Functions Overview](window/overview.md)
- [rolling Method](window/rolling.md)
- [expanding Method](window/expanding.md)
- [ewm Method](window/ewm.md)
- [Window with GroupBy](window/window_groupby.md)

## 10.19 Panel Data

- [Introduction to Panel Data](panel/introduction.md)
- [Building Panel DataFrames](panel/building.md)
- [Accessing Panel Data](panel/accessing.md)
- [Panel Aggregations](panel/aggregations.md)
- [Reshaping Panel Data](panel/reshaping.md)

## 10.20 Performance Optimization

- [Memory Optimization](performance/memory_optimization.md)
- [Vectorization](performance/vectorization.md)
- [Chunked Processing](performance/chunked_processing.md)
- [Introduction to Dask](performance/dask_intro.md)

## 10.21 Common Pitfalls

- [View vs Copy](pitfalls/view_vs_copy.md)
- [Chained Assignment](pitfalls/chained_assignment.md)
- [Index Misalignment](pitfalls/index_misalignment.md)
- [Unexpected NaNs](pitfalls/unexpected_nans.md)
- [Performance Traps](pitfalls/performance_traps.md)

## 10.22 Practical Examples

- [Financial Data Workflow](examples/yfinance_workflow.md)
- [SP500 Analysis](examples/sp500_analysis.md)
- [LeetCode Patterns](examples/leetcode_patterns.md)
- [LeetCode Series Problems](examples/leetcode_series.md)
- [LeetCode DataFrame Problems](examples/leetcode_dataframe.md)

## 10.23 Pandas OOP Design

- [Pandas Series](oop/pandas_series.md)
- [Pandas DataFrame](oop/pandas_dataframe.md)
- [Pandas Index Objects](oop/pandas_index.md)
- [Pandas MultiIndex](oop/pandas_multiindex.md)
- [Pandas Method Chaining](oop/pandas_method_chaining.md)

## 10.24 Pandas Plotting

- [plot Method](plotting/plot_method.md)
- [plot Keywords](plotting/plot_keywords.md)
- [Plot Types (kind)](plotting/plot_kinds.md)
- [hist Method](plotting/hist.md)
- [boxplot Method](plotting/boxplot.md)
- [scatter_matrix](plotting/scatter_matrix.md)
- [Bar Plots](plotting/bar_plots.md)
