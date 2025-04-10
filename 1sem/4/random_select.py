from argparse import ArgumentParser
import numpy as np


if __name__ == '__main__':
    parser = ArgumentParser()

    # python random_select.py --file1 file_1.txt --file2 file_2.txt --p 0.2
    # parser.add_argument('--file1', type=str)
    # parser.add_argument('--file2', type=str)
    # parser.add_argument('--p', type=float)
    # data = parser.parse_args()

    data = {"file1": "file_1.txt", "file2": "file_2.txt", "p": 0.2}

    real = [int(i) for i in open(data["file1"], "r").readline().split()]
    synthetic = [int(i) for i in open(data["file2"], "r").readline().split()]

    mask = np.random.rand(len(real)) < data["p"]


    comb = np.where(mask, synthetic, real)
    print(comb)

    combined = synthetic * mask + real * (1 - mask)
    print(combined)

    choices = np.array([real, synthetic])
    combined = np.choose(mask, choices)
    print(combined)
