#!/usr/bin/env python3
import os
import subprocess
from multiprocessing import Pool

src = "./data/prod/"
dest = "./data/prod_backup/"


def run(source):
    destination = source.replace(src, dest)
    subprocess.call(["rsync", "-arq", source, destination])


def getfilelist(src):
    filelist = []
    for root, dirs, files in os.walk(src):
        for file in files:
            filepath = os.path.join(root, file)
            filelist.append(filepath)
            print(filepath)
    return filelist


if __name__ == "__main__":
    filelist = list(getfilelist(src))
    print("Total file number is {}".format(len(filelist)))
    p = Pool(len(filelist))
    p.map(run, filelist)
    print("Done")
