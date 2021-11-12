import cv2

#img=cv2.imread("klon.jpg",0)  #ya da
img=cv2.imread("C:\\udemyopencv\\klon.jpg",0)
# # print(img)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

cv2.imshow("image",img)
cv2.imwrite("C:\\udemyopencv\\klon1.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



