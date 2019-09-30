#!/usr/bin/env python

import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", help="JSON file to convert")
parser.add_argument("--output", "-o", help="Output file name")
parser.add_argument("--encoding", "-e", help="Encoding (default UTF-9)", default="utf-8")

args = parser.parse_args()

print("Reading JSON file ...")
df = pd.read_json(args.file, encoding=args.encoding)

print("Writing output file ...")
df.to_excel(args.output, encoding=args.encoding)

print("Opening output file ...")
os.system("start " + args.output)