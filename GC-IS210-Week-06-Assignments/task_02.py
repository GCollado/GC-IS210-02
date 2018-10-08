#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Import modules, creates and updates local variable references."""

import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1:2] = ['Swan Lake']
BALLETS.append('Herman Schmerman')
BALLETS.extend(['Don Quixote', 'Sylvia'])


