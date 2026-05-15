# 📊 S&P 500 Quantitative Research — Market Anomaly Testing

| 🇬🇧 English (current) | 🇹🇷 [Türkçe](README_TR.md) |
|---|---|

> **A systematic, data-driven investigation of well-known financial market anomalies using statistical hypothesis testing on a custom S&P 500 data warehouse.**

---

## 🧑‍💻 About This Project

This repository is part of my ongoing quantitative finance research portfolio. I built a full end-to-end data pipeline that ingests, cleans, and stores historical price data for all S&P 500 constituents into a personal PostgreSQL data warehouse. Each notebook in this series applies rigorous academic-level statistical tests to validate or reject a specific market hypothesis.

**My philosophy:** *Don't trust intuition — test it with data, report p-values, and make an explicit trading verdict.*

---

## 🗄️ Data Infrastructure

| Layer | Description |
|---|---|
| **Source** | [yfinance](https://github.com/ranaroussi/yfinance) API — daily OHLCV data |
| **Coverage** | ~500 S&P 500 constituents · Full available history per ticker |
| **Storage** | Self-hosted PostgreSQL 15 data warehouse (`sp500_dw`) |
| **Key Tables** | `daily_prices` (OHLCV) · `tickers` (metadata & GICS sectors) · `ticker_stats` (pre-computed statistical profiles) |
| **Pre-computation** | Kurtosis, Skewness, and Jarque-Bera statistics are computed via a batch pipeline over all tickers and persisted in `ticker_stats` for fast retrieval |

> **Note on credentials:** Database connection details are stored in a local `config.py` file excluded from version control (see `.gitignore`). The `db_utils.py` module abstracts the connection — all notebooks simply call `fetch_data(query)`.

---

## 📁 Repository Structure

```
├── db_utils.py                  # Shared DB connector (public)
├── config.py                    # DB credentials (private — gitignored)
│
├── H1_Tail_Risk_vs_Return.ipynb      # H1: Does Kurtosis predict long-term return?
├── H2_H3_Seasonality.ipynb           # H2: Jan/Dec Effect · H3: ANOVA on 12 months
├── H4_Weekend_Effect.ipynb           # H4: Friday vs Monday — Weekend Effect
│
└── README.md
```

---

## 🔬 Hypotheses Tested

### H1 · Tail-Risk Premium: Does Kurtosis Get Rewarded?
- **Test:** Pearson Correlation + OLS Regression
- **Claim:** Stocks with higher excess kurtosis (fat tails / Black Swan exposure) should earn higher long-term returns as compensation for the extra risk.

### H2 · January & December Effect (Santa Claus Rally)
- **Test:** Welch's Independent Samples T-Test (one-tailed)
- **Claim:** January and December exhibit systematically higher monthly returns than the rest of the year.

### H3 · Seasonality ANOVA — All 12 Calendar Months (2008–Present)
- **Test:** One-Way ANOVA (F-test)
- **Claim:** There is a statistically significant difference in mean returns across the 12 calendar months, implying exploitable seasonality.
- **Key Finding:** 📅 **November** emerged as the strongest month; **September** as the weakest — consistent with the classic "September Effect" documented in academic literature.

### H4 · Weekend Effect — Fridays vs Mondays
- **Test:** Welch's Independent Samples T-Test (one-tailed) + KDE comparison
- **Claim:** Friday daily log returns are significantly higher than Monday log returns across the full S&P 500 universe.

---

## 📋 Report Template

Each hypothesis follows a strict 4-part structure:

```
1. Hypothesis Definition   → H₀ and H₁ clearly stated
2. Data & Methodology      → Population, variables, test choice
3. Statistical Findings    → p-value, test statistic, descriptive stats + visualizations
4. Quant Verdict           → CONFIRMED / REJECTED + Tradeable? + ML feature value
```

---

## 🛠️ Tech Stack

`Python 3.11` · `PostgreSQL 15` · `SQLAlchemy` · `Pandas` · `NumPy` · `SciPy` · `Seaborn` · `Matplotlib` · `Jupyter`

---

## 👤 Author

**Furkan Çelik**  
Quantitative Research · Data Engineering · Algorithmic Finance  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/celikfrkn)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/celikfrkn)

---

*This project is for educational and research purposes. Nothing in this repository constitutes financial advice.*
