#sharing memory between processes using Array and Value
import multiprocessing
import ctypes

def calc_square(numbers, result, v, str_result, str_Value):
    v.value = 3.9
    for idx, n in enumerate(numbers):
        result[idx] = n*n
        str_Value[idx] = 's'
        str_result[idx] = 'asd'

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)
    str_Value = multiprocessing.Array('c', 3)
    str_result = multiprocessing.Array(ctypes.c_char_p, 3)
    v = multiprocessing.Value('d', 0.0)

    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v,str_result, str_Value))

    p.start()
    p.join()

    print(result[:])
    print(v.value)
    print(str_result[:])
    print(str_Value[:])
