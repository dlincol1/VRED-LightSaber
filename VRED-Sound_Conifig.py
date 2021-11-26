sound_on = findNode('saberOn.wav')
sound_off = findNode('saberOff.wav')
sound_idle = findNode('saberHum.wav')

sounds = [sound_off, sound_on, sound_idle]

sound_ptrs = []
for count, i in enumerate(sounds):
    i.setFieldBool("play", False)
    sound_ptrs.append(i)

    print(f'Configured: {i.getName()}')
