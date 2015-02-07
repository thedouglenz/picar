from flask import Flask
from flask_sockets import Sockets
import json
import carfunc as car

# Start Flask server + init flask_sockets.Socket
app = Flask(__name__)
app.config['DEBUG'] = True
sockets = Scokets(app)

# Flask
@app.route('/')
def root():
    return send_from_directory('www', 'index.html')

@app.route('/<any(css, img, js, sound):folder>/<path:filename>')
def toplevel_static(folder, filename):
    filename = safe_join(folder, filename)
    cache_timeout = app.get_send_file_max_age(filename)
    return send_from_directory(app.static_folder, filename, cache_timeout=cache_timeout)

@sockets.route('/picar')
def control(ws):
    while True:
        try:
            m = ws.receive()
        except Exception:
            pass
        if m:
            obj = json.loads(m)
	    car.key_in(m['keys'])
