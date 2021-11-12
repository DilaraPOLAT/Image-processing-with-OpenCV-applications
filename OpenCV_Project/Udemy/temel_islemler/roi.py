#ROI: Region of interest-->ilgi alanı
import cv2
img=cv2.imread("klon.jpg")

print(img.shape[0:2]) #Resmin boyutu
roi=img[30:200,200:375]
cv2.imshow("Klon Asker",img)
cv2.imshow("Roi",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()