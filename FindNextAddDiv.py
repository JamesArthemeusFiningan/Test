__author__ = "Jason Oesch"
__version__ = "0.1.0"
__license__ = "MIT"

from datetime import datetime


def findDiv(num):

    x = 1
    retlist = []
    while (x<num):
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
    # Check = 0
    # End = 1000
    # reslist = []
    # start = datetime.now()
    # while Check <= End:
    #     divs = findDiv(Check)
    #     test = sumdiv(divs)
    #     if test >= Check:
    #         reslist.append(Check)
    #     Check += 1
    #     if Check % (End/100) == 0:
    #         print(f'{(Check/End)*100} %')
    #         end2 = datetime.now()
    #         print(end2 - start)
    # end = datetime.now()
    # print(reslist)
    # print (end -start)
    # x = 0
    # mult = 2
    #
    #
    # reslst = []
    # stage = 1
    # while x < 100:
    #     addls = [1]
    #     set = 2
    #     i = 1
    #     while i <= stage:
    #         addls.append(set)
    #         set = set*mult
    #         i += 1
    #     # while
    #     print(addls)
    #     x+=1
    # print(reslst)
    print(sum(findDiv(8589869056)))




if __name__ == "__main__":
    main()