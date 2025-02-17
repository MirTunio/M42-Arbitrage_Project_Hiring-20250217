"""
Arbitrage Project Mach 42
Trader 2025

This is just a basic framework to get you started
You modify it any way you like, as long as the input
of  market data is from UDP, and the output is a csv
"""

#%% IMPORTS
import socket
import csv
import select
import datetime
import time

#%% SETUP
# UDP Configuration
UDP_IP = "0.0.0.0"  # Listen to all incoming connections
PORTS = [4010, 8128]  # Securities being traded
BUFFER_SIZE = 1024

# Setup UDP rx sockets
sockets = []
for port in PORTS:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", port))
    sock.settimeout(0.1)
    sockets.append(sock)

# Output
trades_made = [] # list which holds tuples of trades made
CSV_FILENAME = "trade_log.csv"

# Algo
#
#

#%% UTILS
def save_trades(trades_made, name=CSV_FILENAME):
    print("Saving trades made...")
    """
    Your code here!
    """

#%% TRADING LOGIC
def trade_arbitrage(delta=4.0):
    print("Started arbitrage trading algo...")
    """
    Your code here!
    """ 

#%% MAIN
if __name__ == '__main__':
    try:
        print("Starting trading - press Ctrl+C to stop")
        trade_arbitrage()
    except KeyboardInterrupt:
        print("Trading halted by user...")
    save_trades(trades_made)
