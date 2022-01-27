import platform
import multiprocessing
import psutil
import socket
import timeit

def showinfo(tip, info):
    print("{}: {}".format(tip, info))


def main():
    showinfo("Name of machine",platform.node())
    showinfo("operating system name",platform.system())
    showinfo("operating system version",platform.version())
    showinfo("CPU numbers", multiprocessing.cpu_count())
    showinfo("Memory size",psutil.virtual_memory().total)
    showinfo("IP address", socket.gethostbyname("localhost"))
    showinfo("Time needed to a simple calculation", timeit.timeit("result = 2**11 + 123"))

if __name__ == "__main__":
    main()
