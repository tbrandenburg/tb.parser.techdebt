import json

from FileVisitor import *

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class FileVisitorTechDebt(FileVisitor):
    __colored = True
    __format = "gcc"
    
    def __init__(self,colored,format):
        self.__colored = colored
        self.__format = format

    def __colorize(self, severity, text) -> str:
        if self.__colored:
            if str(severity).lower() == "error":
                return colors.ERROR + text + colors.ENDC
            elif str(severity).lower() == "info":
                return colors.OKBLUE + text + colors.ENDC
            else:
                # defaults to yellow/warning
                return colors.WARNING + text + colors.ENDC
        else:
            return text

    def __gcc(self, techdebt) -> str:
        return techdebt["file"] + ":" + str(techdebt["line"]) + ":" + str(techdebt["column"]) + ": " + self.__colorize(techdebt["severity"], techdebt["severity"]) + ": " + techdebt["brief"] + " [" + self.__colorize(techdebt["severity"], str(techdebt["category"]).upper()) + "]"

    def __tdr(self, techdebt) -> str:
        return "[" + self.__colorize(techdebt["severity"], str(techdebt["severity"]).upper()) + "][" + self.__colorize(techdebt["severity"], str(techdebt["category"]).upper()) + "] " + techdebt["brief"] + ", File: "  + techdebt["file"] + ", Line: "  + str(techdebt["line"]) + ", Column: "  + str(techdebt["column"])

    def __preparePrint(self, techdebt):
        if "id" not in techdebt:
            techdebt["id"] = ""
        if "brief" not in techdebt:
            techdebt["brief"] = "Undefined"
        if "author" not in techdebt:
            techdebt["author"] = ""
        if "date" not in techdebt:
            techdebt["date"] = ""
        if "description" not in techdebt:
            techdebt["description"] = ""
        if "owner" not in techdebt:
            techdebt["owner"] = ""
        if "category" not in techdebt:
            techdebt["category"] = "techdebt"
        if "severity" not in techdebt:
            techdebt["severity"] = "warning"
        if "priority" not in techdebt:
            techdebt["priority"] = ""
        if "file" not in techdebt:
            techdebt["file"] = "."
        if "line" not in techdebt:
            techdebt["line"] = 0
        if "column" not in techdebt:
            techdebt["column"] = 0
        if "votes" not in techdebt:
            techdebt["votes"] = 1
        if "workitem" not in techdebt:
            techdebt["workitem"] = ""
        if "cost" not in techdebt:
            techdebt["cost"] = ""
        if "effort" not in techdebt:
            techdebt["effort"] = ""
        if "impedes" not in techdebt:
            techdebt["impedes"] = ""
        if "discussion" not in techdebt:
            techdebt["discussion"] = []
        if "tags" not in techdebt:
            techdebt["tags"] = []
        return techdebt

    def __print(self, techdebt):
        techdebt = self.__preparePrint(techdebt)
        if self.__format == "tdr":
            print(self.__tdr(techdebt))
        else:
            # defaults to gcc format
            print(self.__gcc(techdebt))


    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        if not isDir:
            with open(absFilePath, 'r') as f:
                techdebt = json.load(f)
                try:
                    self.__print(techdebt)
                    return {"techdebt":techdebt}
                except Exception as e:
                    print("[TDR] Error loading: " + relFilePath + " (" + str(e) + ")")
                    return {}
        return dict()