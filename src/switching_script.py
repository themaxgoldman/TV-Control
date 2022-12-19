import sys
from VizioTv import VizioTv
from AudioSystem import AudioSystem
from Config import Config

audio_system = AudioSystem(Config("config.json").get_audio_devices())
if __name__ == '__main__':
    tv_to_mute = sys.argv[1]
    audio_system.focus_device(tv_to_mute)
