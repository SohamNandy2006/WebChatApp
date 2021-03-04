from flask import *
from flask_socketio import *
import logging
app = Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
# logging.basicConfig(filename='error.log',level=logging.DEBUG)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html',username=username,room=room)
    else:
        return "Bad/incomplete Request Errror Code 405/400"

@socketio.on('send_message')
def handle_send_message_event(data):
    print('{} at room {}: {}'.format(data["username"],data["room"],data["message"]))
    socketio.emit('recieve_message', data,room=data["room"])
@socketio.on('join_room')
def handle_join_room_event(data):
    print("{} has joined room {}".format(data["username"],data["room"]))
    # logging.info("{} has joined room {}".format(data["username"],data["room"]))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=80,debug=True)
