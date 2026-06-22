import gc
import machine
import radio
import random

gc.enable()

def initiate_mode:

    starter_channel = 6

    random_channel = random.randint(0, 83)

    radio.reset()
    radio.config(channel=starter_channel, power=7)

    pre_shared_key = 168856323

    encoded_channel_num = str(machine.unique_id() * pre_shared_key * random_channel)

    radio.send(encoded_channel_num)

    radio.config(channel=encoded_channel_num, power=7)

def recieve_mode:
    starter_channel = 6

    radio.reset()
    radio.config(channel=starter_channel, power=7)

    pre_shared_key = 168856323

    decoded_channnel_num = 