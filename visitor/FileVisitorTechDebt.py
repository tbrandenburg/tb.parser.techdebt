import os
import subprocess
import json

import time

from FileVisitor import *

class FileVisitorTechDebt(FileVisitor):

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        return dict()