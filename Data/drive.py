import socketio
import eventlet
from flask import Flask 
sio = socketio.Server()
app = Flask(__name__) #'__main__'

# @app.route('/home')
# def greeting():
#   return 'Welcome!'
@sio.on('connect')
def connect(sid, environ):
  print('Connected')

if __name__ == '__main__':
  # app.run(port=3000)
  app = socketio.Middleware(sio, app)
  eventlet.wsgi.server(eventlet.listen(('', 4567)), app)