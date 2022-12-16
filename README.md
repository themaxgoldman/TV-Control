Audio Device Control System
This code provides a system for controlling multiple audio devices, including Vizio TVs and Denon Receivers.

Classes
AudioDevice
This is an abstract base class for audio devices that can be controlled by the system. It has the following methods:

mute: Mutes or unmutes the device, depending on the value of the mute parameter.
mute_on: Mutes the device.
mute_off: Unmutes the device.
already_muted: Returns a boolean indicating whether the device is currently muted.
get_volume: Returns the current volume of the device.
set_volume: Sets the volume of the device to the target volume specified as a parameter.
AudioSystem
This class is responsible for managing a collection of audio devices. It has the following methods:

__init__: Constructor that takes in an arbitrary number of audio devices and stores them in a dictionary with the device names as keys.
focus_device: Mutes all devices except for the one specified by the device_name parameter.
VizioTv
This class inherits from AudioDevice and provides implementation details for controlling Vizio TVs. It has methods for sending commands to the TV over a network connection, such as send_mute_on_command and send_get_volume_command.

DenonReceiver
This class also inherits from AudioDevice and provides implementation details for controlling Denon Receivers. It uses the telnetlib module to establish a Telnet connection with the receiver and has methods for sending commands over this connection, such as send_mute_on_command and send_get_volume_command.