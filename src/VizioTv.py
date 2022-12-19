import asyncio
import pyvizio
import time
from AudioDevice import AudioDevice


class VizioTv(AudioDevice):
    def __init__(self, name, ip_port, auth_token):
        self.vizio_tv = pyvizio.VizioAsync(
            name + str("_id"), ip_port, name, auth_token, "tv", None, None)
        self.name = name
        self.event_loop = asyncio.new_event_loop()

    def get_name(self) -> str:
        return self.name

    def send_mute_on_command(self):
        return self.event_loop.run_until_complete(self.vizio_tv.mute_on())

    def send_mute_off_command(self):
        return self.event_loop.run_until_complete(self.vizio_tv.mute_off())

    def send_already_muted_command(self) -> bool:
        return self.event_loop.run_until_complete(self.vizio_tv.is_muted())

    def get_volume(self) -> int:
        asyncio.get_event_loop().run_until_complete(self.vizio_tv.get_current_volume())

    def set_volume(self, target_volume: int):
        iterations = 0
        while current_volume != target_volume and iterations < 10:
            iterations += 1
            time.sleep(1)
            current_volume = self.get_volume()
            difference = target_volume - current_volume
            if difference > 0:
                self.send_volume_up_command(difference)
            else:
                self.send_volume_down_command(difference)

    def send_volume_up_command(self, change: int):
        asyncio.get_event_loop().run_until_complete(self.vizio_tv.vol_up(change))

    def send_volume_down_command(self, change: int):
        asyncio.get_event_loop().run_until_complete(self.vizio_tv.vol_down(-1 * change))
