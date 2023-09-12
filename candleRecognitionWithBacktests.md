
# Hammer Pattern Detection and Trading Strategy

This README file provides an overview of the Python code that identifies hammer candlestick patterns in historical financial data using Yahoo Finance data (via yfinance library). It calculates various trading metrics and plots cumulative profit and loss (P&L) curves for both a pattern-based strategy and a long-only strategy.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Results](#results)
- [License](#license)

## Introduction

The code presented here is designed to analyze historical stock market data and identify hammer candlestick patterns. A hammer is a bullish reversal pattern characterized by a small real body (the difference between the open and close prices) near the top of the candlestick and a long lower shadow. The code performs the following tasks:

1. Downloads historical stock market data for a given ticker symbol and date range.
2. Identifies hammer patterns within the data and marks them.
3. Calculates profit and loss (P&L) for 4 trading strategies: 3 pattern-based strategies and a long-only strategy.
4. Prints trade metrics such as the number of trades and average P&L.
5. Plots cumulative P&L curves for both trading strategies.
6. Exports the data with P&L information to a CSV file.

![image](https://github.com/jamiePDunne/scanners/assets/83908748/781edf3b-d601-4eaa-95de-574d4e34e07f)


## Requirements

Before using this code, you need to have the following libraries installed:

- `yfinance`: Used to download historical stock market data.
- `pandas`: Used for data manipulation and analysis.
- `matplotlib`: Used for creating P&L curves and visualizations.

You can install these libraries using `pip`:

```bash
pip install yfinance pandas matplotlib
```

## Usage

1. Clone this repository or download the code file to your local machine.
2. Make sure you meet the requirements listed above.
3. Modify the `ticker_symbol`, `start_date`, and `end_date` variables in the `main` function to specify the stock you want to analyze and the date range for the data.
4. Run the code using a Python interpreter:

```bash
python your_file_name.py
```

The code will execute and provide trade metrics in the console, as well as generate P&L curves and save the data to a CSV file.

## Code Overview

The code is divided into several functions, each with a specific purpose:

- `download_data`: Downloads historical data for a given ticker symbol and date range using Yahoo Finance.

- `identify_hammer`: Identifies hammer patterns in the data and marks them with a "Signal" column.

- `calculate_pnls`: Calculates various P&L columns and cumulative P&L curves for both pattern-based and long-only trading strategies.

- `calculate_trade_metrics`: Computes trade metrics such as the number of trades and average P&L for both strategies.

- `print_trade_metrics`: Prints the calculated trade metrics and execution time.

- `plot_curves`: Plots cumulative P&L curves for pattern-based and long-only strategies.

- `main`: The main function that orchestrates the entire process.

## Results

After running the code, you will see trade metrics for both trading strategies, including the total number of trades and average P&L. Additionally, cumulative P&L curves will be displayed in a plot. The data with P&L information will also be saved to a CSV file named "hammer_patterns_with_pnl_and_curves.csv" in the same directory as the code file.

## License

This code is provided under the [MIT License](LICENSE). You are free to use, modify, and distribute it as needed.
