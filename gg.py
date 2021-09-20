import cv2
def takepicture():
    videoCapture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCapture.read()
        cv2.imwrite("image1.png",frame)
        result=False
    videoCapture.release()
    cv2.destroyAllWindows()

takepicture()