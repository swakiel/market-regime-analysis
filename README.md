# Market Regime Detection with Unsupervised Learning

## Overview

Financial markets operate under distinct **regimes** characterised by different volatility, correlation, and return dynamics.  
Strategies that perform well in one regime can fail catastrophically in another.

This project builds an **end-to-end market regime detection pipeline** using unsupervised and probabilistic models, with a strong emphasis on:

- Interpretability over raw performance  
- Leakage-free feature engineering and evaluation  
- Realistic conclusions about trading applicability  

The project is designed as a **flagship portfolio piece** demonstrating applied machine learning, time-series reasoning, and critical model evaluation.

---

## Project Objectives

1. Identify latent market regimes using unsupervised learning  
2. Compare clustering and probabilistic regime models  
3. Analyse regime statistics and temporal behaviour  
4. Evaluate a simple regime-based trading strategy  
5. Understand where regime models add value — and where they do not  

---

## Data & Features

**Asset:** SPY (US Equity Market Proxy)  
**Frequency:** Daily  

### Engineered Features
- Log returns  
- Rolling volatility (20d, 60d)  
- Distance from 50-day moving average  
- Rolling correlations:
  - SPY–TLT (60d)
  - SPY–GLD (60d)

> **Note:** Normalised return/volatility ratio features were tested and excluded due to excessive noise at daily frequency.

All features are standardised using **expanding z-scores** to avoid look-ahead bias.

---

## Models Implemented

### 1. KMeans
- Hard clustering
- No temporal structure
- Fast and highly reactive

### 2. Gaussian Mixture Model (GMM)
- Soft probabilistic clustering
- Captures uncertainty
- Static regime assignments

### 3. Hidden Markov Model (HMM)
- Time-dependent regime transitions
- Persistent regimes
- Gaussian emissions with diagonal covariance

HMM emission parameters are initialised using KMeans for stability, and transition matrices are constrained to encourage regime persistence.

---

## Regime Interpretation

Across all models, three economically intuitive regimes emerge:

- **Calm / Growth** — low volatility, positive returns  
- **Transition** — moderate volatility and returns  
- **Stress / Crisis** — elevated volatility and drawdowns  

Regimes are labelled post hoc using statistical characteristics (volatility, drawdown, Sharpe).

---

## Model Comparison Summary

| Model  | Calm Sharpe | Crisis Drawdown | Avg Regime Length (days) | Stability | Key Characteristics |
|------|-------------|-----------------|--------------------------|----------|---------------------|
| KMeans | ~0.08 | ~-0.67 | ~36 | Low | Hard clustering, highly reactive |
| GMM | ~0.14 | ~-0.55 | ~22 | Medium | Soft clustering, probabilistic |
| HMM | ~0.10 | ~-0.55 | ~88 | High | Persistent, interpretable regimes |

> *Exact statistics available in:* `src/analysis/regime_stats.py`

---

## Strategy Evaluation

A simple regime-based strategy was tested:

- **Long** during *Calm / Growth*
- **Short** during *Stress / Crisis*
- **Hold** during *Transition*

Performance was compared against buy-and-hold using an initial capital approach.

### Results Summary
- No regime strategy outperforms buy-and-hold over the full period
- KMeans provides the strongest drawdown protection
- HMM produces stable but slow-moving signals
- Regime strategies function better as **risk overlays** than alpha generators

---

## Key Insights

- Simpler models (KMeans) can be surprisingly effective
- Probabilistic models improve interpretability more than performance
- Temporal structure improves regime realism but reduces responsiveness
- Regime detection is better suited to **risk management and context** than pure trading

---

## Limitations

- No transaction costs or slippage
- Single-market focus (SPY only)
- Fixed number of regimes
- No walk-forward retraining
- No macroeconomic features

---

## Future Work

- Dynamic regime counts via information criteria
- Macro and cross-asset feature expansion
- Volatility-targeted or allocation-based strategies
- Walk-forward regime estimation
- Multi-asset regime comparison

---

## Portfolio Takeaway

This project demonstrates the ability to:

- Design a clean, modular ML research pipeline  
- Apply unsupervised learning to noisy financial data  
- Make disciplined, realistic conclusions about model performance  

Rather than optimising for backtest returns, the focus is on **robust reasoning, interpretability, and practical understanding** — skills critical for ML engineering, data science, and quantitative roles.
