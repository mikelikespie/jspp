import sys
import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        help="input file [default = stdin]",
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        help="output file [default = stdout]",
                        default=sys.stdout)

    args = parser.parse_args()
    json.dump(json.load(args.infile), args.outfile, indent=2)
