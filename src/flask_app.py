import json
from flask import Flask
from flask import render_template
from AudioSystem import AudioSystem
from Config import Config

app = Flask(__name__)

config_file = 'config.json'
audio_system = AudioSystem(Config(config_file).get_audio_devices())
device_names = list(audio_system.audio_devices.keys())


@app.route('/')
def index():
    return render_template('index.html', device_names=device_names)


@app.route('/focus/<device_name>')
def focus(device_name):
    audio_system.focus_device(device_name)
    return 'Focused on device: {}'.format(device_name)


if __name__ == '__main__':
    app.run("0.0.0.0")
