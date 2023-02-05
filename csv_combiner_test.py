#!/usr/bin/env python3

import os.path
import sys
import unittest as unit
from csv_generator import Generator
from csv_combiner import Combiner

class ArgumentTest(unit.TestCase):
    @classmethod # setup class method for arguments
    def setUpClass(cls):
        # create instances of Combiner and Generator
        cls.cmb = Combiner() 
        cls.gen = Generator()
        # generate new set of CSV files
        cls.gen.main() 
        # set paths for combiner and arguments
        cls.combinerPath = './csv_combiner.py'
        cls.argvDirPath = './fixtures/'
        cls.argvNotCSVPath = cls.argvDirPath + 'accessories'
        cls.argvNotExistPath = cls.argvDirPath + 'electronics.csv'

    # reset argv values and generate new set of CSV files
    def setUp(self):
        self.argv = [self.combinerPath]

    @classmethod # teardown class method to remove all generated test files
    def tearDownClass(cls):
        for file in os.scandir(cls.argvDirPath):
            os.remove(file.path)
        os.rmdir(cls.argvDirPath)
    
    # default test (passes every time)
    def test_AlwaysTrue(self):
        assert True == True

    # pass in no arguments
    def test_ArgumentEmpty(self):
        assert self.cmb.combineFiles(self.argv) == False

    # pass in non-CSV argument
    def test_ArgumentNotCSV(self):
        self.argv.append(self.argvNotCSVPath)
        assert self.cmb.combineFiles(self.argv) == False

    # pass in dubious argument
    def test_ArgumentNotExist(self):
        self.argv.append(self.argvNotExistPath)
        assert self.cmb.combineFiles(self.argv) == False


class OutputTest(unit.TestCase):
    @classmethod # setup class method for arguments and expected variables
    def setUpClass(cls):
        # create instances of Combiner and Generator
        cls.cmb = Combiner() 
        cls.gen = Generator()
        # generate new set of CSV files
        cls.gen.main() 
        # set paths for output, combiner, and arguments
        cls.outputPath = './output_test.csv'
        cls.combinerPath = './csv_combiner.py'
        cls.argvDirPath = './fixtures/'
        cls.argvPath1 = cls.argvDirPath + 'household_cleaners.csv'
        cls.argvPath2 = cls.argvDirPath + 'clothing.csv'
        cls.argvPath3 = cls.argvDirPath + 'accessories.csv'
        # calculate argv file sizes for comparison
        cls.argvSize1 = os.path.getsize(cls.argvPath1)
        cls.argvSize2 = os.path.getsize(cls.argvPath2)
        cls.argvSize3 = os.path.getsize(cls.argvPath3)
        cls.argvSize1and2 = cls.argvSize1 + cls.argvSize2
        cls.argvSizeAll = cls.argvSize1and2 + cls.argvSize3 
        # save system stdout to reset once tests are done
        cls.stdoutMain = sys.stdout
    
    # setup method to reset arguments and clean output file
    def setUp(self):
        self.argv = [self.combinerPath]
        self.outputFile = open(self.outputPath, 'w+')
        sys.stdout = self.outputFile
      
    @classmethod # teardown class method to reset stdout and delete test files
    def tearDownClass(cls):
        sys.stdout = cls.stdoutMain
        for file in os.scandir(cls.argvDirPath):
            os.remove(file.path)
        os.rmdir(cls.argvDirPath)
        if os.path.exists(cls.outputPath):
            os.remove(cls.outputPath)

    # teardown method to delete output file between tests
    def tearDown(self):
        if not self.outputFile.closed:
            self.outputFile.close()
        os.remove(self.outputPath)

    # output is bigger than the single argument file that is passed
    def test_CombineOne(self):
        self.argv.append(self.argvPath1)
        self.cmb.combineFiles(self.argv)
        self.outputFile.close()
        assert os.path.getsize(self.outputPath) > os.path.getsize(self.argvPath1)

    # Combine is bigger than one of the arguments when two are passed 
    def test_CombineTwo(self):
        self.argv.append(self.argvPath1)
        self.argv.append(self.argvPath2)
        self.cmb.combineFiles(self.argv)
        self.outputFile.close()
        assert os.path.getsize(self.outputPath) > self.argvSize1and2

    # output is bigger than two of the arguments when three are passed
    def test_CombineThree(self):
        self.argv.append(self.argvPath1)
        self.argv.append(self.argvPath2)
        self.argv.append(self.argvPath3)
        self.cmb.combineFiles(self.argv)
        self.outputFile.close()
        assert os.path.getsize(self.outputPath) > self.argvSizeAll

    # output contains all filenames of arguments passed
    def test_CombineThreeFilename(self):
        self.argv.append(self.argvPath1)
        self.argv.append(self.argvPath2)
        self.argv.append(self.argvPath3)
        self.cmb.combineFiles(self.argv)   
        self.outputFile.close()
        with open(self.outputPath, 'r') as file:
            fileRead = file.read()
        assert(fileRead.find(self.argvPath1.split(os.sep)[-1]) != -1)
        assert(fileRead.find(self.argvPath2.split(os.sep)[-1]) != -1)
        assert(fileRead.find(self.argvPath3.split(os.sep)[-1]) != -1)


if __name__ == "__main__":
    unit.main()