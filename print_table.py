import argparse
from pyscripts.table import get_table_string, parse_csv_lines

parser = argparse.ArgumentParser(description='Make an ASCII table.')
parser.add_argument('--csvfile', type=str, default=None, help='The csv file path')
parser.add_argument('--content', type=str, default=None, help='The content of csv file')
parser.add_argument('--splitter', type=str, default = ",", help='The column splitter')
parser.add_argument('--cell_splitter', type=str, default = "|", help='The column splitter in table')
parser.add_argument('--table_line', type=str, default = "-", help='The line in table')
parser.add_argument('--line_splitter', type=str, default = "+", help='The line in table')
parser.add_argument('--padding', type=str, default = " ", help='The left/right padding inside a cell')
args = parser.parse_args()

assert(len(args.cell_splitter) == len(args.line_splitter))
assert(len(args.table_line) == 1)
assert(len(args.table_line) == len(args.padding))

def get_contentlines(csvfile=None, content=None):
    if not csvfile == None:
        assert(content == None)
        content = open(csvfile, "r", encoding="utf-8").read()
    if content == None:
        print("No content to build table. Please set `--csvfile` or `--content`")
    lines = content.split("\n")
    assert(len(lines) >= 2)
    return lines

print(get_table_string(
        parse_csv_lines(get_contentlines(args.csvfile, args.content), args.splitter),
        table_line = args.table_line,
        padding = args.padding,
        line_splitter = args.line_splitter,
        cell_splitter = args.cell_splitter))