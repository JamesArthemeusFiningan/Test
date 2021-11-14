__author__ = "Jason Oesch"
__version__ = "0.1.0"
__license__ = "MIT"

from datetime import datetime


def findDiv(num):

    x = 1
    retlist = []
    while (x<num/4):
        if num%x == 0:
            if x not in retlist:
                retlist.append(x)
            if x != 1 and (num/x) not in retlist:
                retlist.append(int(num/x))
        x += 1
    return retlist

def sumdiv (divlist):
    total = 0
    for div in divlist:
        total = total + div
    return total

def main():
    Check = 0
    End = 100000
    reslist = []
    start = datetime.now()
    while Check <= End:
        divs = findDiv(Check)
        test = sumdiv(divs)
        if test == Check:
            reslist.append(Check)
        Check += 1
    end = datetime.now()
    print(reslist)
    print (end -start)





if __name__ == "__main__":
    main()