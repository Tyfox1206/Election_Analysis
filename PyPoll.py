import os
#import sys
import csv
#os.chdir(os.path.dirname(sys.argv[0]))

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_analysis.txt')
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
     print(headers)

