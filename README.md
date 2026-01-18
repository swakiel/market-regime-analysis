# Project Statement

Financial markets exhibit distinct regimes characterised by differences in volatility, correlation structure, and return dynamics. Strategies that perform well in one regime often fail catastrophically in others.

The goal of this project is to identify latent market regimes using unsupervised learning on financial time series, and to evaluate the robustness of simple trading strategies across regimes, with an emphasis on interpretability, leakage-free backtesting, and risk-aware evaluation.

## Feature Engineering

I experimented with normalised returns (return/volatility), but found the signal too noisy at daily frequency to contribute meaningfully to regime separation, so I excluded it.


I compared KMeans and GMM for regime detection.
Both identified a dominant low-volatility growth regime and a short-lived high-volatility stress regime.
However, GMM produced more stable regime assignments and better-separated crisis periods, motivating a transition to HMM.


When implementing HMMs I found that full covariance estimation was unstable for financial features, so I used diagonal covariance with standardised inputs, which is standard in practical regime modelling.

Financial features are noisy and highly correlated.
I initialise emission distributions with KMeans and impose persistent transitions to avoid degenerate solutions and ensure stable, interpretable regimes.

### Model Comparison Summary

| Model  | Calm / Growth Sharpe | Stress Regime Drawdown | Avg Regime Length (days) | Regime Stability | Key Characteristics |
|------|----------------------|------------------------|--------------------------|------------------|--------------------|
| KMeans | ~0.08 | -0.67 | ~36 | Low | Hard clustering, no temporal structure |
| GMM | ~0.14 | -0.55 | ~22 | Medium | Soft clustering, probabilistic but static |
| HMM | ~0.10 | -0.55 | ~88 | High | Temporal dependence, persistent regimes |


### Interpretation

KMeans identifies broad market conditions but exhibits frequent regime switching due to the absence of temporal structure. While it separates high-volatility periods effectively, the resulting regimes are short-lived and noisy, limiting practical usefulness.

GMM improves upon KMeans by modelling uncertainty through soft assignments, leading to more coherent regime separation. However, without explicit temporal dependence, regime persistence remains limited and transitions are still relatively frequent.

The Hidden Markov Model produces the most realistic regime structure. Regimes are persistent, transitions are infrequent, and crisis periods are captured as prolonged states rather than isolated spikes. Although Sharpe ratios are comparable to GMM, the HMM provides superior interpretability and stability, making it the most suitable model for market regime analysis and downstream decision-making.
