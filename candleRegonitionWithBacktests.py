import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import time


def download_data(ticker_symbol, start_date, end_date):
    """
    Download historical data for a given ticker symbol and date range.
    """
    data = yf.download(ticker_symbol, start=start_date, end=end_date)
    data = data.sort_index()
    data.reset_index(inplace=True)
    return data


def identify_hammer(data):
    """
    Identify hammer patterns and mark the "Signal" column in the DataFrame.
    """
    data["Signal"] = 0
    for i in range(2, len(data) - 2):
        if (
                data["Low"][i] < data["Open"][i]
                and data["Low"][i] < data["Close"][i]
                and data["Open"][i] > data["Close"][i]
                and data["Open"][i] - data["Low"][i] > data["High"][i] - data["Open"][i]
                and data["Open"][i] - data["Low"][i] > data["High"][i] - data["Close"][i]
        ):
            data.loc[data.index[i], "Signal"] = 1
    return data


def calculate_pnls(data):
    """
    Calculate P&L columns and cumulative sum columns.
    """
    data["pnl_pattern_overnight"] = ((data["Open"] - data["Close"].shift()) / data["Close"].shift()) * data[
        "Signal"].shift()
    data["pnl_pattern_day_pnl"] = ((data["Close"] - data["Open"]) / data["Open"]) * data["Signal"].shift()
    data["pnl_pattern_closeclose"] = ((data["Close"] - data["Close"].shift()) / data["Close"].shift()) * data[
        "Signal"].shift()
    data["pnl_long_only"] = (data["Close"] - data["Close"].shift()) / data["Close"].shift()

    data["pnl_pattern_overnight_curve"] = data["pnl_pattern_overnight"].cumsum()
    data["pnl_pattern_day_curve"] = data["pnl_pattern_day_pnl"].cumsum()
    data["pnl_pattern_closeclose_curve"] = data["pnl_pattern_closeclose"].cumsum()
    data["pnl_long_only_curve"] = data["pnl_long_only"].cumsum()

    return data


def calculate_trade_metrics(data):
    """
    Calculate trade metrics including total trades and average P&Ls.
    """
    total_pattern_trades = data["Signal"].sum()
    total_long_only_trades = len(data)

    pattern_pnl_metrics = {
        "Total Pattern Trades": total_pattern_trades,
        "Average Pattern P&L": data[
                                   "pnl_pattern_overnight"].sum() / total_pattern_trades if total_pattern_trades > 0 else 0,
        "Total Pattern P&L": data["pnl_pattern_overnight"].sum(),
    }

    long_only_pnl_metrics = {
        "Total Long-Only Trades": total_long_only_trades,
        "Average Long-Only P&L": data[
                                     "pnl_long_only"].sum() / total_long_only_trades if total_long_only_trades > 0 else 0,
        "Total Long-Only P&L": data["pnl_long_only"].sum(),
    }

    return pattern_pnl_metrics, long_only_pnl_metrics


def print_trade_metrics(pattern_pnl_metrics, long_only_pnl_metrics, execution_time_ms):
    """
    Print trade metrics and execution time.
    """
    print("Pattern P&L Metrics:")
    for key, value in pattern_pnl_metrics.items():
        print(f"{key}: {value}")

    print("\nLong-Only P&L Metrics:")
    for key, value in long_only_pnl_metrics.items():
        print(f"{key}: {value}")

    print(f"\nExecution Time: {execution_time_ms:.2f} ms")


def plot_curves(data, ticker_symbol):
    """
    Plot P&L cumulative sum curves.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data["Date"], data["pnl_pattern_overnight_curve"], label="pnl_pattern_overnight_curve")
    plt.plot(data["Date"], data["pnl_pattern_day_curve"], label="pnl_pattern_day_pnl_curve")
    plt.plot(data["Date"], data["pnl_pattern_closeclose_curve"], label="pnl_pattern_closeclose_curve")
    plt.plot(data["Date"], data["pnl_long_only_curve"], label="pnl_long_only_curve")

    plt.xlabel("Date")
    plt.ylabel("P&L Cumulative Sum")
    plt.title(f"P&L Cumulative Sum Curves - Ticker: {ticker_symbol}")
    plt.legend()
    plt.show()


def main():
    start_time = time.time()
    ticker_symbol = "^GSPC"
    start_date = "2000-01-01"
    end_date = "2023-12-31"

    data = download_data(ticker_symbol, start_date, end_date)
    data = identify_hammer(data)
    data = calculate_pnls(data)

    pattern_pnl_metrics, long_only_pnl_metrics = calculate_trade_metrics(data)
    execution_time_ms = (time.time() - start_time) * 1000

    print_trade_metrics(pattern_pnl_metrics, long_only_pnl_metrics, execution_time_ms)
    plot_curves(data, ticker_symbol)
    data.to_csv("hammer_patterns_with_pnl_and_curves.csv", index=False)


if __name__ == "__main__":
    main()
