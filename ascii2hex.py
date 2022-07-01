import argparse
from pyscripts.ascii import get_hex_table_from_ascii_string
from pyscripts.table import get_table_string

parser = argparse.ArgumentParser(description='Convert ASCII string to hex in uint64 numbers.')
parser.add_argument('--ascii', "-a", type=str, default=None, help='The ASCII string')
args = parser.parse_args()

print(get_table_string(get_hex_table_from_ascii_string(args.ascii)))