# File name: task2_29858186.py
# Author: Akshay Sapra
# Student Id: 29858186
# Semester 2, year 2018
# Date: 10/10/2018
# Description:  produce a number of statistics for the two groups of children transcripts
# • Length of the transcript — indicated by the number of statements
# • Size of the vocabulary — indicated by the number of unique words
# • Number of repetition for certain words or phrases — indicated by the CHAT symbol [/]
# • Number of retracing for certain words or phrases — indicated by the CHAT symbol [//]
# • Number of grammatical errors detected — indicated by the CHAT symbol [*]3
# • Number of pauses made — indicated by the CHAT symbol (.)


class Analyser:
    def __init__(self):  # Constructor  for creating instances of this class
        self.SLI = {}
        self.lenght_of_statement = {}  # Dictionary to store length of statements
        self.size_of_vocab = {}  # Dictionary to store size of vocabulary
        self.num_of_slash = {}  # Dictionary to store [/]
        self.num_of_double_slash = {}  # Dictionary to store [//]
        self.num_of_gram_err = {}   # Dictionary to store grammatical errors
        self.num_of_pause = {}  # Dictionary to store (.)
        self.data = []   # List tp store all the statistics in order lenght_of_statement, num_of_pause, num_of_gram_err, num_of_slash, num_of_double_slash, size_of_vocab
        self.number_of_files = 10

    def __str__(self):  # Re-defining this method to present the data
        analyser_details = ''
        for file_num in range(1 , self.number_of_files+1):
            analyser_details += "\nLength of the transcript number "+str(file_num)+" is "+str(self.lenght_of_statement[file_num])
            analyser_details += "\nSize of the vocabulary of transcript number "+str(file_num)+" is " + str(self.size_of_vocab[file_num])
            analyser_details += "\nNumber of repetition for certain words or phrases in transcript number "+str(file_num)+" is " + str(self.num_of_slash[file_num])
            analyser_details += "\nNumber of retracing for certain words or phrases in transcript number "+str(file_num)+" is " + str(self.num_of_double_slash[file_num])
            analyser_details += "\nNumber of Grammatical error in transcript number "+str(file_num)+" is " + str(self.num_of_gram_err[file_num])
            analyser_details += "\nNumber of Pauses in transcript number "+str(file_num)+" is " + str(self.num_of_pause[file_num])
            analyser_details += "\n"
        return analyser_details

    def analyse_script(self, cleaned_file):  # method to perform the analysis on a given cleaned script
        for i in range(1, self.number_of_files+1):
            file = open("./"+str(cleaned_file)+"_Cleaned/"+str(cleaned_file)+"-" + str(i) + ".txt", 'r')
            self.SLI[i] = file.read()  # Reading clean files
            self.SLI[i] = self.SLI[i].split('\n')
            self.lenght_of_statement[i] = len(self.SLI[i]) - 1   # reduced 1 from the length of statements as new line character is added to the end of each file
            # Declaring temporary variables for counting the statistics
            temp_set = set()
            temp_slash = 0
            temp_double_slash = 0
            temp_gram_err = 0
            temp_pause = 0
            for each in range(len(self.SLI[i])):
                self.SLI[i][each] = self.SLI[i][each].split() # Dividing each line into words
                for eacher in range(len(self.SLI[i][each])):
                    # checking for each statistics for each word
                    if '[/]' in self.SLI[i][each][eacher]:
                        temp_slash += 1
                    if '[//]' in self.SLI[i][each][eacher]:
                        temp_double_slash += 1
                    if '*' in self.SLI[i][each][eacher]:
                        temp_gram_err += 1
                    if '(.)' in self.SLI[i][each][eacher]:
                        temp_pause += 1
                    self.SLI[i][each][eacher] = self.SLI[i][each][eacher].replace(',', '')
                    temp_set.add(self.SLI[i][each][eacher].upper())
                    if '[' in self.SLI[i][each][eacher]:
                        temp_set.discard(self.SLI[i][each][eacher])
                    if ']' in self.SLI[i][each][eacher]:
                        temp_set.discard(self.SLI[i][each][eacher])
                    if '(' in self.SLI[i][each][eacher]:
                        temp_set.discard(self.SLI[i][each][eacher])
            # storing the count of each statistics in respective variables
            self.num_of_slash[i] = temp_slash
            self.num_of_double_slash[i] = temp_double_slash
            self.num_of_gram_err[i] = temp_gram_err
            self.num_of_pause[i] = temp_pause
            temp_set.discard('!')
            temp_set.discard('?')
            temp_set.discard('.')
            self.size_of_vocab[i] = len(temp_set)
        # appending the statistics to a single list
        self.data.append(self.lenght_of_statement)
        self.data.append(self.num_of_pause)
        self.data.append(self.num_of_gram_err)
        self.data.append(self.num_of_slash)
        self.data.append(self.num_of_double_slash)
        self.data.append(self.size_of_vocab)
        file.close()
