# Type I and Type II Errors

When performing a hypothesis test, two kinds of mistakes are possible: concluding that an effect exists when it does not, or missing a real effect. These mistakes — Type I and Type II errors — have direct consequences for scientific conclusions and decision-making. This section defines both error types, quantifies their probabilities, and examines the fundamental trade-off between them.

## Type I Error (False Positive)

A **Type I error** occurs when the null hypothesis $H_0$ is true, but the test incorrectly rejects it. Informally, this is a "false alarm" — we declare a significant result when there is actually no effect.

The probability of a Type I error is denoted by $\alpha$ and equals the significance level of the test:

$$
\alpha = P(\text{reject } H_0 \mid H_0 \text{ is true})
$$

The value of $\alpha$ is chosen by the analyst before conducting the test. A common choice is $\alpha = 0.05$, meaning we accept a 5% chance of falsely rejecting a true null hypothesis.

!!! example "Type I Error in Practice"
    A pharmaceutical company tests whether a new drug lowers blood pressure more than a placebo. If the drug has no real effect ($H_0$ is true) but the test yields $p < 0.05$, the company would incorrectly conclude the drug works. This false positive could lead to costly clinical trials of an ineffective treatment.

## Type II Error (False Negative)

A **Type II error** occurs when the alternative hypothesis $H_1$ is true, but the test fails to reject $H_0$. This means a real effect goes undetected.

The probability of a Type II error is denoted by $\beta$:

$$
\beta = P(\text{fail to reject } H_0 \mid H_1 \text{ is true})
$$

Unlike $\alpha$, the value of $\beta$ is generally not fixed directly. Instead, it depends on the true effect size, the sample size $n$, the chosen significance level $\alpha$, and the variability in the data.

!!! example "Type II Error in Practice"
    Continuing the drug trial example, suppose the drug truly does lower blood pressure by a small amount. If the sample size is too small to detect this modest effect, the test fails to reject $H_0$, and the effective drug is incorrectly deemed no better than a placebo.

## Power and the Error Trade-off

The **power** of a test is the probability of correctly rejecting $H_0$ when $H_1$ is true:

$$
\text{Power} = 1 - \beta = P(\text{reject } H_0 \mid H_1 \text{ is true})
$$

Higher power means a lower chance of missing a real effect. A conventional target is power $\geq 0.80$, meaning at most a 20% chance of a Type II error.

The key trade-off in hypothesis testing is that, for a fixed sample size, decreasing $\alpha$ (making the test more conservative) increases $\beta$ (making it harder to detect real effects), and vice versa. The only way to reduce both error rates simultaneously is to increase the sample size $n$ or to study a larger effect size.

The following table summarizes the four possible outcomes of a hypothesis test:

|  | $H_0$ is true | $H_1$ is true |
|---|---|---|
| **Reject** $H_0$ | Type I error (prob. $\alpha$) | Correct decision (prob. $1 - \beta$) |
| **Fail to reject** $H_0$ | Correct decision (prob. $1 - \alpha$) | Type II error (prob. $\beta$) |

## Summary

Type I errors (false positives, probability $\alpha$) and Type II errors (false negatives, probability $\beta$) represent the two fundamental mistakes in hypothesis testing. The power of a test, $1 - \beta$, measures its ability to detect a true effect, and the trade-off between $\alpha$ and $\beta$ is governed by sample size and effect size.
