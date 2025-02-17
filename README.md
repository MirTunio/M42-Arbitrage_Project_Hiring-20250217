# **Mach 42 Arbitrage Challenge - FEB 2025**  
### **Introduction**  
Arbitrage is a trading strategy that takes advantage of price differences between two securities. In this case, we have two securities, `4010` and `8128`. Prices of `4010` and `8128` can change randomly. If the 'current' price difference `|price 8128 - price 4010|` exceeds 4.0 Rs, a trade opportunity exists. When an opportunity is found we simultaneously BUY the lower-priced security and SELL the higher-priced security to capture the spread.

Note:  For **Challenge A**, 'current' refers to the price difference between `4010` and `8128` when `trader.py` receives the latest UDP message. For **Challenge B**, 'current' refers to price difference between `4010` and `8128` at each row in `test_data.csv`

This challenge includes the following files:

* data_feed_replay.py - this is a python program which simulates the stock market, **this relevant only for those doing Challenge A.** When it is run it either broadcasts price data randomly over UDP, or replays `test_data`. It sends out UDP broadcasts over two ports, `4010` and `8128`, the port on which they broadcasts matches the names of the stocks.
* test_data.csv  - this is the input data for those doing **Challenge B**
* test_data.pkl - this is the input data for those doing **Challenge A** - the file is used by data_feed_replay.py and should not be modified.
* trader.py - a file to get those doing **Challenge A**  started

**From below, select <u>one</u> of the challenges (A or B), whichever is appropriate to your background.**

**Deadline: March 9th 2025**

---

## **Challenge A: Software Engineer / Data Scientist**  
### **Task**  
- Create a program called `trader.py`, which:

  - Listens to the market data feed broadcast over UDP on the localhost.  

  - Checks the 'current' price of `4010` and `8128` and detects a trade opportunity (`|price_4010 - price_8128| > DELTA`)

  - If an opportunity is found, execute a virtual trade by logging it in a csv file called `trades.csv` with headings `time`,` side`,` security` 

    - time - the system time at which the trade was executed

    - side - `BUY` or `SELL`

    - security - which security was bought or sold, i.e. `4010` or `8128` 

- Testing your code:  
  1. Start your `trader.py` Running your arbitrage algorithm.  
  2. Start the `data_feed_replay.py`  and wait until it is done broadcasting, your `trader.py` should be finding arbitrage opportunities and logging them in the file `trades.csv`
  
- Your `trader.py` will be reviewed for efficiency, and the accuracy of the trades in `trades.csv` will be considered.

- Also keep in mind [Clean code](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29) and [Python Style Guide

### Extra Credit:

  - If you find the above challenge a little easy, take a crack these:
    - [More realistic arbitrage challenge](https://gist.github.com/MirTunio/859ba1f48492eb010d1e89a05faff625)
    - [Time Syncing Challenge](https://github.com/MirTunio/M42-NTP_Project_Hiring-20240129)


---

## **Challenge B: Finance / Accounting**  / Data Science
### **Task**  
- Create an excel spreadsheet to identify trading opportunities from the given data

- Analyze historical price data from the csv file `test_data.csv`  The file is a simple record of the prices received for `4010` and `8128`

- Make excel functions to identify trade opportunities: i.e. whenever the price difference between `4010` and `8128` exceeds `4 Rs`, we have the opportunity to make arbitrage trades. You will buy the lower priced security, and sell the higher priced security.

- In a separate `trade summary` sheet, log all the potential trades in the format:
  `time`, `side`, `security`

  - time - the index number at which the opportunity occurred

  - side - `buy` or `sell`

  - security - which security was bought or sold, i.e. `4010` or `8128` 

- Testing Your Spreadsheet:
  - our spreadsheet should be set up to load `test_data.csv` automatically (e.g., via Power Query or built-in formulas).
  - The logic should run on the input data and dynamically identify arbitrage opportunities 
  - The `trade summary` sheet should dynamically update accordingly


---

## **Submission Guidelines**  
- **Software Engineers / Data Scientists:** 
  - Submit `trader.py` and `trades.csv`.
  - Include a brief `.txt` or `.md` file explaining your approach.

- **Finance / Accounting Candidates:** Submit a spreadsheet `arbitrage.xlsx` , along with a brief description of your approach in one of the sheets.
- Send your responses to info@machfortytwo.com
- **Deadline: March 9th 2025**

## **Final Note - Asking Questions!**

At M42 everyone is working on projects that are slightly beyond their knowledge or ability. It genuinely is NOT easy to develop trading strategies or build the infrastructure we are attempting to. And so we have to constantly pool our knowledge to achieve what we want. And one of the ways we do that is by **asking questions**. So if you have any questions about anything at all to do with this project, send us an email at info@machfortytwo.com and we will be sure to respond. There are no 'simple' or 'basic' questions, share your questions freely. Moreover, the questions you ask will not impact your application, in fact they might actually work in your favor!