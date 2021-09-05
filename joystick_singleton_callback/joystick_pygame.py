import pygame
import threading


value_counter = 0


def _initialize_joystick():
    joysticks = []

    pygame.init()
    pygame.joystick.init()

    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        print(f"Found joystick {i}: ", joysticks[-1].get_name())

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
    axes = [ 0.0 ] * joystick.get_numaxes()
    buttons = [ False ] * joystick.get_numbuttons()

    keep_alive = True
    while keep_alive:
        try:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                keep_alive = False
            elif event.type == pygame.JOYAXISMOTION:
                axes[event.dict['axis']] = event.dict['value']
            elif event.type in [pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN]:
                buttons[event.dict['button']] ^= True

            _print_values(axes, buttons)
        except KeyboardInterrupt:
            keep_alive = False


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
