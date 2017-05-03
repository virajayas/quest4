import queue
import timeit
if __name__=="__main__":
    lol=queue.Queue()
    lol.put(453)
    print(lol.empty())
    print(lol.get())
    print(lol.empty())
    print(16%5)


def funtion(array, i):
    array[i]=65
    return 1


if __name__=="__fdmain__":
    time=timeit.Timer()
    list=[0]*50000
    print(time.timer())
    for i in range(len(list)):
        funtion(list, i)
    print(list)
    print(time.timer())

    blah=time.timer()
    for i in range(len(list)):
        funtion(list[i:], 0)
    print(list)
    print(time.timer()-blah)