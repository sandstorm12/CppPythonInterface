import glob
import struct
import threading


# infile_path = "/dev/input/js0"
# EVENT_SIZE = struct.calcsize("llHHI")
# file = open(infile_path, "rb")
# event = file.read(EVENT_SIZE)
# while event:
#     print(struct.unpack("llHHI", event))
#     (tv_sec, tv_usec, type, code, value) = struct.unpack("llHHI", event)
#     event = file.read(EVENT_SIZE)

value_counter = 0


def _initialize_joystick():
    joysticks = glob.glob('/dev/input/event15')

    for i in range(len(joysticks)):
        print(f"Found joystick {i}: ", joysticks[i])

    return joysticks


def _read_from_joysticks(joysticks):
    threads = []

    for joystick in joysticks:
        thread = threading.Thread(
            target=_joystick_event_loop, args=(joystick,)
        )
        thread.daemon = True
        thread.start()
        
        threads.append(thread)

    return threads


def _wait_on_threads(threads):
    for thread in threads:
        thread.join()


def _joystick_event_loop(joystick):
    EVENT_SIZE = struct.calcsize("4IHHI")
    file = open(joystick, "rb")
    event = file.read(EVENT_SIZE)
    while event:
        print(struct.unpack("4IHHI", event))
        # (tv_sec, type, code, value) = struct.unpack("4IHHI", event)
        event = file.read(EVENT_SIZE)


def _print_values(axes, buttons):
    global value_counter

    axes_string = " ".join(
        ["{:.3f}".format(axe_value) for axe_value in axes]
    )

    buttons_string = " ".join(
        ["Down" if button_value else "Up" for button_value in buttons]
    )

    print("Response: {} \nAnalog sticks: {} \nButtons: {}\n".format(
            value_counter, axes_string, buttons_string
        )
    )

    value_counter += 1


if __name__ == "__main__":
    joysticks = _initialize_joystick()

    threads = _read_from_joysticks(joysticks)

    _wait_on_threads(threads)
