#! /usr/bin/python3

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import sys
import os
import matplotlib as mpl

MAX_SIZE  = 1500000
DIV       = 750000

mpl.rcParams['agg.path.chunksize'] = 100000000000

def to2d(f, size, n, fsize):
    x = []
    y = []
    for i in range(size // 2):
        if (f.tell() < fsize - 1):
            tmp, byte = f.read(2)
            f.seek(n, os.SEEK_CUR)
            x.append(tmp)
            y.append(byte)
    return x, y

def to3d(f, size, n, fsize):
    x = []
    y = []
    z = []
    for i in range(size // 3):
        if (f.tell() < fsize - 2):
            tmp_0, tmp_1, byte = f.read(3)
            f.seek(n, os.SEEK_CUR)
            x.append(tmp_0)
            y.append(tmp_1)
            z.append(byte)
    return x, y, z

def usage():
    print(sys.argv[0] + "file_name {2d|3d}")

def sampleSize(fsize):
    if (fsize > MAX_SIZE):
        n = fsize // DIV
        size = fsize // n
    else:
        n = 0
        size = fsize
    return n, size
    
def main():
    if (len(sys.argv) != 3 or sys.argv[2] not in ("2d", "3d")):
        usage()
        exit(-1)

    f = open(sys.argv[1], "rb")
    fsize = os.path.getsize(sys.argv[1])
    n, size = sampleSize(fsize)

    print("fsize: " + str(fsize))
    print("n: " + str(n))


    if (sys.argv[2] == "2d"):
        x, y = to2d(f, size, n, fsize)
        ax = plt.axes()
        ax.set_facecolor('black')
        ax.plot(x, y, 'w.', markersize=.5, linestyle="None")
        ax.set_title('2D Visualization ' + sys.argv[1], {'color':"w"})
    elif (sys.argv[2] == "3d"):
        x, y, z = to3d(f, size, n, fsize)
        ax = plt.axes(projection ='3d')
        ax.set_facecolor('black')
        ax.plot(x, y, z, 'w.', markersize=.1, linestyle="None")
        ax.axis("off")
        ax.set_title('3D Visualization: ' + sys.argv[1], {'color':"w"})
        
    plt.show()

if __name__ == "__main__":
    main()
