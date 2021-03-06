"""
CSE 163
Ethan Hu
Verifies the plotly graphing functions by making
the same graphs without plotly. Assumes that
the requisite libaries are installed and that there is a
valid csv of IMDB data.
"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv("movies.csv")
    data = data.dropna()
    bar_test(data)
    scatter_test(data)


def bar_test(data):
    """
    Given an IMDB dataframe, makes a bar plot to compare
    with output from research_question_1.py. Assumes that the
    given dataframe is properly preprocessed.
    """
    data = data.groupby("genre").mean()
    data.reset_index(inplace=True)
    data = data.sort_values("score")
    data.plot(x="genre", y="score", kind="bar")
    plt.savefig("bar_test.png")


def scatter_test(data):
    """
    Given an IMDB dataframe, makes a bar plot to compare
    with output from research_question_1.py. Assumes that the
    given dataframe is properly preprocessed.
    """
    data.plot(x="budget", y="score", kind="scatter")
    plt.savefig("scatter_test.png")


if __name__ == '__main__':
    main()
