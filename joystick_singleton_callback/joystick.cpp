#include <thread>
#include <fcntl.h>
#include <stdint.h>
#include <dirent.h>
#include <iostream>
#include <pybind11/pybind11.h>
#include <pybind11/functional.h>


class JoystickEvent {
    private:
        friend class Joystick;

        struct js_event {
            uint32_t time;      // Event timestamp in milliseconds
            int16_t value;      // Value
            uint8_t type;       // Event type
            uint8_t number;     // Axis/button number
        };

        struct js_event _event;

        JoystickEvent(js_event &event) {
            _event = event;
        }
    
    public:
        int get_timestamp() {
            return _event.time;
        }

        int get_value() {
            return _event.value;
        }

        int get_type() {
            return _event.type;
        }

        int get_number() {
            return _event.number;
        }
};


class Joystick {
    private:
        friend class JoystickController;
        
        std::string _file_descriptor;
        pybind11::list _listeners;
        std::thread *_thread;

        static void event_handler(std::string file_descriptor,
                pybind11::list listeners) {

            int file = open(file_descriptor.c_str(), O_RDONLY);
            while (true) {
                JoystickEvent::js_event event;
                ssize_t read_size = read(file, &event, sizeof(event));
                if (read_size != sizeof(event)) {
                    std::cout << "Cannot read fully" << std::endl;
                    return;
                    // There is a problem but how to handler it?
                }

                pybind11::gil_scoped_acquire acquire;
                for (auto listener : listeners) {
                    JoystickEvent joystick_event(event);
                    listener(joystick_event);
                }
                pybind11::gil_scoped_release release;
            }
        }
        
        Joystick(std::string file_descriptor) {
            _file_descriptor = file_descriptor;
        }

    public:
        void set_on_event(
                const std::function<void(JoystickEvent)> &on_event) {
            _listeners.append(on_event);
            _thread = new std::thread(
                event_handler, _file_descriptor, _listeners
            );
        }

        bool is_running() {
            return _thread->joinable();
        }
};


class JoystickController {
    private:
        static JoystickController _instance;
    
    public:
        const static JoystickController get_instance() {
            return JoystickController::_instance;
        }

        pybind11::list get_joysticks(
                std::string search_directory="/dev/input/") {
            pybind11::list joysticks;
            struct dirent *file;
            DIR *directory = opendir(search_directory.c_str());

            if (directory != NULL) {
                while ((file = readdir(directory)) != NULL) {
                    std::string file_name = std::string(file->d_name);
                    if (file_name.find("js") != std::string::npos){
                        std::string joystick_path = 
                            search_directory + file_name;
                        joysticks.append(Joystick(joystick_path));
                        // joysticks.append(joystick_path);
                    }
                }
            }

            return joysticks;
        }
};


PYBIND11_MODULE(joystick, m)
{
    pybind11::class_<JoystickController>(m, "JoystickController")
        .def_static(
            "get_instance", &JoystickController::get_instance
        )
        .def(
            "get_joysticks", &JoystickController::get_joysticks,
            pybind11::arg("search_directory") = "/dev/input/"
        );

    pybind11::class_<Joystick>(m, "Joystick")
        .def(
            "set_on_event", &Joystick::set_on_event
        )
        .def(
            "is_running", &Joystick::is_running
        );

    pybind11::class_<JoystickEvent>(m, "JoystickEvent")
        .def(
            "get_timestamp", &JoystickEvent::get_timestamp
        )
        .def(
            "get_value", &JoystickEvent::get_value
        )
        .def(
            "get_type", &JoystickEvent::get_type
        )
        .def(
            "get_number", &JoystickEvent::get_number
        );
}
