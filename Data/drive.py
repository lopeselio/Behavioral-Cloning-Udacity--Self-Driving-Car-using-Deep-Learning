import socketio
import eventlet
from flask import Flask 
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image 
import numpy as np
sio = socketio.Server()

app = Flask(__name__) #'__main__'

 
def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img

@sio.on('telemetry')
def telemetry(sid, data):
  image = image.open(BytesIO(base64.b64decode(data['iamge'])))
  image = np.asarray(image)
@sio.on('connect')
def connect(sid, environ):
  print('Connected')
  send_control(0,0)

def send_control(steering_angle, throttle):
  sio.emit('steer', data = {
    'steering_angle': steering_angle.__str__(),
    'throttle': throttle.__str__()
  })
if __name__ == '__main__':
  # app.run(port=3000)
  model = load_model('model.h5')
  app = socketio.Middleware(sio, app)
  eventlet.wsgi.server(eventlet.listen(('', 4567)), app)