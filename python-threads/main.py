from threading import Thread
from time import sleep

started = False

def threaded_function(arg):
    for i in range(arg):
        print i,started
        sleep(1)

if __name__ == "__main__":
    started = True
    thread = Thread(target = threaded_function, args = (5, ))
    thread.start()
    sleep(2)
    started = False
    thread.join()
    print "thread finished...exiting"

