import numpy as np
from muselearn.src.containers.waveform import Waveform
from muselearn.src.signal_processing.basic import compute_energy
import matplotlib.pyplot as plt
import matplotlib
from typing import List
import seaborn as sns


def calculate_histogram(data: List[np.float64], bins: int):
    frequencies, values = np.histogram(data, bins)
    return frequencies, values


def estimate_distribution(frequencies, values):
    raise NotImplementedError


def plot_kdeplot(data: List[np.float64], axes: matplotlib.axes):
    sns.kdeplot(data=data, kernel='gau', bw='scott', ax=axes)
    axes.set_title('KDE plot')
    axes.set_xlabel('x')
    axes.set_ylabel('f')


def plot_histogram(data: List[np.float64], bins: int, axes: matplotlib.axes):
    axes.hist(x=data, bins=bins)
    axes.set_title('KDE plot')
    axes.set_xlabel('x')
    axes.set_ylabel('f')


if __name__ == '__main__':
    fig, axes = plt.subplots(nrows=1, ncols=1)
    plot_kdeplot(data=np.random.random_sample(100), bins=10, axes=axes)
    plt.show()
