import gc
import microbit
import radio
import random

gc.enable()

pre_shared_key = 168856323

current_channel = 6

def initiate_mode():

    microbit.display.scroll('Initiating')

    new_channel = random.randint(0, 83)

    radio.reset()
    radio.config(channel=current_channel, power=7)

def receive_mode():

    microbit.display.scroll('Receiving')

    radio.reset()
    radio.config(channel=current_channel, power=7)
    new_channel = radio.receive()

    for i in range(11):
        radio.send('ready')
        microbit.sleep(1000)

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

def on_ready():
    new_channel = random.randint(0,83)
    while True:
        if new_channel == current_channel:
            new_channel = random.randint(0,83)
        else:
            current_channel = new_channel
            radio.config(channel=current_channel, power=7)

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