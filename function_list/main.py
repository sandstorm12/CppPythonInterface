import time
import module


def generate_list():
    list_length = int(input("Enter length of list: "))
    sample_list = [i for i in range(list_length)]

    return sample_list


def sum(sample_list):
    sum = 0
    for i in range(len(sample_list)):
        sum += sample_list[i]

    return sum


def increment(sample_list):
    for i in range(len(sample_list)):
        sample_list[i] += 1


def max(sample_list):
    max = 0
    for item in sample_list:
        if item > max:
            max = item

    return max


def benchmark_sum(dictionary):
    start = time.time()
    return_value = module.sum(dictionary)
    end = time.time()
    print(f"Sum time cpp: {end - start:.6f}")

    start = time.time()
    return_value = sum(dictionary)
    end = time.time()
    print(f"Sum time python: {end - start:.6f}")


def benchmark_increment(dictionary):
    start = time.time()
    module.increment(dictionary)
    end = time.time()
    print(f"Increment time cpp: {end - start:.6f}")

    start = time.time()
    increment(dictionary)
    end = time.time()
    print(f"Increment time python: {end - start:.6f}")


def benchmark_max(dictionary):
    start = time.time()
    return_value = module.max(dictionary)
    end = time.time()
    print(f"Max time cpp: {end - start:.6f}")

    start = time.time()
    return_value = max(dictionary)
    end = time.time()
    print(f"Max time python: {end - start:.6f}")


def run():
    sample_list = generate_list()

    benchmark_max(sample_list)
    benchmark_increment(sample_list)
    benchmark_sum(sample_list)


if __name__ == "__main__":
    run()
