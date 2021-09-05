import time

from joystick import JoystickController


joystick_controller = JoystickController.get_instance()
joysticks = joystick_controller.get_joysticks()

print("Joysticks found: {}".format(len(joysticks)))


def on_event(event):
    print(
        event.get_timestamp(),
        event.get_value(),
        event.get_type(),
        event.get_number(),
        "\n"
    )


for joystick in joysticks:
    joystick.set_on_event(on_event)

# Wait for util your work is done
for joystick in joysticks:
    while joystick.is_running():
        time.sleep(.5)
