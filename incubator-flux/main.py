# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
from core.analyzer import *
from core.utils import list_files


root_path = 'Level_2_Data'
time = '2019-06-05'
target = '603767.csv'

Header = [
    'TranID', 'Time',	'Price', 'Volume', 
    'SaleOrderVolume', 'BuyOrderVolume', 'Type', 
    'SaleOrderID', 'SaleOrderPrice', 'BuyOrderID', 
    'BuyOrderPrice'
]

def main():
    df = pd.read_csv(os.path.join(root_path, time, target))
    print(df)


if __name__ == '__main__':
    main()