import re
import sys
from itertools import groupby

if __name__ == "__main__":
    li=[]
    with open("txtfile.txt",encoding="utf8") as infile:
        yourResult = [line.split(' ') for line in infile.readlines()]
        
        for word in yourResult:
            string = word
            res = [len(list(j)) for _, j in groupby(string)]
            print("The Consecutive characters  : ",str(res))
            