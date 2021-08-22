import time
import string
import random
import module
import numpy as np


def get_random_string():
    length = int(input("Enter numpy length (length x length): "))

    numpy_array = np.ones((length, length))

    return numpy_array


def print_shape(numpy_array):
    print(numpy_array.shape)


def increment(numpy_array):
    for i in range(numpy_array.shape[0]):
        for j in range(numpy_array.shape[1]):
            numpy_array[i, j] += 1


def increment_numpy(numpy_array):
    numpy_array += 1


def sum(numpy_array):
    sum = 0
    for i in range(numpy_array.shape[0]):
        for j in range(numpy_array.shape[1]):
            sum += numpy_array[i, j]

    return sum


def sum_numpy(numpy_array):
    return np.sum(numpy_array)


def benchmark_print_shape_cpp(numpy_array):
    start = time.time()
    return_value = module.print_shape(numpy_array)
    end = time.time()
    print(f"Time print shape cpp {end - start:.6f}")


def benchmark_print_shape_python(numpy_array):
    start = time.time()
    return_value = print_shape(numpy_array)
    end = time.time()
    print(f"Time print shape python {end - start:.6f}")


def benchmark_increment_cpp(numpy_array):
    start = time.time()
    return_value = module.increment(numpy_array)
    end = time.time()
    print(f"Time increment cpp {end - start:.6f}")


def benchmark_increment_python(numpy_array):
    start = time.time()
    return_value = increment(numpy_array)
    end = time.time()
    print(f"Time increment python {end - start:.6f}")


def benchmark_increment_python_numpy(numpy_array):
    start = time.time()
    return_value = increment_numpy(numpy_array)
    end = time.time()
    print(f"Time increment python numpy {end - start:.6f}")


def benchmark_sum_cpp(numpy_array):
    start = time.time()
    return_value = module.sum(numpy_array)
    end = time.time()
    print(f"Time sum cpp {end - start:.6f}")


def benchmark_sum_python(numpy_array):
    start = time.time()
    return_value = sum(numpy_array)
    end = time.time()
    print(f"Time sum python {end - start:.6f}")


def benchmark_sum_python_numpy(numpy_array):
    start = time.time()
    return_value = sum_numpy(numpy_array)
    end = time.time()
    print(f"Time sum python numpy {end - start:.6f}")


def run():
    numpy_array = get_random_string()

    benchmark_print_shape_cpp(numpy_array)
    benchmark_print_shape_python(numpy_array)
    benchmark_increment_cpp(numpy_array)
    benchmark_increment_python(numpy_array)
    benchmark_increment_python_numpy(numpy_array)
    benchmark_sum_cpp(numpy_array)
    benchmark_sum_python(numpy_array)
    benchmark_sum_python_numpy(numpy_array)


if __name__ == "__main__":
    run()
