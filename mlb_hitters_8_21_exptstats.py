#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:13:05 2020

@author: michaeljorisch
"""

import csv
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

filename = 'expected_stats_8_21.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    players = []
    for i, row in enumerate(reader):
        last = row[0]
        first = row[1]
        est_woba = float(row[13])
        est_woba_minus_woba_diff = float(row[14])
        name = first + ' ' + last        
        players.append((
            name,
            {
            'value': est_woba,
            'label': name,
            },
            {
            'value': est_woba_minus_woba_diff,
            'label': name,
            }
        )) 
                    
players = sorted(players, key=lambda t: t[1]['value'], reverse=True)
players_top30 = players[20:50]

# print(list(zip(players)))

names, est_woba_dicts, est_woba_minus_woba_diff_dicts  = zip(*players_top30)
        
#Make visualization.
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Line(my_config, style=my_style)
chart.title = 'Top MLB Hitters Expected wOBA and wOBA'
chart.x_labels = names

chart.add('Expected wOBA', est_woba_dicts)
chart.add('Expected vs Actual wOBA Diff', est_woba_minus_woba_diff_dicts, secondary=True)
chart.render_to_file('wOBA_dff_data.svg')
            
        