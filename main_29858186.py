# File name: main_29858186.py
# Author: Akshay Sapra
# Student Id: 29858186
# Semester 2, year 2018
# Date: 10/10/2018
# Description:  main file to run the task1,2 and 3 to analyse the scripts.


from task2_29858186 import Analyser
from task1_29858186 import PrePocessor
from task3_29858186 import Visualiser


pre_processing = PrePocessor()  # Calling task 1 constructor to perform pre-processing activities
# Creating object of task 2 or analyser class
SLI = Analyser()
TD = Analyser()

# Calling task 2 methods to  create the statistics
SLI.analyse_script("SLI")
TD.analyse_script("TD")

# printing the statistics in readable format
print("*"*50+"SLI Statistics"+"*"*50)
print(SLI)
print("*"*50+"TD Statistics"+"*"*50)
print(TD)

# Creating object of task 3 or visualiser class
vis_SLI = Visualiser(SLI.data)
vis_TD = Visualiser(TD.data)

# Calling visualise statistics to generate graph
vis_SLI.visualise_statistics()
vis_TD.visualise_statistics()
