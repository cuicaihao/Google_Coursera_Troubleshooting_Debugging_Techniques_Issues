#!/usr/bin/env python3
import os
import subprocess
from multiprocessing import Pool


def run(task):
  # Do something with task here
    print("Handling {}".format(task))


if __name__ == "__main__":
    tasks = ['task1', 'task2', 'task3']
    # Create a pool of specific number of CPUs
    p = Pool(len(tasks))
    # Start each task within the pool
    p.map(run, tasks)
