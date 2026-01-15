# Project Statement

Financial markets exhibit distinct regimes characterised by differences in volatility, correlation structure, and return dynamics. Strategies that perform well in one regime often fail catastrophically in others.

The goal of this project is to identify latent market regimes using unsupervised learning on financial time series, and to evaluate the robustness of simple trading strategies across regimes, with an emphasis on interpretability, leakage-free backtesting, and risk-aware evaluation.

## Feature Engineering

“I experimented with normalised returns (return/volatility), but found the signal too noisy at daily frequency to contribute meaningfully to regime separation, so I excluded it.”