# PMG Coding Challenge 
My submission for the PMG Graduate Leadership Program Coding Challenge. Looking forward to share my work with the PMG team :)

## Description
For this challenge, I chose to implement my own methods to manipulate the generated CSV files, as they are ultimately plaintext. For larger and more varied files, I would use a library like Pandas and PyArrow, which may be faster.

If I had more time, I would:
  - Add more unit tests for comprehensive code coverage.
  - Create a unified class in *csv_combiner_test.py* to avoid redeclaring shared arguments.
  - Improve the generator by adding more category and item names from a dictionary.
  - Create alternative versions based on Pandas and PyArrow and compare speeds.


## How To Use
To use the CSV Combiner, run the following command in the project's directory:
`./csv_combiner argv1 argv2 ...`

- `argv1` is a relative path to a CSV file
- `argv2` (optional) is a relative path to another CSV file
- `...` (optional) is any number of additional relative paths to CSV files separated by a space

Example: `./csv_combiner ./fixtures/accessories.csv ./fixtures/household_cleaners.csv` 

The program will print the resulting file to standard output (stdout). If you wish to save the output to a file, you may redirect the output to another non-existing or existing file by adding ` > filename`

- `filename` is a relative path to a file where output will be stored

Example: `./csv_combiner ./fixtures/accessories.csv household_cleaners.csv > items.csv`


## Program Structure

### Combiner
The program itself is contained within *csv_combiner.py* as a Combiner class. It can be used with either standard input arguments via the *main()* method or with any predetermined array of arguments via the *combineFiles()* method.

### Generator
The provided *generatefixtures.py* file has been transformed into *csv_generator.py*, which contains a Generator class used in *csv_combiner_test.py* to create CSV files and fill them with semi-random data for testing.

### Tester
The file *csv_combiner_test.py* is a unit test file that aims to automate testing of the program *csv_combiner.py*.



