import time
import string
import random
import module


def get_random_string():
    string_length = int(input("Enter string length: "))

    random_string = ''.join(
        random.choices(
            string.ascii_lowercase +
                string.ascii_uppercase +
                string.digits +
                string.punctuation,
            k=string_length
        )
    )

    return random_string


def reverse_string(sample_string):
    reversed_string = sample_string[::-1]

    return reversed_string


def count_digits(random_string):
    count = sum(c.isdigit() for c in random_string)

    return count


def benchmark_reverse_cpp(random_string):
    start = time.time()
    return_value = module.reverse_string(random_string)
    end = time.time()
    print(f"Time reverse cpp {end - start:.6f}")


def benchmark_reverse_python(random_string):
    start = time.time()
    return_value = reverse_string(random_string)
    end = time.time()
    print(f"Time reverse python {end - start:.6f}")


def benchmark_count_digits_cpp(random_string):
    start = time.time()
    return_value = module.count_digits(random_string)
    end = time.time()
    print(f"Time count digits cpp {end - start:.6f}")


def benchmark_count_digits_python(random_string):
    start = time.time()
    return_value = count_digits(random_string)
    end = time.time()
    print(f"Time count digits python {end - start:.6f}")


def run():
    random_string = get_random_string()

    benchmark_reverse_cpp(random_string)
    benchmark_reverse_python(random_string)
    benchmark_count_digits_cpp(random_string)
    benchmark_count_digits_python(random_string)


if __name__ == "__main__":
    run()
