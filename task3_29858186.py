# File name: task3_29858186.py
# Author: Akshay Sapra
# Student Id: 29858186
# Semester 2, year 2018
# Date: 10/10/2018
# Description:  class to visualise the statistics collected in Section 2.3
# (Task 2) as some form of graphs

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Visualiser:
    def __init__(self, data):  # constructor for creating instances of this class
        self.avg = {}   # Dictionary to store average of each statistics
        self.data = data  # instantiating the data value generated from task 2

    def compute_averages(self):  # method to find mean of the six statistics for each child group (i.e. both the SLI and TD groups).
        for each in range(len(self.data)):
            tmp_var = 0
            for eacher in self.data[each]:
                tmp_var += self.data[each][eacher]
            self.avg[each + 1] = tmp_var/10
        return self.avg

    def visualise_statistics(self):  # Method to construct the graph
        df = self.compute_averages()
        avg_stat = pd.DataFrame.from_dict(df, orient='index')  # Converting the average statistics into dataframe
        # print(df)
        # print(avg_stat[0])
        ind = np.arange(6)
        plt.bar(ind, avg_stat[0], 0.5 )  # plotting the bar plot. avg_stat[0] where 0 is column name
        # setting bar plot parameters
        for each_x, each_y in zip(ind, avg_stat[0]):
            plt.text(each_x-0.2, each_y+1, str(each_y)) # Reference: https://www.reddit.com/r/learnpython/comments/2y9zwq/adding_value_labels_on_bars_in_a_matplotlib_bar/
        plt.ylabel('Count')
        plt.title('Average Statistics of Transcripts')
        plt.grid('True')
        plt.xticks(ind, ['Length of\nTranscript', 'Pauses', 'Grammatical\nErrors', 'Repetitions', 'Retracings', 'Size of\nVocabulary'])
        plt.xlabel("True")
        plt.show()



