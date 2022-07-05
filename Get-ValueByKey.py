import argparse
from pyscripts.find import find_value_by_key_from_text_lines

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--Key", help="The key to be searched from the text file.")
parser.add_argument("-f", "--File", help="The text file to be searched.")
args = parser.parse_args()

def printResult(filepath, key):
    # redirect to file if needed
    print("Search key:", key, "in file:", filepath)
    for r in find_value_by_key_from_text_lines(filepath, key):
        print("\n\t#", r[0])
        print(r[1])

printResult(args.File, args.Key)