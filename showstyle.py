#!/usr/bin/env python

from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import os
import argparse
HERE = os.path.dirname(__file__)
available = os.listdir(os.path.join(HERE, 'rc'))

ap = argparse.ArgumentParser()
ap.add_argument('style', help='Which rc file to use.  One of %s' % available)
ap.add_argument('--plot', default='all', help='One of [scatter, hist, line, image], or '
                'a comma-separated list of a subset.  Default is all.')
ap.add_argument('-o', '--output', required=False, help='Render the plot to a file')
args = ap.parse_args()

matplotlib.rc_file(os.path.join(HERE, 'rc', args.style))

def lineplot(ax):
    x = np.linspace(0, 4*np.pi, 100)
    y = np.sin(x)
    for i, offset in enumerate((np.arange(5) / 3.)):
        ax.plot(x, y + offset, label='line %s' % i)
    ax.set_ylabel('y values')
    ax.set_xlabel('x values')
    ax.set_title('demo plot')
    ax.legend(loc='best')

def scatterplot(ax):
    x = np.random.random(1000)
    y = np.random.random(1000)
    ax.scatter(x, y, label='scatter 1',
               c=matplotlib.rcParams['axes.color_cycle'][0],
               s=50)
    ax.set_ylabel('y values')
    ax.set_xlabel('x values')
    ax.set_title('demo plot')
    ax.legend(loc='best')

def histogram(ax):
    x = np.random.poisson(4, 1000)
    ax.hist(x, label='hist 1')
    ax.set_ylabel('y values')
    ax.set_xlabel('x values')
    ax.set_title('demo plot')
    ax.legend(loc='best')

fig = plt.figure(figsize=(11, 8))

def image(ax):
    ax.imshow(np.random.random((100, 100)))

if 'line' in args.plot or args.plot == 'all':
    ax = fig.add_subplot(221)
    lineplot(ax)

if 'scatter' in args.plot or args.plot == 'all':
    ax = fig.add_subplot(222)
    scatterplot(ax)

if 'hist' in args.plot or args.plot == 'all':
    ax = fig.add_subplot(223)
    histogram(ax)

if 'image' in args.plot or args.plot == 'all':
    ax = fig.add_subplot(224)
    image(ax)

plt.tight_layout()
if args.output:
    plt.savefig(args.output)
else:
    plt.show()
