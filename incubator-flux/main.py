# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
from core.analyzer import *


Header = [
    'TranID', 'Time',	'Price', 'Volume', 
    'SaleOrderVolume', 'BuyOrderVolume', 'Type', 
    'SaleOrderID', 'SaleOrderPrice', 'BuyOrderID', 
    'BuyOrderPrice'
]


def list_files(code='000001'):
    code = '{}.csv'.format(code)
    paths = []
    for root, dirs, files in os.walk('Level_2_Data'):
        if files:
            paths += [os.path.join(root, f) for f in files if code == f]
    return paths



# 时间、开盘价、收盘价、最高价、最低价

def main():
    code = '000001'
    files = list_files(code)
    for csv_path in files:
        df = pd.read_csv(csv_path)
        print(df['TranID'])


if __name__ == '__main__':
    main()