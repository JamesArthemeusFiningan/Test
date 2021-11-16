__author__ = "Jason Oesch"
__version__ = "0.1.0"
__license__ = "MIT"

from datetime import datetime

def main():
    start = 1
    end = 100
    reslst = []
    stime = datetime.now()
    for start in range(end):
        test = 1
        for test in range(end):
            if test == start:
                continue
            if test**start == start**test:
                reslst.append(str(f'{start},{test}'))
            test += 1
        start += 1
    etime = datetime.now()
    print(reslst)
    print(etime - stime)


if __name__ == "__main__":
    main()