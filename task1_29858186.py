# File name: task1_29858186.py
# Author: Akshay Sapra
# Student Id: 29858186
# Semester 2, year 2018
# Date: 10/10/2018
# Description: this file is created to pre process the files by removing certain tokens and extracting statement
#              starting with *Chi

import os
import re
# imported os and re libraries for directory path and regular expression


class PrePocessor:

    def __init__(self):
        number_of_files = 10  # number of files to be taken as input
        SLI = {}  # Dictionary to load SLI scripts
        SLI_only_CHI = {}  # Dictionary to load filtered (with only CHI) SLI data
        TD = {}  # Dictionary to load TD script
        TD_only_CHI = {}  # Dictionary to load filtered (with only CHI) TD data data
        # check if output directory for SLI exists, if not then create one
        if not os.path.exists("SLI_Cleaned"):
            os.mkdir("SLI_Cleaned")
        # check if output directory for TD exists, if not then create one
        if not os.path.exists("TD_Cleaned"):
            os.mkdir("TD_Cleaned")    # Reference: https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
        for i in range(1, number_of_files+1):  # looping for all SLI files
            file = open("SLI-"+str(i)+".txt")
            SLI[i] = file.read()   # Reading the file and storing it in SLI dictionary
            SLI[i] = SLI[i].replace('\n', ' ')  # for each SLI file replacing new line character with space and making entire file as one string.
            SLI[i] = SLI[i].replace('@', '\n@')  # Adding new line character before special symbol @
            SLI[i] = SLI[i].replace('*', '\n*')  # Adding new line character before special symbol *
            SLI[i] = SLI[i].replace('%', '\n%')  # Adding new line character before special symbol %
            SLI[i] = SLI[i].replace('[\n*', '[*')  # fixing extra new line character after *
            SLI[i] = SLI[i].split('\n')     # Splitting entire file on the basis of new line characters
            SLI_only_CHI[i] = []   # adding list to each element of SLI_only_CHI
            new_file = open("./SLI_Cleaned/SLI-" + str(i) + ".txt", 'w')  # Opening new file in the folder named “SLI_cleaned” to store cleaned scripts,
            for each in range(len(SLI[i])):
                if SLI[i][each].startswith("*CHI"):  # Taking lines that start with *CHI
                    SLI[i][each] = SLI[i][each].replace('*CHI:\t', '')
                    SLI_only_CHI[i].append(SLI[i][each])
            for each in range(len(SLI_only_CHI[i])):
                SLI_only_CHI[i][each] = re.sub(r'<', '', SLI_only_CHI[i][each])       # task 1 (b)
                SLI_only_CHI[i][each] = re.sub(r'>', '', SLI_only_CHI[i][each])       # task 1 (b)
                SLI_only_CHI[i][each] = re.sub(r'\(([a-z]*)\)', r'\1', SLI_only_CHI[i][each])        # Task 1(d) Reference: https://stackoverflow.com/questions/7191209/python-re-sub-replace-with-matched-content
                SLI_only_CHI[i][each] = re.sub(r'(\s|\n|^)\+\S+','', SLI_only_CHI[i][each])       # Task 1 c
                SLI_only_CHI[i][each] = re.sub(r'(\s|\n|^)\&\S+', '', SLI_only_CHI[i][each])        # Task 1 c
                SLI_only_CHI[i][each] = re.sub(r'\[[^\/*].*?\]', '', SLI_only_CHI[i][each])  # Task 1 a
                SLI_only_CHI[i][each] = re.sub(r'\((...)\)', '', SLI_only_CHI[i][each])  # removing (...)
                SLI_only_CHI[i][each] = re.sub(r'\((..)\)', '', SLI_only_CHI[i][each])  # removing (..)
                SLI_only_CHI[i][each] = re.sub(r'\[/-\]', '', SLI_only_CHI[i][each])  # removing [/-]
                new_file.write(SLI_only_CHI[i][each])  # Writing in each file
                new_file.write("\n")
            new_file.close()
            file.close()

        for i in range(1, number_of_files+1):   # looping for all TD files
            file = open("TD-"+str(i)+".txt")
            TD[i] = file.read()  # Reading the file and storing it in TD dictionary
            TD[i] = TD[i].replace('\n', ' ')  # for each TD file replacing new line character with space and making entire file as one string.
            TD[i] = TD[i].replace('@', '\n@')  # Adding new line character before special symbol @
            TD[i] = TD[i].replace('*', '\n*')  # Adding new line character before special symbol *
            TD[i] = TD[i].replace('%', '\n%')  # Adding new line character before special symbol %
            TD[i] = TD[i].replace('[\n*', '[*')  # fixing extra new line character after *
            TD[i] = TD[i].split('\n')  # Splitting entire file on the basis of new line characters
            TD_only_CHI[i] = []  # adding list to each element of TD_only_CHI
            new_file = open("./TD_Cleaned/TD-" + str(i) + ".txt", 'w')   # Opening new file to the folder named “TD_cleaned” to store cleaned scripts,
            for each in range(len(TD[i])):
                if TD[i][each].startswith("*CHI"):  # Taking lines that start with *CHI
                    TD[i][each] = TD[i][each].replace('*CHI:\t', '')
                    TD_only_CHI[i].append(TD[i][each])
            for each in range(len(TD_only_CHI[i])):
                TD_only_CHI[i][each] = re.sub(r'<', '', TD_only_CHI[i][each])       # task 1 (b)
                TD_only_CHI[i][each] = re.sub(r'>', '', TD_only_CHI[i][each])       # task 1 (b)
                TD_only_CHI[i][each] = re.sub(r'\(([a-z]*)\)', r'\1', TD_only_CHI[i][each])      # Task 1(d) REference: https://stackoverflow.com/questions/7191209/python-re-sub-replace-with-matched-content
                TD_only_CHI[i][each] = re.sub(r'\s\+\S+','', TD_only_CHI[i][each])       # Task 1 c
                TD_only_CHI[i][each] = re.sub(r'\s\&\S+', '', TD_only_CHI[i][each])      # Task 1 c
                TD_only_CHI[i][each] = re.sub(r'\[[^\/*]*\]', '', TD_only_CHI[i][each])  # Task 1 a
                TD_only_CHI[i][each] = re.sub(r'\((...)\)', '', TD_only_CHI[i][each])  # removing (...)
                TD_only_CHI[i][each] = re.sub(r'\((..)\)', '', TD_only_CHI[i][each])  # removing (..)
                TD_only_CHI[i][each] = re.sub(r'\[/-\]', '', TD_only_CHI[i][each])  # removing (..)
                new_file.write(TD_only_CHI[i][each])  # Writing in each file
                new_file.write("\n")
            new_file.close()
            file.close()
        print("Pre-processing done !")


