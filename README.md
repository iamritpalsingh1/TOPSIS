#TOPSIS
Introduction:
TOPSIS is a Python package that provides a simple and effective way to perform the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) analysis on a given dataset. This package is particularly useful in decision-making problems where multiple criteria are involved, and the goal is to select the best alternative among a set of available options.

##Installation:
You can install Topic-TOPSIS using pip, by running the following command:

'''pip install TOPSIS-AMRIT-102003690'''

##Usage:
TOPSIS can be used from the command line, by providing the input data file, weights, impacts, and the name of the result file. Here is an example command:

'''python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>'''

where:

<program.py> is the name of the Python program file (in this case, 101556.py)
<InputDataFile> is the name of the CSV file containing the input data
<Weights> is a comma-separated list of weights for each criterion, e.g., “1,1,1,2”
<Impacts> is a comma-separated list of impacts for each criterion, e.g., “+,+,-,+”
<ResultFileName> is the name of the CSV file where the result will be saved (in this case, 101556-result.csv)

##Example:

Here is an example command using the provided example data:

'''python 101556.py 101556-data.csv “1,1,1,2” “+,+,-,+” 101556-result.csv'''

This will perform the TOPSIS analysis on the data in the file 101556-data.csv, using the weights and impacts specified, and save the result in the file 101556-result.csv.


##Contributing:

We welcome contributions to Topic-TOPSIS! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request on the GitHub repository: https://github.com/iamritpalsingh/TOPSIS

##License:

TOPSIS is released under the MIT License. See the LICENSE file for details.