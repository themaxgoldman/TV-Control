import time
import signal
import threading

class AudioDevice:

    def __init__(self):
        pass

    # Get the name of the device
    def get_name(self) -> str:
        # not implemented
        pass
    

    # Run the given function with a timeout
    def run_with_timeout(self, func, timeout):
        # Create a new thread
        thread = threading.Thread(target=func)

        # Start the thread
        thread.start()

        # Wait for the thread to finish for the specified amount of time
        thread.join(timeout)

        # If the thread is still running, terminate it
        if thread.is_alive():
            raise TimeoutError

    # Mute the device with a timeout
    def mute_with_timeout(self, mute: bool):
        def mute_func():
            if mute:
                self.mute_on()
            else:
                self.mute_off()

        self.run_with_timeout(mute_func, 1)

    # Mute the device
    def mute(self, mute: bool):
        try: 
            self.mute_with_timeout(mute)
        except TimeoutError:
            pass

    def mute_on(self):
        already_muted = self.already_muted()
        if not already_muted:
            self.send_mute_on_command()

    def send_mute_on_command(self):
        # not implemented
        pass

    def mute_off(self):
        if self.already_muted():
            self.send_mute_off_command()

    def send_mute_off_command(self):
        # not implemented
        pass

    def already_muted(self) -> bool:
        return self.send_already_muted_command()

    def send_already_muted_command(self) -> bool:
        # not implemented
        pass

    def get_volume(self) -> int:
        self.send_get_volume_command()

    def send_get_volume_command(self) -> int:
        # not implemented
        pass

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
        # not implemented
        pass

    def send_volume_down_command(self, change: int):
        # not implemented
        pass