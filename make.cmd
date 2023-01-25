@echo off
pyinstaller --onefile --hidden-import json tdr_new.py
pyinstaller --onefile --hidden-import json --paths external/file/ --paths external/file/filter/ --paths external/file/visitor/ --paths visitor/ tdr_list.py