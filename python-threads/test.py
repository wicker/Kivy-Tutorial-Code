from threading import Thread

def threaded_function():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = Thread(target=threaded_function)
    threads.append(t)
    t.start()
