# -*- encoding:utf-8 -*-
#
#   savecsv.py
#   tweetgetter
#
#   Copyright (c) 2018 Shota Shimazu. All rights reserved.
#

import csv


def save_as_csv(filename, content, createNew = False):

    if createNew:
        with open(filename, "aw") as f:
            print("File created!")
    
    with open(filename, "w") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(content)
