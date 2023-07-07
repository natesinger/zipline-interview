# native
import os
import sys
import math
import json
import logging

# third-party
import google.cloud.logging
from flask import (
    Flask,
    render_template,
    send_from_directory
)
from flask_socketio import SocketIO, emit

# internal
pass

# setup environment and instantiate app
required_environment_variables = [
    'ZIPLINE_SECRET',
]

with open('simulation.json', 'r') as fio:
    simulation_data = json.load(fio)
    logging.info(f'got simulation data {len(simulation_data)}')

for environment_variable in required_environment_variables:
    if environment_variable not in os.environ:
        logging.error(f'required environment variable {environment_variable} is missing, exiting...')
        sys.exit(-1)

DIST_LOCATION = '../frontend/dist'
app = Flask(__name__, template_folder=DIST_LOCATION)
app.config['DIST_LOCATION'] = DIST_LOCATION
app.secret_key = os.environ.get("ZIPLINE_SECRET")

# configure logging
if bool(os.environ.get("ZIPLINE_LOGLOCAL", 0)):
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d (%(levelname)s | %(filename)s:%(lineno)d) - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    logging.info("logging set to stdout instead of GCP")

else: google.cloud.logging.Client().setup_logging()

# extend gunicorn so that WSGI errors are logged
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)
app.logger.debug('this will show in the log')

# establish web socket worker
socketio = SocketIO(app)

# routes
@app.route('/', methods=['GET'])
def root(): return render_template('home.html')

@app.route('/css/<path:filename>')
def assets_css(filename:str): return send_from_directory(f"{app.config['DIST_LOCATION']}/css/", filename)

@app.route('/js/<path:filename>')
def assets_js(filename:str): return send_from_directory(f"{app.config['DIST_LOCATION']}/js/", filename)

@app.route('/fonts/<path:filename>')
def assets_fonts(filename:str): return send_from_directory(f"{app.config['DIST_LOCATION']}/fonts/", filename)

@app.route('/img/<path:filename>')
def assets_img(filename:str): return send_from_directory(f"{app.config['DIST_LOCATION']}/img/", filename)

@app.route('/favicon.png')
def assets_logo(): return send_from_directory(f"{app.config['DIST_LOCATION']}/", 'favicon.png')

# catchall 404 fallback
@app.route('/<path:path>', methods=['GET'])
def catch_all(path): return render_template('404.html')

@socketio.on('connect')
def process_connect():
    logging.info('client connected')
    emit('my response', 'connected')

"""
flights = [
    { 'id': '38206', 'status': 'deployed', 'destination': 'Kibilizi', 'x': 38907, 'y': -31610 },
    { 'id': '99519', 'status': 'deployed', 'destination': 'Gitwe', 'x': 57316, 'y': -16810 },
    { 'id': '25483', 'status': 'standby', 'destination': 'N/A', 'x': 0, 'y': 0 },
    { 'id': '94273', 'status': 'deployed', 'destination': 'Muhororo', 'x': 27555, 'y': 11922 },
    { 'id': '07213', 'status': 'deployed', 'destination': 'Murunda', 'x': 11111, 'y': -2240 },
    { 'id': '05521', 'status': 'standby', 'destination': 'N/A', 'x': 0, 'y': 0 },
    { 'id': '56821', 'status': 'deployed', 'destination': 'Ruhango', 'x': 22316, 'y': -19610 },
    { 'id': '77250', 'status': 'deployed', 'destination': 'Shyira', 'x': 18316, 'y': -29610 },
    { 'id': '96216', 'status': 'standby', 'destination': 'N/A', 'x': 0, 'y': 0 },
    { 'id': '21708', 'status': 'standby', 'destination': 'N/A', 'x': 0, 'y': 0 },
]
futureOrders = [
    {'id': 54159, 'time': 39659, 'destination': 'Kaduha', 'status': 'Emergency'},
    {'id': 97720, 'time': 45754, 'destination': 'Butaro', 'status': 'Resupply'},
    {'id': 24205, 'time': 85968, 'destination': 'Butaro', 'status': 'Resupply'},
    {'id': 47570, 'time': 30191, 'destination': 'Nemba', 'status': 'Resupply'},
    {'id': 90971, 'time': 83419, 'destination': 'Gakoma', 'status': 'Emergency'},
    {'id': 95494, 'time': 40989, 'destination': 'Nyanza', 'status': 'Resupply'},
    {'id': 34292, 'time': 79100, 'destination': 'Kabaya', 'status': 'Emergency'},
    {'id': 20833, 'time': 18815, 'destination': 'Gitwe', 'status': 'Resupply'},
    {'id': 21116, 'time': 24698, 'destination': 'Kinihira', 'status': 'Resupply'},
    {'id': 59009, 'time': 81197, 'destination': 'Nyanza', 'status': 'Resupply'},
    {'id': 56721, 'time': 38718, 'destination': 'Byumba', 'status': 'Resupply'},
    {'id': 15686, 'time': 31643, 'destination': 'Kigeme', 'status': 'Emergency'},
    {'id': 48414, 'time': 79674, 'destination': 'Kibilizi', 'status': 'Emergency'},
    {'id': 78768, 'time': 47886, 'destination': 'Gakoma', 'status': 'Resupply'},
    {'id': 66124, 'time': 26961, 'destination': 'Kaduha', 'status': 'Resupply'},
    {'id': 94182, 'time': 76879, 'destination': 'Nemba', 'status': 'Emergency'},
    {'id': 23688, 'time': 74704, 'destination': 'Butaro', 'status': 'Emergency'},
    {'id': 27074, 'time': 29761, 'destination': 'Ruhango', 'status': 'Emergency'},
    {'id': 82231, 'time': 1552, 'destination': 'Nyanza', 'status': 'Resupply'},
    {'id': 32248, 'time': 26930, 'destination': 'Nemba', 'status': 'Emergency'},
    {'id': 24645, 'time': 72588, 'destination': 'Gitwe', 'status': 'Emergency'},
    {'id': 30146, 'time': 24729, 'destination': 'Ruhango', 'status': 'Resupply'},
    {'id': 87480, 'time': 61512, 'destination': 'Kibilizi', 'status': 'Resupply'},
    {'id': 11625, 'time': 10434, 'destination': 'Murunda', 'status': 'Resupply'},
    {'id': 63397, 'time': 75717, 'destination': 'Muhororo', 'status': 'Emergency'},
    {'id': 33038, 'time': 59378, 'destination': 'Nemba', 'status': 'Resupply'},
    {'id': 18746, 'time': 72601, 'destination': 'Kabaya', 'status': 'Emergency'},
    {'id': 13176, 'time': 66277, 'destination': 'Kaduha', 'status': 'Emergency'},
    {'id': 69971, 'time': 40995, 'destination': 'Shyira', 'status': 'Emergency'},
    {'id': 16289, 'time': 30032, 'destination': 'Kabgayi', 'status': 'Emergency'}
]
"""

@socketio.on('message_event')
def process_message(message):
    time_seconds = message['data']

    try:
        time_rounded = str(math.floor(int(time_seconds) / 60) * 60)
        response_object = simulation_data[time_rounded]
    except KeyError:
        logging.warning('no flights found')
        response_object = {'flights': [], 'futureOrders': []}

    emit('message_event', json.dumps(response_object))

@socketio.on('disconnect')
def process_disconnect():
    logging.info('Client disconnected')

# start app in debug mode if run directly without gunicorn
if __name__ == '__main__':
    socketio.run(app,
        host = "0.0.0.0",
        port=5000,
        debug=True
    )
