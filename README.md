# Google Coursera: Troubleshooting and Debugging Techniques

Issue Time: Fri Nov 20 20:31:26 AEDT 2020

## Qwiklabs Assessment in Week 2:

## Results Comparison and Issues with "rsync"

I got passed on the Qwikilabs Assessment of week2 with the following code [dailysync2.py](dailysync2.py) and my local simulation. but this one only copies files by folders.

```bash
# Experimental Records
# Task copy the file from data/prod to data/prod_backup.

# folder directory based backup.
bash-3.2$ ./dailysync2.py
bash-3.2$ tree data/
data/
├── prod
│   ├── A
│   │   ├── a1.txt
│   │   └── a2.txt
│   ├── B
│   │   ├── b1
│   │   └── b2
│   ├── c1.txt
│   └── c2.txt
└── prod_backup
    ├── A
    │   ├── a1.txt
    │   └── a2.txt
    └── B
        ├── b1
        └── b2

6 directories, 10 files

bash-3.2$ rm -rf data/prod_backup/*
bash-3.2$ tree data
data
├── prod
│   ├── A
│   │   ├── a1.txt
│   │   └── a2.txt
│   ├── B
│   │   ├── b1
│   │   └── b2
│   ├── c1.txt
│   └── c2.txt
└── prod_backup

# file based backup
bash-3.2$ ./dailysync.py
./data/prod/c1.txt
./data/prod/c2.txt
./data/prod/A/a1.txt
./data/prod/A/a2.txt
./data/prod/B/b2
./data/prod/B/b1
Total file number is 6
Done
bash-3.2$ tree data/
data/
├── prod
│   ├── A
│   │   ├── a1.txt
│   │   └── a2.txt
│   ├── B
│   │   ├── b1
│   │   └── b2
│   ├── c1.txt
│   └── c2.txt
└── prod_backup
    ├── A
    │   ├── a1.txt
    │   └── a2.txt
    ├── B
    │   ├── b1
    │   └── b2
    ├── c1.txt
    └── c2.txt

6 directories, 12 files
bash-3.2$ date
Fri Nov 20 20:34:56 AEDT 2020
bash-3.2$
```

![dailysync2.py](image/1_dailysync.png)

But you can see the code missed the c1.txt and c2.txt in the root.

Then I change the code to [dailysync.py](dailysync.py)to fix that as below, which works totally fine on my MacOS(11.0.1 Big Sur).

![dailysync.py](image/2_dailysync.png)

But it raised errors in the Linux environment.
