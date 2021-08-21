import module


if __name__ == "__main__":
    module.run("thread1", 100)
    module.run("thread2", 100)
    module.run("thread3", 100)
    module.wait_on_threads()
