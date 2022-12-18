# TV Control
This repository contains a Python module for controlling an audio system that consists of one or more audio devices.

## Classes
- `AudioDevice`: Abstract base class for audio devices. Contains methods for muting and unmuting the device, setting and getting the volume, and checking if the device is already muted.
- `DenonReceiver`: Concrete implementation of AudioDevice for Denon receivers. Contains methods for sending commands over a telnet connection to control the device.
- `VizioTv`: Concrete implementation of AudioDevice for Vizio TVs. Contains methods for sending HTTP requests to control the device.
- `AudioSystem`: Class that represents an audio system, where the audio system consists of one or more audio devices. Contains a method for focusing on a specific device, by muting all other devices and unmuting the specified device.
- `Config`: Class for parsing a configuration file and creating instances of DenonReceiver and VizioTv based on the configuration.

## Example
```
import json
from AudioSystem import AudioSystem, Config

with open('config.json', 'r') as f:
    config = json.load(f)

audio_system = AudioSystem(Config("config.json").get_audio_devices())
audio_system.focus_device('Living Room Receiver')
```

## Configuration
```
{
  "device_name_1": {
    "platform": "denonavr" or "viziotv",
    "host": "hostname",
    "port": "port",
    "timeout": timeout (only for denonavr),
    "auth_token": "auth_token" (only for viziotv)
  },
  "device_name_2": {
    ...
  }
}

```