# Alpaca Market Trading Algorithm

## Introduction

This project is focused on developing an automated trading algorithm using the Alpaca Trade API, targeting the AAPL stock. The algorithm employs moving average strategies to determine optimal buy and sell moments throughout the trading day. We utilize Python for scripting, Pandas for data manipulation, and Alpaca Trade API for real-time trading capabilities.

## Repository Structure

- `project.py`: Main script containing the trading algorithm, data fetching, analysis, and order execution logic.
- `requirements.txt`: Lists all Python dependencies for the project, ensuring replicability.
- `README.md`: Documentation providing an overview, setup guidelines, and additional project insights.

## Code Explanation
The algorithm's strategy hinges on comparing the 20-minute slow EMA with the current VWAP of AAPL. Depending on the comparison:

A buy order is placed if the VWAP falls below the slow EMA, signaling an upward trend.
A sell order is initiated if the VWAP exceeds the slow EMA, indicating a downward trend.
The script orchestrates data retrieval, indicator calculations, and trading decisions within specified market hours, including functionality to preemptively cancel any pending orders.

## Usage Examples
The trading script autonomously executes based on real-time market data. An example console output could be:
Cancelled open order for AAPL
2024-02-13 09:33:00+00:00
Buy order placed for AAPL at $188.05
Cancelled open order for AAPL
2024-02-13 09:37:00+00:00
Buy order placed for AAPL at $188.03
## Results and Screenshots
Outcomes and performance metrics will vary with market conditions. Users are encouraged to test the algorithm in a paper trading setup to evaluate its performance without financial risk.
