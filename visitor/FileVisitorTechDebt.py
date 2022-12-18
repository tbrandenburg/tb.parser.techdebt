import json

from FileVisitor import *

class FileVisitorTechDebt(FileVisitor):

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        if not isDir:
            with open(absFilePath, 'r') as f:
                techdebts = json.load(f)
                for techdebt in techdebts:
                    print("[TECHDEBT] " + techdebt["brief"])
                return {"techdebts":techdebts}
        return dict()