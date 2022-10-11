# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:13:26 2022

@author: andile.mbele
"""


import csv


def parser():
    with open('C:/Users/andile.mbele\Desktop/prescient/code/training/SQL_DUMPS/SqlConversions/actomics.com/actomics.com - wpuq_users_fromsql.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # write to a new csv file
        with open('actomics.com - wpuq_users_fromsql.csv', 'w') as new_file:
            writer = csv.writer(new_file)
            writer.writerows(csv_reader)

            # print the new csv file
            for line in csv_reader:
                writer.writerow(line)


if __name__ == '__main__':
    parser()
