# KL Divergence

When comparing two probability distributions, we often need a way to quantify how much one distribution differs from another. The Kullback-Leibler (KL) divergence provides exactly this measure: it captures the expected extra cost of encoding data from a true distribution $p$ using a code optimized for an approximate distribution $q$. KL divergence arises naturally in model selection, variational inference, and maximum likelihood estimation. This section defines KL divergence, proves its non-negativity, and highlights its key properties.

## Definition

Let $p$ and $q$ be two probability distributions over the same discrete sample space $\mathcal{X}$. The **Kullback-Leibler divergence** (or relative entropy) of $q$ from $p$ is

$$
D_{\mathrm{KL}}(p \| q) = \sum_{x \in \mathcal{X}} p(x) \log \frac{p(x)}{q(x)}
$$

where the sum runs over all $x$ with $p(x) > 0$. We require $q(x) > 0$ whenever $p(x) > 0$; otherwise $D_{\mathrm{KL}}(p \| q) = +\infty$.

For continuous distributions with densities $p(x)$ and $q(x)$, the KL divergence is

$$
D_{\mathrm{KL}}(p \| q) = \int p(x) \log \frac{p(x)}{q(x)} \, dx
$$

The notation $D_{\mathrm{KL}}(p \| q)$ is read as "the KL divergence from $p$ to $q$" or "the KL divergence of $q$ from $p$." The order matters because KL divergence is not symmetric.

## Non-negativity (Gibbs' Inequality)

The most fundamental property of KL divergence is that it is always non-negative.

!!! note "Gibbs' Inequality"
    For any two probability distributions $p$ and $q$ on the same sample space,

    $$
    D_{\mathrm{KL}}(p \| q) \geq 0
    $$

    with equality if and only if $p = q$ almost everywhere.

**Proof sketch.** The proof uses Jensen's inequality applied to the convex function $f(t) = -\log t$:

$$
D_{\mathrm{KL}}(p \| q) = -\sum_x p(x) \log \frac{q(x)}{p(x)} \geq -\log \left( \sum_x p(x) \cdot \frac{q(x)}{p(x)} \right) = -\log \left( \sum_x q(x) \right) = -\log 1 = 0
$$

Equality holds if and only if $q(x)/p(x)$ is constant $p$-almost surely, which requires $p = q$. $\square$

## Asymmetry

Unlike a true distance metric, KL divergence is **not symmetric**:

$$
D_{\mathrm{KL}}(p \| q) \neq D_{\mathrm{KL}}(q \| p) \quad \text{in general}
$$

This asymmetry has practical consequences. Minimizing $D_{\mathrm{KL}}(p \| q)$ over $q$ (called the "forward KL" or "M-projection") tends to produce distributions $q$ that cover all modes of $p$, potentially spreading mass broadly. Minimizing $D_{\mathrm{KL}}(q \| p)$ over $q$ (called the "reverse KL" or "I-projection") tends to produce distributions $q$ that concentrate on a single mode of $p$.

!!! example "Asymmetry Illustrated"
    Let $p = (1/2, 1/2)$ and $q = (1/10, 9/10)$ on $\mathcal{X} = \{0, 1\}$. Then:

    $$
    D_{\mathrm{KL}}(p \| q) = \frac{1}{2}\log\frac{1/2}{1/10} + \frac{1}{2}\log\frac{1/2}{9/10} \approx 0.511 \text{ nats}
    $$

    $$
    D_{\mathrm{KL}}(q \| p) = \frac{1}{10}\log\frac{1/10}{1/2} + \frac{9}{10}\log\frac{9/10}{1/2} \approx 0.368 \text{ nats}
    $$

    The two values differ because the divergence penalizes different regions of the distribution depending on which distribution appears in the weighting.

## Relationship to Cross-Entropy

KL divergence connects directly to cross-entropy and entropy through the decomposition:

$$
D_{\mathrm{KL}}(p \| q) = H(p, q) - H(p)
$$

where $H(p, q) = -\sum_x p(x) \log q(x)$ is the cross-entropy and $H(p) = -\sum_x p(x) \log p(x)$ is the Shannon entropy. Since $H(p)$ is constant with respect to $q$, minimizing cross-entropy over $q$ is equivalent to minimizing KL divergence.

## Summary

KL divergence $D_{\mathrm{KL}}(p \| q) = \sum_x p(x) \log \frac{p(x)}{q(x)}$ measures the information-theoretic cost of approximating distribution $p$ with distribution $q$. It is non-negative (Gibbs' inequality), zero only when $p = q$, and asymmetric. Its relationship to cross-entropy, $D_{\mathrm{KL}}(p \| q) = H(p, q) - H(p)$, makes minimizing KL divergence equivalent to minimizing cross-entropy.
