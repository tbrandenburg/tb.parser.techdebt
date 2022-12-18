import json

from FileVisitor import *

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class FileVisitorTechDebt(FileVisitor):

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        if not isDir:
            with open(absFilePath, 'r') as f:
                techdebts = json.load(f)
                for techdebt in techdebts:
                    print("[" + colors.WARNING + "TECHDEBT" + colors.ENDC + "] " + techdebt["brief"])
                return {"techdebts":techdebts}
        return dict()