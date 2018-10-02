#!/usr/bin/env python

import matplotlib

matplotlib.use('pgf')
pgf_parameters = {
        'text.usetex': True,
        'figure.figsize': [4.8, 3],
        'pgf.rcfonts': False,
        'pgf.texsystem': 'pdflatex',
        }

matplotlib.rcParams.update(pgf_parameters)

import matplotlib.pyplot as plt
import numpy as np
import TISTNplot as TN # https://HHS-TN.github.io
TN.PRECISION_X = 3
data = np.loadtxt('data.csv', delimiter=',')

t = data[:,0]
x = data[:,1]*9.81 #m/s^2
y = data[:,2]*9.81 #m/s^2
z = data[:,3]*9.81 #m/s^2
t = t - t[0]

plt.figure()
plt.grid()
plt.plot(t,x,label='x')
plt.plot(t,y,label='y')
plt.legend(loc=0) # best

TN.label_y('a', 'm/s^2', plt.gca())
TN.label_x('t', 's', plt.gca())

TN.fix_axis(plt.gca())

plt.tight_layout()

plt.savefig('pythonfigure.pdf')
plt.savefig('pythonfigure.pgf')

