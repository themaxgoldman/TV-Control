class AudioSystem:
    def __init__(self, *audio_devices):
        self.audio_devices = {device.get_name():device for device in audio_devices}
    
    def focus_device(self, device_name):
        for name, device in self.audio_devices.items():
            if name == device_name:
                device.mute_off()
            else:
                device.mute_on()

    