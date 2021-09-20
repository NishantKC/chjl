
import cv2
import dropbox
import time
import random
start=time.time()
def takepicture():
    number=random.randint(0,100)
    videoCapture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCapture.read()
        imgname="image"+str(number)+".png"
        cv2.imwrite(imgname,frame)
        start=time.time()
        result=False
    return imgname
    print("Photo taken")
    videoCapture.release()
    cv2.destroyAllWindows()

def dropbox123(imgname):
    accesstoken="Rgq9H3jM1nEAAAAAAAAAAfe2F7TOUNVXDFq-N19e4aw84x8JoCGrNzwSoumYPxtr"
    db=dropbox.Dropbox(accesstoken)
    f=open(imgname,"rb")
    db.files_upload(f.read(),"/img/"+imgname,mode=dropbox.files.WriteMode.overwrite)
    print("Files Uploaded")

def main():
    while(True):
        if((time.time()-start)>=5):
            name=takepicture()
            dropbox123(name)
main()