import time
import module


def get_input():
    count_length = int(input("Enter count length: "))

    return count_length


def count(count_length):
    counter = 1
    for i in range(count_length):
        counter += counter

    return counter


def benchmark_length_cpp(count_length):
    start = time.time()
    return_value = module.count(count_length)
    end = time.time()
    print(f"Time cpp {end - start:.6f}")


def benchmark_length_python(count_length):
    start = time.time()
    return_value = count(count_length)
    end = time.time()
    print(f"Time python {end - start:.6f}")


def run():
    count_length = get_input()

    benchmark_length_cpp(count_length)
    benchmark_length_python(count_length)


if __name__ == "__main__":
    run()
