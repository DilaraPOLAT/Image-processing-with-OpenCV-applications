import cv2

##cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
## 0 yazdıgımızda webcam acılır yol belirtirsek o videyu acar
## cv2.CAP_DSHOW webcam acarken hata aldım sourceReader gibi bir sey yazıyordu bunu yazınca hata duzeldı python surumu ile ilgili
cap= cv2.VideoCapture("antalya.mp4")
while True:
    ret,frame=cap.read()## eger cap.read() frameleri dogru okuduysa ret true yanlıs okuduysa false dır.
    if ret == 0:
        break
    frame=cv2.flip(frame,1) ##y eksenine gore her bir frame goruntulenecek
    ##cv2.imshow("webcam",frame)
    cv2.imshow("antalya", frame)
    if cv2.waitKey(50) & 0xFF == ord('q'): ##her bir frame 30 saniye gozukecek ve diger frame gecilecek
        break

cap.release()
cv2.destroyAllWindows()

