import glob
import struct
import threading


value_counter = 0


def _initialize_joystick():
    joysticks = glob.glob('/dev/input/js*')

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
    EVENT_SIZE = struct.calcsize("<Ihbb")
    file = open(joystick, "rb")
    event = file.read(EVENT_SIZE)
    while event:
        # More: https://www.kernel.org/doc/Documentation/input/joystick-api.txt
        timestamp, value, type, number = struct.unpack("<Ihbb", event)

        print("Timestamp: {} Type: {} Number: {} Value: {}".format(
                timestamp, type, number, value
            )
        )

        event = file.read(EVENT_SIZE)


if __name__ == "__main__":
    joysticks = _initialize_joystick()

    threads = _read_from_joysticks(joysticks)

    _wait_on_threads(threads)
