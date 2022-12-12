import pyvizio
import asyncio
import sys
import telnetlib

TV_TYPE = "tv"

LEFT_TV_ID = "left_tv"
LEFT_TV_IP_PORT = "192.168.1.219:7345"
LEFT_TV_AUTH = "Zlnsf02jzd"
LEFT_TV_NAME = "Left TV"

RIGHT_TV_ID = "right_tv"
RIGHT_TV_IP_PORT = "192.168.1.220:7345"
RIGHT_TV_AUTH = "Z2p9ms0jj9"
RIGHT_TV_NAME = "Right TV"

DENON_IP = "192.168.1.172"
DENON_PORT = 23
DENON_TIMEOUT = 100

def mute_tv(tv, desired_mute_state):
    already_muted = asyncio.get_event_loop().run_until_complete(tv.is_muted())
    print(already_muted)
    if(desired_mute_state is not already_muted):
        asyncio.get_event_loop().run_until_complete(tv.mute_on())

def mute_left_tv(desired_mute_state):
    left_tv = pyvizio.VizioAsync(LEFT_TV_ID, LEFT_TV_IP_PORT, LEFT_TV_NAME, LEFT_TV_AUTH, TV_TYPE, None, None)
    mute_tv(left_tv, desired_mute_state)

def mute_right_tv(desired_mute_state):
    right_tv = pyvizio.VizioAsync(RIGHT_TV_ID, RIGHT_TV_IP_PORT, RIGHT_TV_NAME, RIGHT_TV_AUTH, TV_TYPE, None, None)
    mute_tv(right_tv, desired_mute_state)

def mute_denon(desired_mute_state):
    session = telnetlib.Telnet(DENON_IP, DENON_PORT, DENON_TIMEOUT)
    if(desired_mute_state):
        session.write(b"MUON")
    else:
        session.write(b"MUOFF")
    session.close()

def focus_sound(tv_num):
    tv_mute_commands = [mute_left_tv, mute_denon, mute_right_tv]
    for i,tv_mute_command in enumerate(tv_mute_commands):
        if(tv_num == -1 or i != tv_num):
            tv_mute_command(True)
        else:
            tv_mute_command(False)

if __name__ == '__main__':
    tv_to_mute = int(sys.argv[1])
    focus_sound(tv_to_mute)
