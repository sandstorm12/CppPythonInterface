import time
import module

def increment(value):
    for i in value.keys():
        value[i] += 1


def get_input():
    input_value = int(input("Enter the length of simple dict: "))

    input_dict = {}
    for i in range(input_value):
        input_dict[i] = i

    return input_dict


def benchmark_cpp(input_value):
    start = time.time()
    return_value = module.increment(input_value)
    end = time.time()
    print("C++ time:", end - start)


def benchmark_python(input_value):
    start = time.time()
    return_value = increment(input_value)
    end = time.time()
    print("Python time:", end - start)


def run():
    input_value = get_input()

    benchmark_cpp(input_value)
    benchmark_python(input_value)

if __name__ == "__main__":
    run()
