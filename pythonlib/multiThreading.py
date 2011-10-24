import threading,time
_locking = threading.Lock()

def run(func,parameterList,threadingCount):
    '''
    def f1(a,b):
        print a+b

    run(f1,[(a,a*a,) for a in range(10)],30) #30 threadings
    '''
    allT = []
    success=0
    while success < len(parameterList):
        while len(allT) < threadingCount and success < len(parameterList):
            t = threading.Thread(target=func,args=parameterList[success])
            success+=1
            t.setDaemon(1)
            allT += [t]
            t.start()
        time.sleep(0.001)
        allT = [t for t in allT if t.isAlive()]
    for t in allT: t.join()

def lock():
    _locking.acquire()

def unlock():
    _locking.release()

def locked():
    return _locking.locked()
