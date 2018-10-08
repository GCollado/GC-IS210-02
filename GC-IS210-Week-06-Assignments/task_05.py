#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Reverses the order of nested immutables."""

def flip_keys(to_flip = [[],[]]):
        counter = 0
        for i in range(len(to_flip)):
                for i in range(len(to_flip[i])):
                        to_flip[counter] = to_flip[i][i][::-1]
                        counter += 1
        return to_flip
