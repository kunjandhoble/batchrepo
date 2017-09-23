from __future__ import print_function
import time
import multiprocessing, sys, logging

def calc_square(numbers):
    time.sleep(1)
    print(multiprocessing.current_process().name)
    for n in numbers:
        print('square ' + str(n*n))


def calc_cube(numbers):
    time.sleep(1)
    print(multiprocessing.current_process().name)
    for n in numbers:
        print('cube ' + str(n*n*n))


# demonstrate different memory usage
lst =[]
def var_calc_square(numbers):
    global lst
    print(multiprocessing.current_process().name)
    for n in numbers:
        print('square ' + str(n*n))
        lst.append(n*n)

    print ("Within process: {}".format(lst))


# terminating process
def slow_worker():
    print('Starting worker')
    time.sleep(0.1)
    print('Finished worker')

# logging with multiproc
def worker():
    print('Doing some work')
    sys.stdout.flush()


if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    p3 = multiprocessing.Process(target=var_calc_square, args=(arr,))

    p1.start()
    p2.start()
    p3.start()



    p1.join()
    p2.join()
    p3.join()

    print("Done!")
    print(lst)

    #logging
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()

