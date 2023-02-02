# input.py
import time
"""
A module that makes testcase input simillar to Online Judge
"""

def testcase(func):
    def wrapper(*args, **kargs):
        start = time.time()
        with open('../input.txt','rt') as f:
            func(testcase = f)
        end = time.time()

        print(f'\n걸린 시간: {end - start:.6f}sec')

    return wrapper