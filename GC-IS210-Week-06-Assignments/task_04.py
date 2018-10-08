#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""For loop function to calculate sum (integer) and average (float)."""

def process_data(data):
    """Calculates total sum and data average."""
    total_sum = sum(data)
    counter = 0

    for xrange(len(data)):
        counter += 1
        data_average = float(total_sum/counter)
    return (total_sum, data_average)

print process_data([1,2,3])
