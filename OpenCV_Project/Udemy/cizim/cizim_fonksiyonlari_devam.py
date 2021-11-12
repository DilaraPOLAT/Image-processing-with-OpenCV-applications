import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255   #siyah tual olusturuluyor 3 kanal sayısı dtype=np.uint8 cizim yapınca kullanılır
#bgr(0,0,0) siyah 255 eklersek beyaz olur
#cizgi
cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5)
cv2.line(canvas,(100,50),(200,250),(0,0,255),thickness=7)
           # tual,baslangıc, bitiş, renk,kalınlık

#dikdörtgen
cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),thickness=2) #thickness=-1 dersem içi dolu sekilde gelecek
cv2.rectangle(canvas,(50,50),(150,150),(0,255,0),thickness=-1)
             #tual,sol ust kosesi, sag alt kosesi, rengi,kalınlık

#cember
cv2.circle(canvas,(250,250),100,(0,0,255),thickness=-1)
             #tual, merkez, yarıcap, renk, kalınlık


#ucgen cizimi
p1=(100,200)
p2=(50,50)
p3=(300,100)
cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p3,p1,(0,0,0),4)

#rastgele cızgıler cızıp birlestirip cokgen dortgen vb geaometrik sekiller olusturma
points=np.array([[110,200],[330,200],[290,220],[100,100]],np.int32)#veri tipinide belirtmemiz gerekiyor.
cv2.polylines(canvas,[points],True,(0,0,100),5)
              #tual, boyut, kapalı mı acık mı, renk , kalınlık

#ellips
cv2.ellipse(canvas,(300,300),(80,20),10,90,360,(255,255,0),-1)
            #tual, merkez noktası,genişlik yukseklik, yatay eksende yapacagı acı, baslangıc acısı ,bitis acısı, renk, kalınlık

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()