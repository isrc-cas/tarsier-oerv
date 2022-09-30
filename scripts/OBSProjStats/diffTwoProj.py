import requests
from bs4 import BeautifulSoup
import csv
from config import *

def getPkgList():

def read():
    _json = {}
    for i in projRepoUrl:
        html = requests.get(projRepoUrl[i]).text
        b = BeautifulSoup(html, "html.parser").table.tbody
        _arch = dict(eval(b["data-tableinfo"]))[i]
        _json += {i: eval(b["data-statushash"])[i][_arch]}
    return _json

def main():
    plist=[]
    for i in queryUrl.keys():
        plist.append(read(queryUrl[i]))
        pass

    with open(csvName, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["", oldVer, newVer])
        for i in a2:
            writer.writerow([i, "success", "failed"])
        for i in a1:
            writer.writerow([i, "failed", "failed"])


if __name__ == '__main__':
    main()
