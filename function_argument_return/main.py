import time
import module

def count(value):
    output_value = 0
    for i in range(value):
        output_value += 1

    return output_value


def get_input():
    input_value = int(input("Enter a number to count: "))

    return input_value


def benchmark_cpp(input_value):
    start = time.time()
    return_value = module.count(input_value)
    end = time.time()
    print("C time:", end - start)


def benchmark_python(input_value):
    start = time.time()
    return_value = count(input_value)
    end = time.time()
    print("Python time:", end - start)


def run():
    input_value = get_input()

    benchmark_cpp(input_value)
    benchmark_python(input_value)

if __name__ == "__main__":
    run()
