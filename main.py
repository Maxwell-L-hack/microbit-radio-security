import gc
import microbit
import radio
import random

gc.enable()

def initiate_mode():

    microbit.display.scroll('Initiating')

    starter_channel = 6

    new_channel = random.randint(0, 83)

    radio.reset()
    radio.config(channel=starter_channel, power=7)

    pre_shared_key = 168856323

def receive_mode():

    microbit.display.scroll('Receiving')

    starter_channel = 6

    radio.reset()
    radio.config(channel=starter_channel, power=7)

    pre_shared_key = 168856323
    new_channel = radio.receive()

    while True:
        radio.send('ready')

def waiting_animation():
    while True:
        microbit.display.show(microbit.Image('00000:'
                                             '00000:'
                                             '00900:'
                                             '00000:'
                                             '00000'))
        microbit.sleep(1000)
        microbit.display.show(microbit.Image('00000:'
                                             '09990:'
                                             '09590:'
                                             '09990:'
                                             '00000'))
        microbit.sleep(1000)
        microbit.display.show(microbit.Image('99999:'
                                             '95559:'
                                             '95159:'
                                             '95559:'
                                             '99999'))
        microbit.sleep(1000)


def check_if_ready():
    while True:
        confirmation = radio.receive()
        microbit.display.scroll(str(confirmation))

while True:
    if microbit.pin_logo.is_touched():
        initiate_mode()
        check_if_ready()
    elif microbit.button_a.was_pressed():
        receive_mode()