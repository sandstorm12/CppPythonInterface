#include <fcntl.h>
#include <iostream>
#include <pybind11/pybind11.h>


class JoystickController {
    private:
        const static Joystick joystick;
    
    public:
        const static Joystick get_instance() {
            return Joystick::joystick;
        }

        const list_joysticks
};


class Joystick {
    private:
        string name;
        int num
    
    public:
        const static Joystick get_instance() {
            return Joystick::joystick;
        }

        const list_joysticks
};


PYBIND11_MODULE(joystick, m)
{
    pybind11::class_<JoystickController>(m, "JoystickController")
        .def(
            "get_value", &JoystickController::get_value
        );
}
