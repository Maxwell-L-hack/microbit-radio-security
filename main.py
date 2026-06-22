import gc
import microbit
import radio
import random

gc.enable()

def initiate_mode():

    microbit.display.scroll('Initiating')

    starter_channel = 6

    random_channel = random.randint(0, 83)

    radio.reset()
    radio.config(channel=starter_channel, power=7)

    pre_shared_key = 168856323

    radio.send(str(random_channel))

    radio.config(channel=random_channel, power=7)

def recieve_mode():
    starter_channel = 6

    radio.reset()
    radio.config(channel=starter_channel, power=7)

    pre_shared_key = 168856323
    new_channel = radio.receive()

    if new_channel is not None:
        new_channel_int = int(new_channel)
        radio.config(channel=new_channel_int, power=7)
        microbit.display.scroll(new_channel_int)

while True:
    if microbit.pin_logo.is_touched():
        initiate_mode()