# from flask import Flask, render_template, Response
# from camera import VideoCamera
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')
# def gen(camera):
#     while True:
#         #get camera frame
#         frame,_,_= camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
# def gen1(camera):
#     while True:
#         #get camera frame
#         _,frame2,_ = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n\r\n')
# def gen2(camera):
#     while True:
#         #get camera frame
#         _,_,frame3 = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame3 + b'\r\n\r\n')
# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(VideoCamera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/video_feed1')
# def video_feed1():
#     return Response(gen1(VideoCamera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
# @app.route('/video_feed2')
# def video_feed2():
#     return Response(gen2(VideoCamera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
# if __name__ == '__main__':
#     # defining server ip address and port
#     app.run(host='0.0.0.0',port='5000', debug=True)


import cv2

class VideoCamera(object):
    def __init__(self):
        # Open a connection to the webcam using DirectShow backend
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def __del__(self):
        # Release the webcam when the object is destroyed
        self.video.release()

    def get_frame(self):
        # Read a frame from the webcam
        success, image = self.video.read()
        if not success:
            return None, None, None

        # Encode the frame in JPEG format
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()

        # For this example, we will return the same frame for all outputs
        return frame, frame, frame
from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        # get camera frame
        frame, _, _ = camera.get_frame()
        if frame is None:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen1(camera):
    while True:
        # get camera frame
        _, frame2, _ = camera.get_frame()
        if frame2 is None:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n\r\n')

def gen2(camera):
    while True:
        # get camera frame
        _, _, frame3 = camera.get_frame()
        if frame3 is None:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame3 + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed1')
def video_feed1():
    return Response(gen1(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(gen2(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
