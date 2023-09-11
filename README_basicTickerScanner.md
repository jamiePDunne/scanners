

# Basic Market Scanner

The Basic Market Scanner is a Python script that allows you to scan and analyze key market indicators for a list of cryptocurrency pairs. It retrieves data from Yahoo Finance, calculates various technical indicators, and presents the information in a color-coded tabular format for easy analysis.

## Features

- **Data:** The script supports scanning multiple cryptocurrency pairs such as Bitcoin (BTC-USD), Ethereum (ETH-USD), Ripple (XRP-USD), Litecoin (LTC-USD), and Bitcoin Cash (BCH-USD). You can customize the list of pairs by editing the `index_tickers` variable.

- **Technical Indicators:** The following technical indicators are calculated for each cryptocurrency pair:
  - Average True Range (ATR)
  - Simple Moving Averages (SMA) for 20, 50, and 200 periods
  - Relative Strength Index (RSI)

- **Price Change Styling:** The script visually highlights positive and negative price changes and SMA percentage differences in the tabular output. Green indicates positive changes, while pink indicates negative changes.

- ![image](https://github.com/jamiePDunne/scanners/assets/83908748/996436a7-61c4-4562-8950-317412a66745)


## Prerequisites

Before running the Basic Market Scanner, make sure you have the following prerequisites installed:

- Python 3.x
- Required Python packages (install using `pip install yfinance pandas`)

## Usage

1. Clone this repository or download the script (`basic_market_scanner.py`) to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```
   python basic_market_scanner.py
   ```

4. The script will retrieve data for the specified cryptocurrency pairs, calculate technical indicators, and display the results in the terminal.

5. The results include ATR, SMA values for 20, 50, and 200 periods, RSI, current price, 52-week high and low, price change, and volume. Positive changes are highlighted in green, and negative changes are highlighted in pink.

6. Analyze the data to make informed decisions about cryptocurrency investments or trading strategies.

## Customization

- To add or remove cryptocurrency pairs for scanning, edit the `index_tickers` variable in the script.

- You can further customize the code to include additional technical indicators or adjust calculation parameters according to your preferences.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script uses the Yahoo Finance API for retrieving historical market data.

Feel free to enhance and adapt this code for your specific needs. Happy market scanning!
