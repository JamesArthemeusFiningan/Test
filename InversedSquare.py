__author__ = "Jason Oesch"
__version__ = "0.1.0"
__license__ = "MIT"

from datetime import datetime

def main():
    start = 1
    end = 500
    reslst=[]
    stime=datetime.now()
    for start in range(end):
        i = 1
        for i in range(end):
            reslst.append(start**i)
            i+=1
        start+=1
    etime=datetime.now()
    print(reslst)
    print(etime-stime)

if __name__ == "__main__":
    main()