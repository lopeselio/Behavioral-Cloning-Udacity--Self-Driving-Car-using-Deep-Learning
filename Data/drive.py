import socketio
import eventlet
from flask import Flask 
from keras.models import load_model

sio = socketio.Server()
app = Flask(__name__) #'__main__'

@sio.on('connect')
def connect(sid, environ):
  print('Connected')
  send_control(0,1)

def send_control(steering_angle, throttle):
  sio.emit('steer', data = {
    'steering_angle': steering_angle.__str__(),
    'throttle': throttle.__str__()
  })
if __name__ == '__main__':
  # app.run(port=3000)
  app = socketio.Middleware(sio, app)
  eventlet.wsgi.server(eventlet.listen(('', 4567)), app)