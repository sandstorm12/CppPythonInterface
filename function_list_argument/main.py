import time
import module


def generate_list():
    list_length = int(input("Enter the length of list: "))

    test_list = [i for i in range(list_length)]

    return test_list


def benchmark_cpp(test_list):
    start = time.time()
    
    returned_list = module.reverse(test_list)
    
    end = time.time()

    print(f"Cpp time: {end - start}")


def benchmark_python(test_list):
    start = time.time()
    
    test_list.reverse()
    
    end = time.time()

    print(f"Python time: {end - start}")


def run():
    test_list = generate_list()

    benchmark_cpp(test_list)

    benchmark_python(test_list)


if __name__ == "__main__":
    run()
