import numpy as np

def main():
    print(compute_energy(np.ones(10), 1))



def compute_energy(waveform, sampling_rate):
    return np.sum(amplitude**2 for amplitude in waveform) * 1/sampling_rate


if __name__ == '__main__':
    main()
