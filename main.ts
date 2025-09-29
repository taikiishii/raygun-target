input.onButtonPressed(Button.A, function () {
    serial.writeString("a")
})
input.onButtonPressed(Button.B, function () {
    serial.writeString("b")
})
makerbit.onIrDatagram(function () {
    hit = 1
})
function 的を倒す () {
    serial.writeString("a")
    pins.servoWritePin(AnalogPin.P1, 160)
    music.setVolume(255)
    music.play(music.tonePlayable(995, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Sad)
    basic.pause(randint(0, 3000))
    strip.showRainbow(1, 360)
    hit = 0
    basic.showIcon(IconNames.Happy)
}
let strip: neopixel.Strip = null
let hit = 0
radio.setGroup(141)
basic.showIcon(IconNames.Happy)
pins.setPull(DigitalPin.P2, PinPullMode.PullUp)
pins.servoSetPulse(AnalogPin.P1, 2000)
pins.servoWritePin(AnalogPin.P1, 90)
hit = 0
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
strip.setBrightness(30)
strip.showRainbow(1, 360)
makerbit.connectIrReceiver(DigitalPin.P2, IrProtocol.NEC)
serial.redirectToUSB()
serial.setBaudRate(BaudRate.BaudRate9600)
basic.forever(function () {
    if (hit == 0) {
        pins.servoWritePin(AnalogPin.P1, 90)
        strip.rotate(1)
        strip.show()
    } else if (makerbit.irDatagram() == "0x08F71FE0") {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        radio.sendString("white")
        的を倒す()
    } else if (makerbit.irDatagram() == "0x08F71EE1") {
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        radio.sendString("blue")
        的を倒す()
    } else if (makerbit.irDatagram() == "0x08F71AE5") {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        radio.sendString("red")
        的を倒す()
    }
})
