import time
import module


def get_input():
    number_calls = int(input("Enter number of calls: "))

    return number_calls


def print_hello_world():
    print("Hello World")


def print_hello_world_repeat(count):
    for i in range(count):
        print("Hello World")


def benchmark_cpp(number_calls):
    start = time.time()
    for i in range(number_calls):
        module.print_hello_world()
    end = time.time()
    print(f"Time cpp {end - start:.6f}")


def benchmark_python(number_calls):
    start = time.time()
    for i in range(number_calls):
        print_hello_world()
    end = time.time()
    print(f"Time python {end - start:.6f}")


def benchmark_cpp_repeat(number_calls):
    start = time.time()
    module.print_hello_world_repeat(number_calls)
    end = time.time()
    print(f"Time repeat cpp {end - start:.6f}")


def benchmark_python_repeat(number_calls):
    start = time.time()
    print_hello_world_repeat(number_calls)
    end = time.time()
    print(f"Time repeat python {end - start:.6f}")


def run():
    number_calls = get_input()

    benchmark_cpp(number_calls)
    benchmark_python(number_calls)
    benchmark_cpp_repeat(number_calls)
    benchmark_python_repeat(number_calls)


if __name__ == "__main__":
    run()
