import threading as th
import time as t

total = 4

def createP1 ():
    global total
    for i in range(10):
        t.sleep(2)
        print('Added Item @ sleep == 2')
        total +=1
    print("all created")

def createP2 ():
    global total
    for i in range(7):
        t.sleep(1)
        print("Added Item @ sleep == 1")
        total +=1
    print("all created")

def totalLimitChecker():
    global total
    total_limit = 5
    switch = True
    while switch:
        if total > total_limit:
            print("exceed total limit {}".format(total_limit))
            total -= 3
            print("substracted 3")
        else:
            t.sleep(1)
            print("waiting ...")

def main():
    create_thread_1 = th.Thread(target=createP1,name="createP1")
    create_thread_2 = th.Thread(target=createP2,name="createP2")
    limit_checker = th.Thread(target=totalLimitChecker,name="limit checker"\
    ,daemon=True)
    create_thread_1.start(); create_thread_2.start(); limit_checker.start();
    
    create_thread_1.join(); create_thread_2.join(); #limit_checker.join()
    print("total ends at -> {}".format(total))

if __name__ == "__main__":
    main()