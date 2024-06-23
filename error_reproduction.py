#!/usr/bin/env python3
# Reproduce the error that prevents the usage string to be coloured if a metavar spans within two lines.

import argparse
from rich_argparse import RichHelpFormatter
import sys

# Create the format class
class SmallWidthFormmater(RichHelpFormatter):
    """
    Class to format argparse Help and Description using the raw help and description classes from rich_argparse
    """
    def __init__(self, prog):
        super().__init__(prog, width=4)

# Create the argument parser with built-in RichHelpFormatter
wideparser = argparse.ArgumentParser(formatter_class=RichHelpFormatter)
# Add smaller parser with smaller width
smallwidthparser = argparse.ArgumentParser(formatter_class=SmallWidthFormmater)

for parser in [wideparser, smallwidthparser]:
    # Add mutually exclusive group
    meg = parser.add_mutually_exclusive_group()
    # Add arguments to mutually exclusive group
    meg.add_argument(
        "--option1",
        metavar="metavar1",
        nargs="*",
    )
    meg.add_argument(
        "--option3",
        nargs=5,
    )
print("\n*** WIDE WINDOW - NO ERROR ***\n(All usage string coloured)\n")
wideparser.print_usage()
print("\n*** SMALL WINDOW - ERROR ***\n(No color for usage after prog name. Option/metavar span within multiple lines) ***\n")
smallwidthparser.print_usage()
