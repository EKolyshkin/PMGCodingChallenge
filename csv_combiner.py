#!/usr/bin/env python3

import os.path
import sys

class Combiner():
    # checks for any errors that may exist, quits if error is found
    def checkErrors(self, argv, argvCount):
        if argvCount < 2: # if user did not provide arguments
            return False

        for i in range(1, argvCount):
            if not os.path.exists(argv[i]):
                return False  # if argument filename doesn't exist
            if argv[i].find('.csv') == -1:
                return False  # if argument filename doesn't contain CSV extension
            
        return True # returns True if no errors found

    # outputs all files listed in arguments in new form to stdout
    def combineFiles(self, argv):
        argvCount = len(argv) # total count of existing filename arguments
        if not self.checkErrors(argv, argvCount):
            return False

        self.printHeader(argv)
        for i in range(1, argvCount): # for each argument filename, print appended file
            self.printFile(argv, i)

        return True # returns True upon successful operation

    # prints file located at argv[num] 
    def printFile(self, argv, num):
        with open(argv[num], 'r') as file: # open file for reading
            fileName = ',"' + file.name.split(os.sep)[-1] + '"'
            file.readline() # ignore header line
            for line in file: # for each line in file, print modified line
                self.printLine(line, fileName)

    # prints header row from file in first argument with added "filename" category
    def printHeader(self, argv):
        with open(argv[1], 'r') as file:
            line = file.readline()
            self.printLine(line, ',"filename"')

    # prints line with appended value
    def printLine(self, line, value):
        if line != '':
            print(line[:-1] + value + line[-1:], end = '')

    # executes combineFiles method with command line arguments
    def main(self):
        self.combineFiles(sys.argv)

    
if __name__ == '__main__':
    Combiner().main()