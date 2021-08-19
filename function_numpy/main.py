import time
import module
import numpy as np

def mean(numpy_array):
    mean_value = numpy_array.mean()

    return mean_value


def get_input():
    size = int(input("Enter the length of numpy array: "))

    numpy_array = np.ones((size, size))

    return numpy_array


def benchmark_cpp(numpy_array):
    start = time.time()
    mean_value = module.mean(numpy_array)
    end = time.time()
    print("C++ time:", end - start)


def benchmark_python(numpy_array):
    start = time.time()
    mean_value = mean(numpy_array)
    end = time.time()
    print("Python time:", end - start)


def run():
    numpy_array = get_input()

    benchmark_cpp(numpy_array)
    benchmark_python(numpy_array)

if __name__ == "__main__":
    run()
