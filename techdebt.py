import os
import sys
import argparse
import pprint

import sys
sys.path.insert(0,'./visitor')
sys.path.insert(0,'./external/file/')
sys.path.insert(0,'./external/file/visitor')
sys.path.insert(0,'./external/file/filter')

from FileTree import *
from FileFilterDir import *
from FileFilterFile import *
from FileVisitorPrintFilepaths import *
from FileVisitorPrintFileCount import *
from FileVisitorFileSize import *
from FileVisitorTechDebt import *

def main():
    parser = argparse.ArgumentParser(description='Parse file structure')
    parser.add_argument("--path", "-p", help="Root path (relative)", type=str, default=".")
    parser.add_argument('--color', "-c", help="Coloured output", action='store_true')
    parser.add_argument("--no-color", "-nc", help="No coloured output", dest='color', action='store_false')
    parser.set_defaults(color=True)
  
    args = parser.parse_args()

    files = FileTree(args.path,[FileFilterDir([".*"]),
                                FileFilterFile([".*\.tdr"])],
                               [FileVisitorTechDebt(args.color)])

    files.to_json("build/td_tree.json")

    return 0

if __name__ == '__main__':
    sys.exit(main())

