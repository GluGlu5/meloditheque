def méloPiratesCaraïbes():
    pass
def méloStarWars():
    global Notes$, listeNotes, nmbrNotes, Durées$, listeDurées, note, durée
    Notes$ = "293.66, 293.66, 293.66, 392.0, 622.25, 554.37, 523.25, 454, 932.32, 622.25, 554.37, 523.25, 454, 932.32, 622.25, 554.37, 523.25, 554.37, 454"
    listeNotes = Notes$.split(",")
    nmbrNotes = len(listeNotes)
    Durées$ = "180, 180, 180, 800, 800, 180, 180, 180, 800, 400, 180, 180, 180, 800, 400, 180, 180, 180, 1000"
    listeDurées = Notes$.split(",")
    index = 0
    while index <= nmbrNotes:
        note = parse_float(listeNotes[index])
        durée = parse_float(listeDurées[index]) / 2
        music.play(music.tone_playable(note, durée),
            music.PlaybackMode.UNTIL_DONE)
        index += 1
durée = 0
note = 0
listeDurées: List[str] = []
Durées$ = ""
nmbrNotes = 0
listeNotes: List[str] = []
Notes$ = ""
méloStarWars()
basic.pause(500)
music.set_tempo(120)
music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
    music.PlaybackMode.UNTIL_DONE)
serial.redirect_to_usb()
serial.write_line("" + control.device_name() + " vous salue")
for index2 in range(100):
    led.plot_brightness(randint(0, 4), randint(0, 4), randint(0, 255))
    basic.pause(50)
basic.show_icon(IconNames.HAPPY)
radio.set_group(7)
radio.set_frequency_band(7)
radio.send_string("J'utilise le groupe 7 sur le canal 7")

def on_every_interval():
    music.play(music.builtin_playable_sound_effect(soundExpression.hello),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("DATA via USB" + "")
    serial.write_line("Communication série via " + "USB")
    serial.write_line("Communication radio via canal " + "7")
    serial.write_line("Groupe radio " + "7")
    serial.write_line("Nom :  " + control.device_name())
    serial.write_line("No serie :  " + str(control.device_serial_number()))
    serial.write_line("Etat des broches" + "" + "")
    serial.write_line("P     num ~ analogique" + "" + "")
    serial.write_line("P 0 : " + str(pins.digital_read_pin(DigitalPin.P0)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P0)))
    serial.write_line("P 1 : " + str(pins.digital_read_pin(DigitalPin.P1)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P1)))
    serial.write_line("P 2 : " + str(pins.digital_read_pin(DigitalPin.P2)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P2)))
    serial.write_line("P 3 : " + str(pins.digital_read_pin(DigitalPin.P3)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P3)))
    serial.write_line("P 4 : " + str(pins.digital_read_pin(DigitalPin.P4)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P4)))
    serial.write_line("P 5 : " + str(pins.digital_read_pin(DigitalPin.P5)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P5)))
    serial.write_line("P 6 : " + str(pins.digital_read_pin(DigitalPin.P6)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P6)))
    serial.write_line("P 7 : " + str(pins.digital_read_pin(DigitalPin.P7)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P7)))
    serial.write_line("P 8 : " + str(pins.digital_read_pin(DigitalPin.P8)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P8)))
    serial.write_line("P 9 : " + str(pins.digital_read_pin(DigitalPin.P9)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P9)))
    serial.write_line("P10 : " + str(pins.digital_read_pin(DigitalPin.P10)) + " ~ " + "")
    serial.write_line("P11 : " + str(pins.digital_read_pin(DigitalPin.P11)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P11)))
    serial.write_line("P12 : " + str(pins.digital_read_pin(DigitalPin.P12)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P12)))
    serial.write_line("P13 : " + str(pins.digital_read_pin(DigitalPin.P13)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P13)))
    serial.write_line("P14 : " + str(pins.digital_read_pin(DigitalPin.P14)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P14)))
    serial.write_line("P15 : " + str(pins.digital_read_pin(DigitalPin.P15)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P15)))
    serial.write_line("P16 : " + str(pins.digital_read_pin(DigitalPin.P16)) + " ~ " + str(pins.analog_read_pin(AnalogPin.P16)))
    méloPiratesCaraïbes()
    méloStarWars()
loops.every_interval(10000, on_every_interval)
