#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",help="display the square of the number given",type=int)
args = parser.parse_args()
print("The square of {} is {}".format(args.square,args.square**2))

