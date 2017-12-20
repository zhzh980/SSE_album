import time,threading

def loop():
    print("thread {} is running...".format(threading.current_thread().name))
    n = 0
    while n<5:
        n = n+1
        print("thread {}>>> {}".format(threading.current_thread().name,n))
        time.sleep(1)
    print("thread{} is ended".format(threading.current_thread().name))
t1 = threading.Thread(target=loop,name="LoopThread1")
t2 = threading.Thread(target=loop,name="LoopTHread2")
t1.start()
t2.start()

