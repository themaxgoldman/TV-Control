import telnetlib
from AudioDevice import AudioDevice

class DenonReceiver(AudioDevice):
    def __init__(self, ip, port, timeout, name):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def mute_on(self):
        self.send_mute_on_command()

    def send_mute_on_command(self):
        self.send_command("MUON")

    def mute_off(self):
        self.send_mute_off_command()
    
    def send_mute_off_command(self):    
        self.send_command("MUOFF")

    def send_command(self, command):
        session = telnetlib.Telnet(self.ip, self.port, self.timeout)
        session.write(command.encode('ascii') + b"\r")
        session.close   
    
