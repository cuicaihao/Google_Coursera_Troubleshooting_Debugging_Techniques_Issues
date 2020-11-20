# Google Coursera: Troubleshooting and Debugging Techniques

## Qwiklabs Assessment in Week 2:

## Results Comparison and Issues with "rsync"

I got passed on the Qwikilabs Assessment of week2 with the following code [dailysync2.py](dailysync2.py) and my local simulation. but this one only copies files by folders.

![dailysync2.py](image/1_dailysync.png)

But you can see the code missed the c1.txt and c2.txt in the root.

Then I change the code to [dailysync.py](dailysync.py)to fix that as below, which works totally fine on my MacOS(11.0.1 Big Sur).

![dailysync.py](image/2_dailysync.png)

But it raised errors in the Linux environment.
