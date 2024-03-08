import cv2 as cv
from config import cameraId
class Camera:
    __cap = None
    isOpen = False
    __sendImg_t = None
    frame_count = 0
    fps = 0

    async def open_camera(self,args, event,queue):
        print('camera opened')
        if self.__cap is None:
            self.__cap = cv.VideoCapture(cameraId)
            self.fps = self.__cap.get(cv.CAP_PROP_FPS)
            self.isOpen = True
        if self.isOpen:
            await self.gather_camera_img(args, event,queue)
        return self.isOpen

    def close_camera(self):
        if self.__cap is None:
            return
        self.__cap.release()
        self.__cap = None
        self.isOpen = False

    def gather_t(self,args, event,queue):
        try:
            self.gather_camera_img(args, event,queue).send(None)
        except StopIteration:
            print('send img thread close')
            self.close_camera()

    async def gather_camera_img(self,args, event,queue):
        while self.isOpen:
            ret, frame = self.__cap.read()
            ret1, buffer =cv.imencode('.jpg', frame)
            picBytes = buffer.tobytes()
            queue.put(picBytes)
