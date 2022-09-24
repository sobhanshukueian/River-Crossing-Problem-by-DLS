import time

from Problem import Problem
from State import START_STATE

def main():
    Problem(START_STATE, 70).serach()
    
if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)