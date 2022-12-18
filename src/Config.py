import json
from DenonReceiver import DenonReceiver
from VizioTv import VizioTv


class Config:
    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            self.config = json.load(f)

    def get_device_config(self, device_name: str):
        return self.config.get(device_name)

    def get_vizio_tv(self, device_name: str):
        config = self.get_device_config(device_name)
        if config and config['platform'] == 'viziotv':
            return VizioTv(device_name, config['host'] + ':' + config['port'], config['auth_token'])
        return None

    def get_denon_receiver(self, device_name: str):
        config = self.get_device_config(device_name)
        if config and config['platform'] == 'denonavr':
            return DenonReceiver(config['host'], config['port'], config['timeout'], device_name)
        return None

    def get_audio_devices(self):
        audio_devices = []
        for device_name, config in self.config.items():
            if config['platform'] == 'viziotv':
                audio_devices.append(self.get_vizio_tv(device_name))
            elif config['platform'] == 'denonavr':
                audio_devices.append(self.get_denon_receiver(device_name))
        return audio_devices
