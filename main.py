def on_button_pressed_a():
    serial.write_string("a")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    serial.write_string("b")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_ir_datagram():
    global hit
    hit = 1
makerbit.on_ir_datagram(on_ir_datagram)

def 的を倒す():
    global hit
    serial.write_string("a")
    pins.servo_write_pin(AnalogPin.P1, 160)
    music.set_volume(255)
    music.play(music.tone_playable(995, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.SAD)
    basic.pause(randint(0, 3000))
    strip.show_rainbow(1, 360)
    hit = 0
    basic.show_icon(IconNames.HAPPY)
strip: neopixel.Strip = None
hit = 0
radio.set_group(141)
basic.show_icon(IconNames.HAPPY)
pins.set_pull(DigitalPin.P2, PinPullMode.PULL_UP)
pins.servo_set_pulse(AnalogPin.P1, 2000)
pins.servo_write_pin(AnalogPin.P1, 90)
hit = 0
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
strip.set_brightness(30)
strip.show_rainbow(1, 360)
makerbit.connect_ir_receiver(DigitalPin.P2, IrProtocol.NEC)
serial.redirect_to_usb()
serial.set_baud_rate(BaudRate.BAUD_RATE9600)

def on_forever():
    if hit == 0:
        pins.servo_write_pin(AnalogPin.P1, 90)
        strip.rotate(1)
        strip.show()
    elif makerbit.ir_datagram() == "0x08F71FE0":
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        radio.send_string("white")
        的を倒す()
    elif makerbit.ir_datagram() == "0x08F71EE1":
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        radio.send_string("blue")
        的を倒す()
    elif makerbit.ir_datagram() == "0x08F71AE5":
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        radio.send_string("red")
        的を倒す()
basic.forever(on_forever)
