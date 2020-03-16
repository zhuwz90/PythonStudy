# -*- coding: UTF-8 -*-

from extract_data import DataExtractor
from os import path
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import numpy as np
import argparse


def get_data(infile, keyword, outfile):
    extractor = DataExtractor(infile, keyword, outfile)
    data = extractor.data_after_keyword()
    if data:
        print("Export data from file[%s] after keyword[%s] successed!" % (
            infile, keyword))
    else:
        print("Export data from file[%s] after keyword[%s] failed!" % (
            infile, keyword))

    return data


def draw_data(data, title):
    if not data:
        return False

    x = np.arange(len(data))
    y = np.array(data)
    plt.figure()
    plt.plot(x, y, color='r', lw=0.2)
    plt.xlim(0, max(x))
    plt.ylim(0, max(y) * 1.2)
    # x_major_locator = MultipleLocator(500)  # X轴刻度间隔设置为500
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(x_major_locator)
    plt.title(title)
    plt.show()


def main():
    ''' Main function '''

    parser = argparse.ArgumentParser(
        description='Draw data which extract from file.')
    parser.add_argument('infile', help='input file which contains data')
    parser.add_argument('keyword', help='keywords for find data')
    parser.add_argument('-o', '--outfile',
                        default=path.basename(__file__).split('.')[0] + '.out',
                        help='output file for save data')

    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile
    keyword = args.keyword
    data = get_data(infile, keyword, outfile)
    draw_data(data, keyword)


if __name__ == '__main__':
    main()
