#!/usr/bin/env python3
import os
import subprocess
from multiprocessing import Pool

src = './data/prod/'
dest = './data/prod_backup/'


def run(dirname):
    subprocess.call(["rsync", "-arq", src + dirname, dest])


if __name__ == "__main__":
    for root, dirs, files in os.walk(src):
        if len(dirs) > 0:
            break
        #     for file in files:
        #         print(os.path.join(root, file))
        # # print("*"*10)
        # print(dirs)

    p = Pool(len(dirs))
    p.map(run, dirs)
