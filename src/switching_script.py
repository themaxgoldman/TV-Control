import sys
from VizioTv import VizioTv
from DenonReceiver import DenonReceiver
from AudioSystem import AudioSystem

LEFT_TV_IP_PORT = "192.168.1.219:7345"
LEFT_TV_AUTH = "Zlnsf02jzd"
LEFT_TV_NAME = "Left TV"
left_tv = VizioTv(LEFT_TV_NAME, LEFT_TV_IP_PORT, LEFT_TV_AUTH)

RIGHT_TV_IP_PORT = "192.168.1.220:7345"
RIGHT_TV_AUTH = "Z2p9ms0jj9"
RIGHT_TV_NAME = "Right TV"
right_tv = VizioTv(RIGHT_TV_NAME, RIGHT_TV_IP_PORT, RIGHT_TV_AUTH)


DENON_IP = "192.168.1.172"
DENON_PORT = 23
DENON_TIMEOUT = 100
DENON_RECEIVER_NAME = "Denon Receiver"
denon_receiver = DenonReceiver(DENON_IP, DENON_PORT, DENON_TIMEOUT, DENON_RECEIVER_NAME)

audio_system = AudioSystem(left_tv, right_tv, denon_receiver)
if __name__ == '__main__':
    tv_to_mute = sys.argv[1]
    audio_system.focus_device(tv_to_mute)
