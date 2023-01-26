
import os
import sys
import argparse
import pprint

import sys
sys.path.insert(0, './visitor')
sys.path.insert(0, './external/file/')
sys.path.insert(0, './external/file/visitor')
sys.path.insert(0, './external/file/filter')

from FileVisitorTechDebt import *
from FileVisitorFileSize import *
from FileVisitorPrintFileCount import *
from FileVisitorPrintFilepaths import *
from FileFilterFile import *
from FileFilterDir import *
from FileTree import *

def main():
    parser = argparse.ArgumentParser(
        prog='tdr_list',
        description='Technical Debt Record Tool - Create new technical debt')
    parser.add_argument("--path", "-p", help="Root path (relative)", type=str, default=".")
    parser.add_argument('--color', "-c", help="Coloured output", action='store_true')
    parser.add_argument("--no-color", "-nc", help="No coloured output",dest='color', action='store_false')
    parser.add_argument("--format", "-f", help="Format of output (tdr, gcc)", type=str, default="gcc")
    parser.set_defaults(color=True)

    args = parser.parse_args()

    files = FileTree(args.path, [FileFilterDir([".*"]),
                                 FileFilterFile([".*\.tdr"])],
                     [FileVisitorTechDebt(args.color, args.format)])

    return 0


if __name__ == '__main__':
    sys.exit(main())
