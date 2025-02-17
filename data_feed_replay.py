"""
TUNIO 2025
Mach 42

Arbitrage Data Replay
Hiring Project February 2025

This module broadcasts market data in a standard format over UDP
Parts of the operation are left intentionally undocumented
A little bit of reverse engineering is required!


Copyright (C) Mach 42 2025 - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Murtaza Tunio - murtaza (at) machfortytwo.com
"""

#%% IMPORT
import numpy as np
import pandas as pd
import pickle
import random
import time
import socket
from sys import platform

#%% SETUP
# Settings
NUM_MSG = 4000 # per stock
RNDM_OPP_DELTA = 5
REPLAY_DATA_PATH = 'test_data.pkl'
DELAY = 30/1000 # 50 milliseconds

# Start UDP broadcasting server
PORTS = [4010, 8128]
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
if platform == "win32":
    pass
elif platform == "linux" or platform == "linux2":
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.settimeout(0.1)

#%% UTILS
def busy_delay(delay):
    """Accurately delay for given time"""
    if delay == 0: return
    t_start = time.time()
    break_at = t_start + delay
    while True:
        tnow = time.time()
        if tnow > break_at: break

def broadcast(messages_to_send):
    """UDP broadcast messages_to_send"""
    count = 0
    for msg in messages_to_send:
        data, addr = msg
        print(f"{count:05}: {addr}: {data}")
        print("-------------------------")
        addr = int(addr)
        data = str(data)
        server.sendto(data.encode(), ('<broadcast>', addr))
        busy_delay(DELAY)
        count+=1

def random_sparse_array(L, N):
    arr = np.zeros(L, dtype=int)
    indices = np.random.choice(L, N//2, replace=False)
    arr[indices] = RNDM_OPP_DELTA
    indices = np.random.choice(L, N//2, replace=False)
    arr[indices] = -1 * RNDM_OPP_DELTA
    return arr

def gen_rndm_data():
    """Generates random market data"""
    print("    Generating random data...")
    # Generate values
    true_value = [random.gauss(100, 4) for _ in range(NUM_MSG)]
    true_value = np.convolve(true_value, np.ones(20) / 20, mode='valid')
    true_value = true_value
    price_a = true_value + [random.gauss(0,0.5) for _ in range(len(true_value))]
    price_b = true_value + [random.gauss(0,0.5) for _ in range(len(true_value))]
    
    # Round values
    price_a = np.around(price_a, 2)
    price_b = np.around(price_b, 2)
    
    # Add opps
    price_a_opps = random_sparse_array(len(price_a), len(price_a)//100)
    price_b_opps = random_sparse_array(len(price_a), len(price_a)//100)
    price_a += price_a_opps
    price_b += price_b_opps
    
    # ax = pd.DataFrame(true_value).plot()
    # pd.DataFrame(price_a).plot(ax=ax)
    # pd.DataFrame(price_b).plot(ax=ax)
    
    # Format for sending
    a_port = (np.ones(len(price_a)) * PORTS[0]).astype(int)
    b_port = (np.ones(len(price_a)) * PORTS[1]).astype(int)
    a_data = list(zip(price_a, a_port))
    b_data = list(zip(price_b, b_port))
    messages_to_send = []
    assert len(a_data) == len(b_data)
    for i in range(len(a_data)):
        messages_to_send += [a_data[i]]
        messages_to_send += [b_data[i]]
    return messages_to_send

def make_df(messages_to_send):
    csv_out_df = pd.DataFrame(columns=['stock_no', 'price', ])
    for msg in messages_to_send:
        data, addr = msg
        new_row = pd.DataFrame({'stock_no': [addr], 'price': [data]})
        csv_out_df = pd.concat([csv_out_df, new_row], ignore_index=True)
    return csv_out_df

# Save messages_to_send type data to pkl and csv
def save_gen_data(messages_to_send, name=REPLAY_DATA_PATH):
    with open(name, "wb") as f:
        pickle.dump(messages_to_send, f)
    csv_name = REPLAY_DATA_PATH.split('.')[0] + '.csv'
    make_df(messages_to_send).to_csv(csv_name)

def load_from_pkl(name=REPLAY_DATA_PATH):
    with open(REPLAY_DATA_PATH, "rb") as f:  # "rb" = read binary
        messages_to_send = pickle.load(f)
    return messages_to_send

#%% DATA SOURCES
def rndm():
    messages_to_send = gen_rndm_data()
    broadcast(messages_to_send)
    return 'done'

def replay():
    """Replay market data"""
    print(f"    Replaying data from {REPLAY_DATA_PATH}")
    messages_to_send = load_from_pkl()
    broadcast(messages_to_send)
    return 'done'

data_types = {'Random market data': rndm,
              'Real data replay': replay,
              }

#%%
if __name__ == '__main__':
    print("")
    print("Which data do you want to broadcast?: ")
    print("    0. Random market data")
    print(f"    1. Data replay {REPLAY_DATA_PATH}")
    n = input("Type the number (0 or 1) and press enter: ")
    while n not in ['0', '1',]:
        n = input("Invalid input, please type a number 0 or 1 and press enter: ")
    n = int(n)
    choice = list(data_types.keys())[n]

    print(f"You have chosen {choice}")
    print("Starting in 5 seconds")
    time.sleep(5.1)
    print("Starting!")
    print(data_types[choice]())
    print('done')

