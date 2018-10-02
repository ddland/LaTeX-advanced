#!/usr/bin/env python

import numpy as np

data = np.loadtxt('data.csv', delimiter=',')

number_lines = 10

header = r'''\begin{tabularx}{0.6\textwidth}{SSSS}
{tijd [\si{s}]} & {$a_x$ [\si{\meter\per\second\squared}]} & {$a_y$ [\si{\meter\per\second\squared}]} & {$a_z$ [\si{\meter\per\second\squared}]}\\'''


fh = open('pythontable.tex', 'w')

print(header, file=fh)
print('\hline', file=fh)
for i in range(number_lines):
    print(r'{time:5.3f} & {ax:5.3f} & {ay:5.3f} & {az:5.3f} \\'.format(time=data[i,0]-data[0,0], ax=data[i,1], ay=data[i,2], az=data[i,3]), file=fh)
print(r'\hline', file=fh)
print(r'\end{tabularx}', file=fh)
