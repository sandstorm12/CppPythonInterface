import time
import module


def generate_dictionary():
    dictionary_length = int(input("Enter length of dictionary: "))
    dictionary = {}
    for i in range(dictionary_length):
        dictionary[i] = i

    return dictionary


def sum(dictionary):
    sum = 0
    for key in dictionary.keys():
        sum += dictionary[key]

    return sum


def increment(dictionary):
    for key in dictionary.keys():
        dictionary[key] += 1


def max(dictionary):
    max = 0
    for key in dictionary.keys():
        if dictionary[key] > max:
            max = dictionary[key]

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
    dictionary = generate_dictionary()

    benchmark_max(dictionary)
    benchmark_increment(dictionary)
    benchmark_sum(dictionary)


if __name__ == "__main__":
    run()
