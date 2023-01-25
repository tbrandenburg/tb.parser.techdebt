@echo off
pyinstaller --onefile --hidden-import json --paths external/file/ --paths external/file/filter/ --paths external/file/visitor/ --paths visitor/ techdebt.py