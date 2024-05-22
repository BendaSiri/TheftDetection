# import urllib.request
# import cv2

# url = [0,'http://100.72.226.182:8080/video','http://100.72.226.182:8080/video']
# ds_factor=0.6
# cap = cv2.VideoCapture(url[1])
# class VideoCamera(object):
#     def __init__(self):
#        #capturing video
#        self.video1 = cv2.VideoCapture(url[0])
#        self.video2 = cv2.VideoCapture(url[1])
#        self.video3 = cv2.VideoCapture(url[2])
      
#     def __del__(self):
#         #releasing camera
#         self.video1.release()
#         self.video2.release()
#         self.video3.release()
        
#     def get_frame(self):
#       #extracting frames
#       _, frame1 = self.video1.read()
#       _, frame2 = self.video2.read()
#       _, frame3 = self.video3.read()
#       frame1=cv2.resize(frame1,None,fx=ds_factor,fy=ds_factor,
#       interpolation=cv2.INTER_AREA)
#       frame2=cv2.resize(frame2,None,fx=ds_factor,fy=ds_factor,
#       interpolation=cv2.INTER_AREA)
#       frame3=cv2.resize(frame3,None,fx=ds_factor,fy=ds_factor,
#       interpolation=cv2.INTER_AREA)
#       ret, jpeg1 = cv2.imencode('.jpg',frame1)
#       ret, jpeg2 = cv2.imencode('.jpg',frame2)
#       ret, jpeg3 = cv2.imencode('.jpg',frame3)
#       return jpeg1.tobytes(), jpeg2.tobytes(), jpeg3.tobytes()
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

