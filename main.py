import gc
import microbit
import radio
import random

gc.enable()

pre_shared_key = 168856323

current_channel = 6

def initiate_mode():

    microbit.display.scroll('Initiating')

    radio.reset()
    radio.config(channel=current_channel, power=7)

def receive_mode():

    microbit.display.scroll('Receiving')

    radio.reset()
    radio.config(channel=current_channel, power=7)
    new_channel = radio.receive()

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

def init_channel_hop():
    microbit.display.scroll('hop')
    new_channel = random.randint(0,83)
    enc_new_channel = new_channel * pre_shared_key
    for i in range(11):
        radio.send(str(new_channel))
        microbit.sleep(1000)
    radio.config(channel=new_channel, power=7)
    for i in range(11):
        check_hopped = radio.receive()
        if str(check_hopped) == 'hopped':
            microbit.display.scroll(str(check_hopped))

def check_if_ready():
    for i in range(21):
        confirmation = radio.receive()
        microbit.display.scroll(str(confirmation))
        microbit.sleep(1000)
        if str(confirmation) == 'ready':
            init_channel_hop()
        else:
            pass

def rec_channel_hop():
    for i in range(11):
        radio.send('ready')
        microbit.sleep(1000)
    for i in range(11):
        new_channel = str(radio.receive())
        dec_new_channel = int(new_channel) / pre_shared_key
        microbit.sleep(1000)
    microbit.display.scroll(new_channel)
    radio.config(channel=int(dec_new_channel), power=7)
    for i in range(11):
        radio.send('hopped')
        microbit.sleep(1000)

while True:
    if microbit.pin_logo.is_touched():
        initiate_mode()
        check_if_ready()
    elif microbit.button_a.was_pressed():
        receive_mode()
        rec_channel_hop()