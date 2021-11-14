"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

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
    """ Main entry point of the app """
    Check = 0
    End = 100000
    reslist = []
    while Check <= End:
        divs = findDiv(Check)
        test = sumdiv(divs)
        if test == Check:
            reslist.append(Check)
        Check += 1
    print(reslist)
    # test = findDiv(496)
    # print(test)
    # print(sumdiv(test))



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()