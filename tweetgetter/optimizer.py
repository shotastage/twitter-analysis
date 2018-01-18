# -*- encoding:utf-8 -*-
#
#   getflow.py
#   tweetgetter
#
#   Copyright (c) 2018 Shota Shimazu. All rights reserved.
#

import json
import csv
import pandas as pd
import numpy as np
import glob



csv_files = glob.glob("./tweets/*.csv")
csv_list = []
tmp_csv_file = str(np.random.rand()) + "optimized.csv"

for f in csv_files:
    csv_list.append(pd.read_csv(f))
    df = pd.concat(csv_list)

df.to_csv(tmp_csv_file)



hoge = pd.read_csv(tmp_csv_file)
sorted_hoge = hoge.sort_values(["name", "text"], ascending=[1, 0])
no_duplicated_hoge = sorted_hoge.drop_duplicates("text", keep='first')
no_duplicated_hoge.to_csv("result.csv")
