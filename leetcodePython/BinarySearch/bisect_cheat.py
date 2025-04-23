from bisect import *


if __name__ == '__main__':
    print(bisect_left([1,1], 1))  #0
    print(bisect_right([1,1], 1)) #2

    print(bisect_left([1,1], 0)) #0
    print(bisect_right([1,1], 0)) #0

    print(bisect_left([1,1], 2)) #2
    print(bisect_right([1,1], 2)) #2