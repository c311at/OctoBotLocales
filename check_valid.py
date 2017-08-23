import json
import os
def check_json(path=""):
    path = os.path.normpath(path)
    print(" " * (len(os.path.split(path))-1),"Folder:", path, sep="")
    folders = []
    for item in os.listdir(path):
        npath = os.path.normpath(os.path.join(path, item))
        if item.endswith(".json"):
            beautiful_path = " " * len(os.path.split(npath)) + npath
            try:
                with open(npath) as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                print(beautiful_path, "FAIL on %s, %s" % (e.lineno, e.colno))
            else:
                print(beautiful_path, "is valid")
        elif os.path.isdir(npath):
            folders.append(npath)
    for folder in folders:
        check_json(folder)

print("Checking json files for validness")
check_json()
