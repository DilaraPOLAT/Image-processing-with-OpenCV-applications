import  cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255 # canvas=Tual cizim icin gerekli olacak np.zeros() siyah ekran olusturmasını sagliyor
#(512,512,3) boyutu belirledim dtype=np.uint8 cızım ıcın kullandigimiz  veri tipi

#print(canvas) # 0'lardan olusan bir matris goruntulendi 0 karsiligi siyah
#bgr(0,0,0) siyah peki beyaz nasıl elde edecegiz bgr(255,255,255) canvas=np.zeros((512,512,3),dtype=np.uint8)+255 diyerek

#print(canvas)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

