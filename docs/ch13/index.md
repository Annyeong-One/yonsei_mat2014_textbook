# Chapter 12: SciPy Stats

This chapter covers statistical analysis with SciPy, including descriptive statistics, probability distributions, density estimation, hypothesis testing, correlation, regression, resampling methods, and information theory.

## 12.1 Descriptive Statistics

- [Summary Statistics](descriptive/summary_stats.md)
- [Moments and Skewness](descriptive/moments.md)
- [Percentiles and Quantiles](descriptive/percentiles.md)
- [Outlier Detection](descriptive/outlier_detection.md)
- [Robust Statistics (MAD, Trimmed)](descriptive/robust_statistics.md)

## 12.2 Distribution Object Model

- [rv_continuous and rv_discrete](distributions/rv_classes.md)
- [Frozen Distributions](distributions/frozen.md)
- [Sampling (rvs)](distributions/rvs.md)
- [Density and Mass (pdf, pmf)](distributions/pdf_pmf.md)
- [Cumulative Distribution (cdf, sf)](distributions/cdf_sf.md)
- [Quantile Function (ppf, isf)](distributions/ppf_isf.md)
- [Moments and Stats (mean, var, moment, stats)](distributions/moments_stats.md)
- [Fitting Distributions to Data (fit)](distributions/fit.md)
- [Confidence Intervals (interval)](distributions/interval.md)

## 12.3 Distribution Families

- [Normal Distribution](families/normal.md)
- [t-Distribution](families/t_distribution.md)
- [Chi-Square Distribution](families/chi_square.md)
- [F-Distribution](families/f_distribution.md)
- [Exponential and Gamma](families/exponential_gamma.md)
- [Beta Distribution](families/beta.md)
- [Uniform Distribution](families/uniform.md)
- [Lognormal and Weibull](families/lognormal_weibull.md)
- [Binomial and Poisson](families/binomial_poisson.md)
- [Multivariate Normal](families/multivariate_normal.md)
- [Custom Distributions (rv_continuous subclass)](families/custom_distributions.md)

## 12.4 Density Estimation

- [gaussian_kde](density/gaussian_kde.md)
- [Bandwidth Selection](density/bandwidth.md)
- [KDE vs Histogram](density/kde_vs_histogram.md)
- [Multivariate KDE](density/multivariate_kde.md)
- [Evaluate and Resample](density/evaluate_resample.md)

## 12.5 Hypothesis Testing

- [Null and Alternative Hypotheses](hypothesis/null_hypothesis.md)
- [p-values and Significance](hypothesis/pvalues.md)
- [Type I and Type II Errors](hypothesis/type_errors.md)
- [Power Analysis](hypothesis/power_analysis.md)
- [Confidence Intervals](hypothesis/confidence_intervals.md)
- [Multiple Testing Correction (Bonferroni, FDR)](hypothesis/multiple_testing.md)
- [One-Sided vs Two-Sided Tests](hypothesis/one_vs_two_sided.md)
- [Effect Size](hypothesis/effect_size.md)

## 12.6 Statistical Tests

- [t-Tests (ttest_1samp, ttest_ind, ttest_rel)](tests/t_tests.md)
- [ANOVA (f_oneway)](tests/anova.md)
- [Chi-Square Tests (chi2_contingency, chisquare)](tests/chi_square.md)
- [Normality Tests (Shapiro, Anderson, D'Agostino)](tests/normality.md)
- [Non-Parametric Tests (Mann-Whitney, Wilcoxon, Kruskal)](tests/nonparametric.md)
- [Goodness of Fit (kstest, anderson)](tests/goodness_of_fit.md)
- [Variance Tests (Levene, Bartlett)](tests/variance_tests.md)
- [Test Selection Guide](tests/selection_guide.md)

## 12.7 Correlation

- [Pearson and Spearman](correlation/correlation.md)
- [Kendall's Tau](correlation/kendall.md)
- [Partial Correlation](correlation/partial_correlation.md)
- [Autocorrelation](correlation/autocorrelation.md)
- [Covariance and Covariance Matrix](correlation/covariance.md)
- [Correlation Pitfalls](correlation/pitfalls.md)

## 12.8 Regression

- [linregress](regression/linregress.md)
- [OLS Fundamentals](regression/ols_fundamentals.md)
- [Residual Analysis](regression/residual_analysis.md)
- [Multiple Regression Concepts](regression/multiple_regression.md)
- [Polynomial Regression](regression/polynomial_regression.md)
- [Regularization Preview (Ridge, Lasso)](regression/regularization_preview.md)
- [Logistic Regression Preview](regression/logistic_preview.md)

## 12.9 Resampling Methods

- [Bootstrap Basics (scipy.stats.bootstrap)](resampling/bootstrap.md)
- [Bootstrap Confidence Intervals](resampling/bootstrap_ci.md)
- [Permutation Tests (permutation_test)](resampling/permutation.md)
- [Jackknife Method](resampling/jackknife.md)
- [Monte Carlo Simulation](resampling/monte_carlo.md)

## 12.10 Probability Plots and Diagnostics

- [QQ Plots (probplot)](diagnostics/qq_plots.md)
- [PP Plots](diagnostics/pp_plots.md)
- [Residual Diagnostics](diagnostics/residual_plots.md)
- [Distribution Comparison Visualization](diagnostics/distribution_comparison.md)
- [Normality Visualization](diagnostics/normality_visualization.md)

## 12.11 Information Theory

- [Entropy (shannon_entropy)](information/entropy.md)
- [KL Divergence](information/kl_divergence.md)
- [Cross-Entropy](information/cross_entropy.md)
- [Mutual Information](information/mutual_information.md)
- [Connection to ML Loss Functions](information/ml_loss_connection.md)

## 12.12 Data Preprocessing

- [Quantile Normalization](preprocessing/quantile_normalization.md)

## 12.13 Practical Applications

- [A/B Testing Workflow](applications/ab_testing.md)
- [Financial Returns Analysis](applications/financial_returns.md)
- [Feature Selection for ML](applications/feature_selection.md)
- [Statistical Preprocessing](applications/preprocessing.md)
- [Monte Carlo Methods in Finance](applications/monte_carlo_finance.md)
- [Bayesian Inference Preview](applications/bayesian_preview.md)
