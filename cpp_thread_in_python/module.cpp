#include <thread>
#include <atomic>
#include <csignal>
#include <iostream>
#include <unistd.h>
#include <pybind11/pybind11.h>


sig_atomic_t interrupted = 0;
std::atomic<int> thread_counter(0);


void interrupt_handler(int signal) {
    interrupted = 1;
}


void set_signal_handler() {
    static bool handler_set = false;
    if (!handler_set) {
        signal(SIGINT, interrupt_handler);
    }
    handler_set = true;
}


void print(const std::string &name, int count) {
    for (int i = 0; i < count; i++) {
        if (interrupted == 1) {
            break;
        }

        std::cout << "Thread: " << name << " --> " << i << std::endl;
        usleep(1000000);
    }
    
    thread_counter--;
}


void run(const std::string &thread_name, int count) {
    set_signal_handler();

    std::thread(print, thread_name, count).detach();
    thread_counter++;
}


void wait_on_threads() {
    while (true) {
        if (thread_counter == 0) {
            break;
        } else {
            usleep(500000);
        }
    }
}


PYBIND11_MODULE(module, m)
{
    m.def(
        "run", &run
    );
    m.def(
        "wait_on_threads", &wait_on_threads
    );
}
